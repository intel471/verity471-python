from __future__ import annotations

import enum
import html
import logging
import re
import concurrent.futures
from dataclasses import dataclass
from html.parser import HTMLParser
from typing import Any, Optional
from urllib.parse import quote

from verity471.api_client import ApiClient
from verity471.api.watchers_api import WatchersApi
from verity471.exceptions import ForbiddenException, NotFoundException
from verity471.models.breach_alert_by_id_response import BreachAlertByIdResponse
from verity471.models.chat_room_message_stream import ChatRoomMessageStream
from verity471.models.data_leak_site_post_item import DataLeakSitePostItem
from verity471.models.fintel_response import FintelResponse
from verity471.models.geopol_report_details_response import GeopolReportDetailsResponse
from verity471.models.get_cred_occurrence_response import GetCredOccurrenceResponse
from verity471.models.get_cred_response import GetCredResponse
from verity471.models.get_cred_set_response import GetCredSetResponse
from verity471.models.href import Href
from verity471.models.info_report_response import InfoReportResponse
from verity471.models.integrations_event import IntegrationsEvent
from verity471.models.integrations_indicator import IntegrationsIndicator
from verity471.models.malware_report_response import MalwareReportResponse
from verity471.models.post_details1 import PostDetails1
from verity471.models.private_message_details1 import PrivateMessageDetails1
from verity471.models.simplified_malware_profile import SimplifiedMalwareProfile
from verity471.models.spot_report_response import SpotReportResponse
from verity471.models.get_watcher_group_response import GetWatcherGroupResponse
from verity471.models.get_watcher_response import GetWatcherResponse
from verity471.models.streaming_alerts_response import StreamingAlertsResponse
from verity471.models.streaming_watcher_alert import StreamingWatcherAlert
from verity471.models.vulnerabilities_report_details_response import VulnerabilitiesReportDetailsResponse

from verity471.helpers.url_router import UnresolvableURL, call_url

log = logging.getLogger(__name__)

# Target types an alert can reference that the SDK deliberately has no route for
# yet. A missing route for one of these is expected, so it is logged at DEBUG; a URL
# outside this set is unexpected and stays a WARNING, as it may mean the SDK needs a
# new route.
KNOWN_UNSUPPORTED_TARGET_PATHS = ("/integrations/marketplaces/",)

_SUMMARY_SNIPPET_LEN = 256  # soft char limit for text snippets; expands to end of current word
_SNIPPET_OVERRUN = 32  # max extra chars that word-boundary expansion may add

# Elements whose *content* is markup machinery, not text, and is dropped with them.
_SKIPPED_ELEMENTS = frozenset({"script", "style"})

# Elements that imply a word boundary, so that "<p>foo</p><p>bar</p>" reads as
# "foo bar" and not "foobar". Inline elements (<b>, <a>, <em>, ...) are absent
# on purpose: they must not push a space into the middle of a sentence.
_BLOCK_ELEMENTS = frozenset({
    "address", "article", "aside", "blockquote", "br", "caption", "dd", "div",
    "dl", "dt", "figcaption", "figure", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "header", "hr", "img", "li", "main", "nav", "ol", "p",
    "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
})

# ---------------------------------------------------------------------------
# TEMPORARY WORKAROUND — remove this block (and its call site in _fetch)
# once the API populates links.verity_portal on all alert types.
# ---------------------------------------------------------------------------

def _patch_portal_url(alert: StreamingWatcherAlert, target: Any) -> None:
    """Backfill alert.links.verity_portal when the API omits it.

    Temporary workaround for an API bug where certain source types do not
    include a verity_portal link.  Remove once the API is fixed.
    """
    # Geopol reports return /intelligence/geopolReportView/{id} but the correct
    # path prefix is /geopol/.
    if isinstance(target, GeopolReportDetailsResponse):
        if (alert.links and alert.links.verity_portal
                and alert.links.verity_portal.href):
            alert.links.verity_portal.href = alert.links.verity_portal.href.replace(
                "intel471.com/intelligence/geopolReportView/",
                "intel471.com/geopol/geopolReportView/",
                1,
            )
        return

    if alert.links and alert.links.verity_portal:
        return

    url: str | None = None

    if isinstance(target, PostDetails1):
        thread = target.thread
        if (thread and thread.links and thread.links.verity_portal
                and thread.links.verity_portal.href):
            url = thread.links.verity_portal.href + "?postId=" + target.post.id

    elif isinstance(target, DataLeakSitePostItem):
        post = target.post
        if (post and post.links and post.links.verity_portal
                and post.links.verity_portal.href):
            url = post.links.verity_portal.href

    elif isinstance(target, ChatRoomMessageStream):
        msg = target.message
        if (msg.links and msg.links.verity_portal
                and msg.links.verity_portal.href):
            url = msg.links.verity_portal.href + "?messageId=" + msg.id

    elif isinstance(target, GetCredSetResponse):
        if target.data.name:
            q = quote("cred_set.name=" + target.data.name, safe="")
            url = f"https://verity.intel471.com/search?q={q}&category=creds_cred_set"

    if url:
        alert.links.verity_portal = Href(href=url)
    else:
        log.debug(
            "Could not build portal URL for alert %s (source_type=%s)",
            alert.source_id, alert.source_type,
        )

