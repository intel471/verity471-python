from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any

from verity471.api_client import ApiClient
from verity471.models.streaming_alerts_response import StreamingAlertsResponse
from verity471.models.streaming_watcher_alert import StreamingWatcherAlert

from verity471.helpers.url_router import UnresolvableURL, call_url

log = logging.getLogger(__name__)


@dataclass
class AlertTarget:
    """An alert paired with its fully fetched target object.

    ``alert`` is the original :class:`StreamingWatcherAlert` (carries status,
    watcher IDs, timestamps, highlights, etc.).  ``target`` is the resolved API
    object — a report, forum post, credential, or whatever the alert refers to.
    ``target`` is ``None`` when the URL could not be mapped to a known route.

    Convenience properties mirror the most-used fields from ``alert`` so you
    rarely need to drill into ``.alert.source_type``.
    """

    alert: StreamingWatcherAlert
    target: Any

    @property
    def source_type(self) -> str:
        return self.alert.source_type

    @property
    def source_id(self) -> str:
        return self.alert.source_id


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
        except Exception:
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
