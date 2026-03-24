from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any

from verity471.api_client import ApiClient
from verity471.models.breach_alert_by_id_response import BreachAlertByIdResponse
from verity471.models.chat_room_message_stream import ChatRoomMessageStream
from verity471.models.fintel_response import FintelResponse
from verity471.models.geopol_report_details_response import GeopolReportDetailsResponse
from verity471.models.get_cred_occurrence_response import GetCredOccurrenceResponse
from verity471.models.get_cred_response import GetCredResponse
from verity471.models.get_cred_set_response import GetCredSetResponse
from verity471.models.info_report_response import InfoReportResponse
from verity471.models.integrations_event import IntegrationsEvent
from verity471.models.integrations_indicator import IntegrationsIndicator
from verity471.models.malware_report_response import MalwareReportResponse
from verity471.models.post_details1 import PostDetails1
from verity471.models.private_message_details1 import PrivateMessageDetails1
from verity471.models.simplified_malware_profile import SimplifiedMalwareProfile
from verity471.models.spot_report_response import SpotReportResponse
from verity471.models.streaming_alerts_response import StreamingAlertsResponse
from verity471.models.streaming_watcher_alert import StreamingWatcherAlert
from verity471.models.vulnerabilities_report_details_response import VulnerabilitiesReportDetailsResponse

from verity471.helpers.url_router import UnresolvableURL, call_url

log = logging.getLogger(__name__)

_SUMMARY_SNIPPET_LEN = 256  # soft char limit for text snippets; expands to end of current word


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
            target.data.accessed_url, target.data.credential_type, target.last_updated_ts]))

    if isinstance(target, GetCredResponse):
        return _prefixed("Credential", _join([
            target.data.credential_login, target.data.credential_domain, target.last_updated_ts]))

    if isinstance(target, GetCredSetResponse):
        return _prefixed("Credential Set", _join([
            target.data.name,
            f"{target.data.record_count} records" if target.data.record_count else None,
            target.data.breach_ts]))

    if isinstance(target, IntegrationsIndicator):
        value = None
        if target.data:
            value = (target.data.domain or target.data.email or target.data.url or target.data.file.sha256
                     or (target.data.ipv4.ip_address if target.data.ipv4 else None))
        conf = f"confidence: {target.confidence}" if target.confidence is not None else None
        return _prefixed("Indicator", _join([target.type, value, conf]))

    if isinstance(target, IntegrationsEvent):
        family = None
        if target.threat and target.threat.data and target.threat.data.malware_family:
            family = target.threat.data.malware_family.name
        label = _type_label(target.type) if target.type else "Event"
        return _prefixed(label, _join([
            family, target.data.attack_type if target.data else None]))

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

    Convenience properties mirror the most-used fields from ``alert`` so you
    rarely need to drill into ``.alert.source_type``.  ``target_summary``
    provides a compact, human-readable one-liner for the target (e.g. report
    title + date, indicator type + value, credential login + domain).
    """

    alert: StreamingWatcherAlert
    target: Any

    @property
    def source_type(self) -> str:
        return self.alert.source_type

    @property
    def source_id(self) -> str:
        return self.alert.source_id

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
            print(r.source_type, r.alert.status, r.target)
    """
    def _fetch(alert: StreamingWatcherAlert) -> AlertTarget | None:
        url = alert.links.verity_api.href if (alert.links and alert.links.verity_api) else None
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
        except Exception as e:
            if raise_on_error:
                raise
            log.error("Failed to fetch target for alert %s (%s)", alert.source_id, url, exc_info=True)
            return None
        return AlertTarget(alert=alert, target=target)

    alerts = alerts_response.alerts or []
    results: list[AlertTarget] = [None] * len(alerts)  # type: ignore[list-item]
    with ThreadPoolExecutor() as executor:
        future_to_index = {executor.submit(_fetch, alert): i for i, alert in enumerate(alerts)}
        for future in as_completed(future_to_index):
            result = future.result()
            if result is not None:
                results[future_to_index[future]] = result
    return [r for r in results if r is not None]