# ---------------------------------------------------------------------------
# END TEMPORARY WORKAROUND
# ---------------------------------------------------------------------------


def _defang(text: Optional[str]) -> str:
    text = str(text).replace("http://", "hxxp://").replace("https://", "hxxps://")
    return re.sub(r"(\w)\.(\w)", r"\1[.]\2", text)


class _PlainTextParser(HTMLParser):
    """Collect the visible text of an HTML fragment.

    One instance per call: :class:`HTMLParser` is stateful, and summaries are
    built from a thread pool.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)  # entities arrive already unescaped
        self.parts: list[str] = []
        self._skipping = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in _SKIPPED_ELEMENTS:
            self._skipping += 1
        elif tag in _BLOCK_ELEMENTS:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIPPED_ELEMENTS:
            self._skipping = max(self._skipping - 1, 0)  # stray close tag
        elif tag in _BLOCK_ELEMENTS:
            self.parts.append(" ")

    def handle_data(self, data: str) -> None:
        if not self._skipping:
            self.parts.append(data)


def _plain_text(value: Optional[str]) -> Optional[str]:
    """Flatten an HTML-bearing field into a single line of visible text.

    Report bodies, forum posts and chat messages are HTML. Consumers that
    render a summary as plain text (chat bots, SIEM connectors) would otherwise
    show literal markup, and the tags would eat into the snippet budget.

    Tags go, with the content of ``<script>``/``<style>``; entities are
    unescaped; block boundaries become whitespace; whitespace runs collapse.
    Plain text passes through unchanged apart from that collapsing. Returns
    ``None`` when nothing visible is left, so ``x if x else None`` call sites
    keep working, and never raises - a summary must not break a fetch.
    """
    if not value:
        return None
    try:
        parser = _PlainTextParser()
        parser.feed(value)
        parser.close()
        text = "".join(parser.parts)
    except Exception:  # noqa: BLE001 - malformed markup must not lose the text
        log.debug("Could not parse HTML for summary, using raw text", exc_info=True)
        text = html.unescape(value)
    else:
        # A fragment cut mid-tag ('...<a href="htt') is flushed as data by
        # close(); drop it rather than surface markup as text.
        cut = text.rfind("<")
        if cut != -1 and ">" not in text[cut:]:
            text = text[:cut] + " "
    return " ".join(text.split()) or None


def _snippet(text: str, limit: int = _SUMMARY_SNIPPET_LEN) -> str:
    """Truncate *text* to roughly *limit* chars, ending on a word boundary."""
    if len(text) <= limit:
        return text
    end = text.find(" ", limit)
    if end == -1 or end > limit + _SNIPPET_OVERRUN:
        end = limit  # an unbroken run (long URL, base64 blob): cut it hard
    return text[:end] + "\u2026"


def _text_snippet(value: Optional[str], limit: int = _SUMMARY_SNIPPET_LEN) -> Optional[str]:
    """Snippet of an HTML-bearing field: strip first, then truncate.

    In that order *limit* counts visible characters, instead of a budget spent
    on markup that is about to be thrown away (and a cut landing mid-tag).
    """
    text = _plain_text(value)
    return _snippet(text, limit) if text else None


def _join(parts: list) -> str | None:
    joined = " | ".join(str(p) for p in parts if p)
    return joined or None


def _type_label(snake: str) -> str:
    return snake.replace("_", " ").title()


def _prefixed(label: str, rest: str | None) -> str | None:
    prefix = f"[{label}]"
    return f"{prefix} {rest}" if rest else prefix


def _summarize_target(target: Any) -> str | None:
    if target is None or isinstance(target, (bytes, bytearray)):
        return None

    if isinstance(target, PostDetails1):
        p = target.post
        return _prefixed("Forum Post", _join([
            _text_snippet(p.message), p.creation_ts]))

    if isinstance(target, PrivateMessageDetails1):
        pm = target.private_message
        return _prefixed("Forum PM", _join([
            _plain_text(pm.subject), _text_snippet(pm.message), pm.creation_ts]))

    if isinstance(target, ChatRoomMessageStream):
        m = target.message
        return _prefixed("Message", _join([
            _text_snippet(m.text), m.creation_ts]))

    if isinstance(target, (BreachAlertByIdResponse, FintelResponse,
                           GeopolReportDetailsResponse, MalwareReportResponse,
                           SpotReportResponse)):
        return _prefixed(_type_label(target.type), _join([
            _plain_text(target.title), target.released_ts,
            _text_snippet(target.body)]))

    if isinstance(target, InfoReportResponse):
        # Fall back to the body when the summary holds no visible text.
        summary = _text_snippet(target.executive_summary) or _text_snippet(target.body)
        return _prefixed(_type_label(target.type), _join([
            _plain_text(target.title), target.released_ts, summary]))

    if isinstance(target, VulnerabilitiesReportDetailsResponse):
        return _prefixed(_type_label(target.type), _join([
            target.name, target.vendor_name, target.product_name,
            str(target.risk_level), str(target.status)]))

    if isinstance(target, GetCredOccurrenceResponse):
        return _prefixed("Credential Occurrence", _join([
            _defang(target.data.accessed_url) if target.data.accessed_url else None,
            target.data.credential_type, target.last_updated_ts]))

    if isinstance(target, GetCredResponse):
        return _prefixed("Credential", _join([
            target.data.credential_login,
            _defang(target.data.credential_domain) if target.data.credential_domain else None,
            target.last_updated_ts]))

    if isinstance(target, GetCredSetResponse):
        return _prefixed("Credential Set", _join([
            target.data.name,
            f"{target.data.record_count} records" if target.data.record_count else None,
            target.data.breach_ts]))

    if isinstance(target, IntegrationsIndicator):
        value = None
        if target.data:
            value = (target.data.domain or target.data.email or target.data.url
                     or (target.data.file.sha256 if target.data.file else None)
                     or (target.data.ipv4.ip_address if target.data.ipv4 else None))
        conf = f"confidence: {target.confidence}" if target.confidence is not None else None
        return _prefixed("Indicator", _join([target.type, _defang(value) if value else None, conf]))

    if isinstance(target, IntegrationsEvent):
        family_str = None
        if target.threat and target.threat.data:
            td = target.threat.data
            name = td.malware_family.name if td.malware_family else None
            version = td.malware.version if td.malware else None
            if name:
                family_str = f"{name} v{version}" if version else name

        parts: list = []
        d = target.data
        if d:
            if d.attack_type:
                parts.append(d.attack_type)
            if d.inject_type:
                parts.append(d.inject_type)
            if d.plugin_type:
                parts.append(d.plugin_type)
            elif d.plugin_name:
                parts.append(d.plugin_name)
            if d.component_type:
                parts.append(d.component_type)
            if d.target_type:
                parts.append(f"target: {d.target_type}")
            if d.exfil_location:
                parts.append(f"exfil: {_defang(d.exfil_location)}")
            elif d.controllers and d.controllers[0].url:
                parts.append(f"C2: {_defang(d.controllers[0].url)}")
            elif d.controller and d.controller.url:
                parts.append(f"C2: {_defang(d.controller.url)}")

        label = _type_label(target.type) if target.type else "Event"
        return _prefixed(label, _join([family_str] + parts))

    if isinstance(target, SimplifiedMalwareProfile):
        aliases = ", ".join(target.aliases[:3]) if target.aliases else None
        return _prefixed("Malware", _join([
            target.name, aliases, _text_snippet(target.description)]))

    return None


def _summarize_alert(alert: StreamingWatcherAlert) -> str | None:
    """Best-effort one-liner from the alert envelope alone (no target needed).

    Used as a fallback when the target couldn't be fetched or isn't
    summarizable: ``"<Type>: <url>"`` plus the first highlight snippet if
    present.
    """
    label = _type_label(alert.source_type) if alert.source_type else None

    url = None
    if alert.links:
        if alert.links.verity_portal and alert.links.verity_portal.href:
            url = alert.links.verity_portal.href
        elif alert.links.verity_api and alert.links.verity_api.href:
            url = alert.links.verity_api.href

    head = f"{label}: {url}" if (label and url) else (label or url)

    snippet = None
    if alert.highlights and alert.highlights[0].snippets:
        snippet = _snippet(alert.highlights[0].snippets[0])

    return _join([head, snippet])


class AlertTargetStatus(str, enum.Enum):
    """HTTP-style outcome of fetching an alert's target."""

    OK = "ok"                      # target fetched
    NO_LINK = "no_link"            # alert had no links.verity_api.href
    UNRESOLVABLE = "unresolvable"  # URL matched no known SDK route (404-ish)
    FORBIDDEN = "forbidden"        # API returned 403
    NOT_FOUND = "not_found"        # target no longer exists (404)
    ERROR = "error"                # unexpected fetch error (5xx-ish)


