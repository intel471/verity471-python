# coding: utf-8

"""Helper for fetching the most recent N items from any stream endpoint.

Stream endpoints only return data in ascending (oldest-first) order.  To get
the *latest* N results the helper probes the API with progressively wider time
windows until ``count >= n``, then performs a single fetch (or a short
pagination run for very high-density endpoints) and slices the tail.

Usage::

    import verity471
    from verity471.helpers import get_latest

    cfg = verity471.Configuration(username=..., password=...)
    with verity471.ApiClient(cfg) as client:
        api = verity471.ReportsApi(client)
        reports = get_latest(api.get_reports_spot_stream, n=20)

        # Domain-specific filters are forwarded as keyword arguments:
        events = get_latest(
            verity471.EventsApi(client).get_events_stream,
            n=50,
            malware_family_name="Cobalt Strike",
        )
"""

from __future__ import annotations

import logging
import time
from typing import Any, Callable

log = logging.getLogger(__name__)

# Initial probe window in seconds per stream method, derived from observed
# data density (counts at 1 h / 24 h / 7 d / 30 d).  The algorithm doubles
# this window until count >= n, so a good starting point reduces round-trips.
_INITIAL_WINDOW_SECONDS: dict[str, int] = {
    "get_messaging_services_messages_stream": 60,          # ~23 700/h
    "get_events_stream":                      300,         # ~3 690/h  (malware events)
    "get_forums_posts_stream":                300,         # ~2 897/h
    "get_alerts_stream":                      3_600,       # ~19/h     (1 h)
    "get_reports_breach_alert_stream":        43_200,      # ~1.4/h    (12 h)
    "get_reports_stream":                     86_400,      # ~2/h      (24 h)
    "get_reports_fintel_stream":              604_800,     # ~0.5/day  (7 d)
    "get_reports_geopol_stream":              604_800,     # ~0.5/day  (7 d)
    "get_reports_info_stream":                604_800,     # ~0.25/day (7 d)
    "get_reports_spot_stream":                604_800,     # ~0.5/day  (7 d)
    "get_reports_vulnerability_stream":       604_800,     # ~5/day    (7 d)
    "get_reports_malware_stream":             1_209_600,   # ~0.1/day  (14 d)
    "get_credentials_stream":                 1_209_600,   # ~0.1/day  (14 d)
    "get_credentials_occurrences_stream":     1_209_600,
    "get_credential_sets_stream":             1_209_600,
    "get_credential_sets_accessed_urls_stream": 1_209_600,
    "get_data_leak_sites_posts_stream":       5_184_000,   # ~1/month  (60 d)
    "get_forums_private_messages_stream":     5_184_000,
    "get_indicators_stream":                  300,         # assumed similar to events
    "get_actors_stream":                      86_400,      # requires search term
    "get_observables_stream":                 86_400,
    "get_entities_stream":                    86_400,
}
_DEFAULT_INITIAL_WINDOW_SECONDS = 86_400        # 24 h fallback for unknown methods
_MAX_WINDOW_SECONDS = 365 * 24 * 3_600          # 1-year hard cap


def _extract_items(response: Any) -> list:
    """Return the items list from a stream response object.

    Every stream response has exactly three fields: ``count``, ``cursor_next``,
    and one items field (e.g. ``reports``, ``events``, ``credentials``).  This
    function returns that third field without needing to know its name.
    """
    for field_name in response.model_fields:
        if field_name not in ("count", "cursor_next"):
            value = getattr(response, field_name)
            if isinstance(value, list):
                return value
    return []


def get_latest(stream_method: Callable, n: int, **kwargs: Any) -> list:
    """Return the *n* most recent items from a stream endpoint.

    Args:
        stream_method: A bound stream API method, e.g.
            ``reports_api.get_reports_spot_stream``.
        n: Number of most-recent items to return.  When fewer than *n* items
            exist across the entire history the function returns however many
            are available (possibly an empty list).
        **kwargs: Additional filter parameters forwarded verbatim to the stream
            method (e.g. ``malware_family_name``, ``threat_type``, ``girs``).
            Do **not** pass ``var_from``, ``until``, ``size``, or ``cursor`` —
            these are managed internally.

    Returns:
        A list of at most *n* items in ascending order (oldest first), i.e. the
        last element is always the single most-recent item.

    Raises:
        ValueError: If any of the internally-managed parameters (``var_from``,
            ``until``, ``size``, ``cursor``) appear in *kwargs*.
    """
    method_name = getattr(stream_method, "__name__", "")

    if not method_name.endswith("_stream"):
        raise ValueError(
            f"{method_name!r} does not appear to be a stream method; "
            "method name must end with '_stream'."
        )

    reserved = {"var_from", "until", "size", "cursor"}
    if conflicts := reserved & kwargs.keys():
        raise ValueError(
            f"get_latest manages {sorted(conflicts)} internally; "
            "do not pass them as keyword arguments."
        )

    now_ms = int(time.time() * 1000)
    window_s = _INITIAL_WINDOW_SECONDS.get(method_name, _DEFAULT_INITIAL_WINDOW_SECONDS)

    # Phase 1: exponential expansion until count >= n or the 1-year cap is hit.
    from_ms = now_ms - window_s * 1000
    count = 0
    while True:
        from_ms = now_ms - window_s * 1000
        resp = stream_method(var_from=from_ms, until=now_ms, size=1, **kwargs)
        count = resp.count
        log.debug(
            "%s probe: window=%ds from_ms=%d count=%d (target n=%d)",
            method_name, window_s, from_ms, count, n,
        )
        if count >= n or window_s >= _MAX_WINDOW_SECONDS:
            break
        window_s = min(window_s * 2, _MAX_WINDOW_SECONDS)

    if count == 0:
        return []

    # Phase 2a: everything fits in one page — single fetch, slice the tail.
    if count <= 1000:
        resp = stream_method(var_from=from_ms, until=now_ms, size=count, **kwargs)
        return _extract_items(resp)[-n:]

    # Phase 2b: high-density burst — paginate and keep only the last n items.
    log.debug(
        "%s: count=%d > 1000, paginating to collect last %d items", method_name, count, n
    )
    buffer: list = []
    cursor: str | None = None
    while len(buffer) < count:
        if cursor:
            resp = stream_method(cursor=cursor, size=1000, **kwargs)
        else:
            resp = stream_method(var_from=from_ms, until=now_ms, size=1000, **kwargs)
        buffer.extend(_extract_items(resp))
        cursor = resp.cursor_next
        if not cursor:
            break
    return buffer[-n:]
