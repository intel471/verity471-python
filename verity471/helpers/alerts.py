from __future__ import annotations

import logging
import re
import concurrent.futures
from dataclasses import dataclass
from typing import Any, Optional
from urllib.parse import quote

from verity471.api_client import ApiClient
from verity471.api.watchers_api import WatchersApi
from verity471.exceptions import ForbiddenException
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

_SUMMARY_SNIPPET_LEN = 256  # soft char limit for text snippets; expands to end of current word

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


def _snippet(text: str, limit: int = _SUMMARY_SNIPPET_LEN) -> str:
    """Truncate *text* to roughly *limit* chars, ending on a word boundary."""
    if len(text) <= limit:
        return text
    end = text.find(" ", limit)
    return text[:end] + "\u2026" if end != -1 else text[:limit] + "\u2026"


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
            _snippet(p.message) if p.message else None, p.creation_ts]))

    if isinstance(target, PrivateMessageDetails1):
        pm = target.private_message
        return _prefixed("Forum PM", _join([
            pm.subject, _snippet(pm.message) if pm.message else None, pm.creation_ts]))

    if isinstance(target, ChatRoomMessageStream):
        m = target.message
        return _prefixed("Message", _join([
            _snippet(m.text) if m.text else None, m.creation_ts]))

    if isinstance(target, (BreachAlertByIdResponse, FintelResponse,
                           GeopolReportDetailsResponse, MalwareReportResponse,
                           SpotReportResponse)):
        return _prefixed(_type_label(target.type), _join([
            target.title, target.released_ts,
            _snippet(target.body) if target.body else None]))

    if isinstance(target, InfoReportResponse):
        summary = target.executive_summary or target.body
        return _prefixed(_type_label(target.type), _join([
            target.title, target.released_ts,
            _snippet(summary) if summary else None]))

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
            target.name, aliases,
            _snippet(target.description) if target.description else None]))

    return None


@dataclass
class AlertTarget:
    """An alert paired with its fully fetched target object.

    ``alert`` is the original :class:`StreamingWatcherAlert` (carries status,
    watcher IDs, timestamps, highlights, etc.).  ``target`` is the resolved API
    object — a report, forum post, credential, or whatever the alert refers to.
    ``target`` is ``None`` when the URL could not be mapped to a known route.

    ``target_summary`` provides a compact, human-readable one-liner for the
    target (e.g. report title + date, indicator type + value, credential
    login + domain).

    ``watcher`` is the full :class:`GetWatcherResponse` for the watcher that
    triggered this alert, or ``None`` if not found in the fetched list.
    ``watcher_group`` is the corresponding :class:`GetWatcherGroupResponse`.
    """

    alert: StreamingWatcherAlert
    target: Any
    watcher: GetWatcherResponse | None = None
    watcher_group: GetWatcherGroupResponse | None = None

    @property
    def target_summary(self) -> str | None:
        return _summarize_target(self.target)


def fetch_alert_targets(
    alerts_response: StreamingAlertsResponse,
    api_client: ApiClient,
    raise_on_error: bool = False,
) -> list[AlertTarget]:
    """Fetch the full target object for every alert in *alerts_response*.

    Each :class:`StreamingWatcherAlert` only carries ``source_type``,
    ``source_id``, and a ``links.verity_api.href``.  This helper resolves that
    URL and returns :class:`AlertTarget` pairs so you can work with the actual
    content (report body, forum post text, etc.) alongside the alert metadata.

    URLs that cannot be mapped to a known SDK route always produce an
    :class:`AlertTarget` with ``target=None`` (and emit a warning).  Other
    errors (missing link, API call failure) follow *raise_on_error*: when
    ``True`` the exception propagates; when ``False`` an error is logged and
    the alert is omitted from the result.

    Args:
        alerts_response: The page returned by :meth:`AlertsApi.get_alerts_stream`.
        api_client: An active :class:`ApiClient` (must share credentials with
            the alerts call).
        raise_on_error: When ``True``, re-raise unexpected errors instead of
            logging and skipping the alert. Defaults to ``False``.

    Returns:
        A list of :class:`AlertTarget` objects in the same order as
        ``alerts_response.alerts``.

    Example::

        alerts = alerts_api.get_alerts_stream(size=10)
        for r in fetch_alert_targets(alerts, api_client):
            print(r.alert.source_type, r.alert.status, r.target)
    """
    def _fetch(alert: StreamingWatcherAlert) -> AlertTarget | None:
        url = alert.links.verity_api.href if (alert.links and alert.links.verity_api) else None
        if url and "/integrations/marketplaces/" in url:
            return None
        if not url:
            if raise_on_error:
                raise ValueError("Alert %s has no verity_api link" % alert.source_id)
            log.error("Alert %s has no verity_api link", alert.source_id)
            return None
        try:
            target = call_url(api_client, url)
        except UnresolvableURL:
            log.warning("No SDK route for alert %s URL: %s", alert.source_id, url)
            return AlertTarget(alert=alert, target=None)
        except ForbiddenException:
            log.debug("Failed to fetch target for alert %s (%s) - Forbidden", alert.source_id, url)
            return None
        except Exception:
            if raise_on_error:
                raise
            log.error("Failed to fetch target for alert %s (%s)", alert.source_id, url, exc_info=True)
            return None
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