@dataclass
class AlertTarget:
    """An alert paired with its fully fetched target object.

    ``alert`` is the original :class:`StreamingWatcherAlert` (carries status,
    watcher IDs, timestamps, highlights, etc.).  ``target`` is the resolved API
    object — a report, forum post, credential, or whatever the alert refers to.
    ``target`` is ``None`` when the URL could not be mapped to a known route.

    ``status`` is the :class:`AlertTargetStatus` for the fetch — ``OK`` when the
    target was fetched, otherwise the reason it could not be (``NO_LINK``,
    ``UNRESOLVABLE``, ``FORBIDDEN``, ``NOT_FOUND``, ``ERROR``).  ``target is
    None`` together with ``status != OK`` means the fetch failed;
    ``status_reason`` carries the human-readable detail (e.g. the URL or the
    underlying error message).

    ``target_summary`` provides a compact, human-readable one-liner for the
    target (e.g. report title + date, indicator type + value, credential
    login + domain).  When the target is missing or not summarizable, it falls
    back to a summary built from the alert envelope itself.

    ``watcher`` is the full :class:`GetWatcherResponse` for the watcher that
    triggered this alert, or ``None`` if not found in the fetched list.
    ``watcher_group`` is the corresponding :class:`GetWatcherGroupResponse`.
    """

    alert: StreamingWatcherAlert
    target: Any
    status: AlertTargetStatus = AlertTargetStatus.OK
    status_reason: str | None = None
    watcher: GetWatcherResponse | None = None
    watcher_group: GetWatcherGroupResponse | None = None

    @property
    def target_summary(self) -> str | None:
        return _summarize_target(self.target) or _summarize_alert(self.alert)


def fetch_alert_targets(
    alerts_response: StreamingAlertsResponse,
    api_client: ApiClient,
    raise_on_error: bool = False,
    skip_missing_targets: bool = False,
    include_inline_images: bool = True,
) -> list[AlertTarget]:
    """Fetch the full target object for every alert in *alerts_response*.

    Each :class:`StreamingWatcherAlert` only carries ``source_type``,
    ``source_id``, and a ``links.verity_api.href``.  This helper resolves that
    URL and returns :class:`AlertTarget` pairs so you can work with the actual
    content (report body, forum post text, etc.) alongside the alert metadata.

    When a target cannot be fetched (no link, no known SDK route, forbidden,
    gone, or an unexpected error), the behaviour depends on
    *skip_missing_targets*: by default (``False``) the alert is still returned
    with ``target=None`` and a non-``OK`` :class:`AlertTargetStatus` (plus a
    ``status_reason``) so callers can see it failed and why; when ``True`` such
    alerts are omitted from the result entirely.  Marketplace alerts have no SDK route yet, so they are
    treated like any other unresolvable target: returned as bare alerts with
    ``status=UNRESOLVABLE`` by default, or omitted when *skip_missing_targets*
    is ``True``.

    Args:
        alerts_response: The page returned by :meth:`AlertsApi.get_alerts_stream`.
        api_client: An active :class:`ApiClient` (must share credentials with
            the alerts call).
        raise_on_error: When ``True``, re-raise unexpected errors (and the
            missing-link ``ValueError``) instead of recording them on the
            result. Defaults to ``False``.
        skip_missing_targets: When ``True``, alerts whose target cannot be
            fetched are omitted from the result. When ``False`` (default) they
            are returned with ``target=None`` and a failure ``status``.
            Defaults to ``False``.
        include_inline_images: When ``True`` (default), report targets are
            fetched with their images embedded in the body as base64 data URIs,
            matching what the report-by-id endpoints return with
            ``include_inline_images=true``. Set to ``False`` for smaller
            responses, leaving the images as bare attachment URLs. Ignored by
            target types that have no such option.

    Returns:
        A list of :class:`AlertTarget` objects in the same order as
        ``alerts_response.alerts``.

    Example::

        alerts = alerts_api.get_alerts_stream(size=10)
        for r in fetch_alert_targets(alerts, api_client):
            print(r.alert.source_type, r.status, r.status_reason, r.target)
    """
    def _fetch(alert: StreamingWatcherAlert) -> AlertTarget | None:
        url = alert.links.verity_api.href if (alert.links and alert.links.verity_api) else None
        if not url:
            if raise_on_error:
                raise ValueError("Alert %s has no verity_api link" % alert.source_id)
            log.error("Alert %s has no verity_api link", alert.source_id)
            if skip_missing_targets:
                return None
            return AlertTarget(alert=alert, target=None, status=AlertTargetStatus.NO_LINK,
                               status_reason="Alert has no verity_api link")
        try:
            target = call_url(api_client, url, include_inline_images=include_inline_images)
        except UnresolvableURL:
            if any(path in url for path in KNOWN_UNSUPPORTED_TARGET_PATHS):
                log.debug("No SDK route for alert %s URL: %s (known unsupported target type)",
                          alert.source_id, url)
            else:
                log.warning("No SDK route for alert %s URL: %s", alert.source_id, url)
            if skip_missing_targets:
                return None
            return AlertTarget(alert=alert, target=None, status=AlertTargetStatus.UNRESOLVABLE,
                               status_reason=f"No SDK route for URL: {url}")
        except ForbiddenException:
            log.debug("Failed to fetch target for alert %s (%s) - Forbidden", alert.source_id, url)
            if skip_missing_targets:
                return None
            return AlertTarget(alert=alert, target=None, status=AlertTargetStatus.FORBIDDEN,
                               status_reason="Forbidden (403) fetching target")
        except NotFoundException:
            # Routine: source content ages out or is removed, and there can be a
            # brief consistency lag. One line, no traceback or header dump.
            if raise_on_error:
                raise
            log.warning("Alert %s target not found (404): %s", alert.source_id, url)
            if skip_missing_targets:
                return None
            return AlertTarget(alert=alert, target=None, status=AlertTargetStatus.NOT_FOUND,
                               status_reason=f"Target not found (404): {url}")
        except Exception as exc:
            if raise_on_error:
                raise
            log.error("Failed to fetch target for alert %s (%s)", alert.source_id, url, exc_info=True)
            if skip_missing_targets:
                return None
            return AlertTarget(alert=alert, target=None, status=AlertTargetStatus.ERROR,
                               status_reason=f"Error fetching target: {exc}")
        _patch_portal_url(alert, target)  # TEMPORARY WORKAROUND — remove once API is fixed
        return AlertTarget(alert=alert, target=target)

    alerts = alerts_response.alerts or []
    results: list[AlertTarget] = [None] * len(alerts)  # type: ignore[list-item]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_index = {executor.submit(_fetch, alert): i for i, alert in enumerate(alerts)}
        for future in concurrent.futures.as_completed(future_to_index):
            result = future.result()
            if result is not None:
                results[future_to_index[future]] = result

    enriched = [r for r in results if r is not None]
    if not enriched:
        return []

    try:
        watchers_api = WatchersApi(api_client)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as watcher_executor:
            future_watchers = watcher_executor.submit(watchers_api.get_watchers)
            future_groups = watcher_executor.submit(watchers_api.get_watcher_groups)
            watchers_resp = future_watchers.result()
            groups_resp = future_groups.result()
        watchers_by_id = {w.id: w for w in (watchers_resp.watchers or [])}
        groups_by_id = {g.id: g for g in (groups_resp.watchers_groups or [])}
        for r in enriched:
            r.watcher = watchers_by_id.get(r.alert.watcher_id)
            r.watcher_group = groups_by_id.get(r.alert.watcher_group_id)
    except Exception:
        log.warning("Failed to fetch watchers/watcher groups; watcher enrichment will be skipped", exc_info=True)

    return enriched
