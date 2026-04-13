from unittest.mock import MagicMock, patch

import pytest

from verity471.helpers.stream_latest import _extract_items, get_latest


def _make_response(count, items, cursor_next=None, items_field="reports"):
    resp = MagicMock()
    resp.count = count
    resp.cursor_next = cursor_next
    resp.model_fields = {"count": None, "cursor_next": None, items_field: None}
    setattr(resp, items_field, items)
    return resp


def _method(name="get_reports_spot_stream"):
    m = MagicMock()
    m.__name__ = name
    return m


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def test_non_stream_method_raises():
    with pytest.raises(ValueError, match="stream"):
        get_latest(_method("get_reports_spot"), n=5)


@pytest.mark.parametrize("kwarg", ["var_from", "until", "size", "cursor"])
def test_reserved_kwarg_raises(kwarg):
    with pytest.raises(ValueError, match="internally"):
        get_latest(_method(), n=5, **{kwarg: "x"})


# ---------------------------------------------------------------------------
# Empty / sparse data
# ---------------------------------------------------------------------------

def test_empty_history_returns_empty_list():
    m = _method()
    m.return_value = _make_response(count=0, items=[])
    assert get_latest(m, n=5) == []


def test_fewer_items_than_n_returns_all_available():
    # count=3 < n=10 even at the max window; returns whatever is there
    items = ["a", "b", "c"]
    m = _method()
    m.return_value = _make_response(count=3, items=items)
    assert get_latest(m, n=10) == items


# ---------------------------------------------------------------------------
# Single-fetch path  (count <= 1000)
# ---------------------------------------------------------------------------

@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_single_fetch_returns_last_n(_):
    items = list(range(33))
    m = _method()
    m.side_effect = [
        _make_response(count=33, items=items[:1]),   # probe
        _make_response(count=33, items=items),       # fetch
    ]
    assert get_latest(m, n=20) == items[-20:]


@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_until_is_pinned_across_all_calls(_):
    now_ms = 1_000_000_000
    items = ["x"]
    m = _method()
    m.side_effect = [
        _make_response(count=1, items=items),   # probe
        _make_response(count=1, items=items),   # fetch
    ]
    get_latest(m, n=1)
    for c in m.call_args_list:
        assert c.kwargs["until"] == now_ms


@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_extra_kwargs_forwarded_to_every_call(_):
    items = list(range(5))
    m = _method()
    m.side_effect = [
        _make_response(count=5, items=items[:1]),   # probe
        _make_response(count=5, items=items),       # fetch
    ]
    get_latest(m, n=3, threat_type="apt")
    for c in m.call_args_list:
        assert c.kwargs.get("threat_type") == "apt"


# ---------------------------------------------------------------------------
# Window expansion
# ---------------------------------------------------------------------------

@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_window_expands_until_count_sufficient(_):
    # Unknown method → default 86 400 s initial window.
    # Probe 1: count=2 < n=10 → expand.  Probe 2: count=15 >= n=10 → fetch.
    items = list(range(15))
    m = _method("get_unknown_endpoint_stream")
    m.side_effect = [
        _make_response(count=2,  items=items[:1]),   # probe 1
        _make_response(count=15, items=items[:1]),   # probe 2
        _make_response(count=15, items=items),       # fetch
    ]
    result = get_latest(m, n=10)
    assert result == items[-10:]
    assert m.call_count == 3


@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_window_doubles_between_probes(_):
    now_ms = 1_000_000_000
    initial_s = 86_400  # default for unknown method
    items = list(range(5))
    m = _method("get_unknown_endpoint_stream")
    m.side_effect = [
        _make_response(count=0, items=[]),           # probe 1: window=86 400
        _make_response(count=5, items=items[:1]),    # probe 2: window=172 800
        _make_response(count=5, items=items),        # fetch
    ]
    get_latest(m, n=5)
    probe1, probe2, _ = m.call_args_list
    assert probe1.kwargs["var_from"] == now_ms - initial_s * 1000
    assert probe2.kwargs["var_from"] == now_ms - initial_s * 2 * 1000


# ---------------------------------------------------------------------------
# Pagination path  (count > 1000)
# ---------------------------------------------------------------------------

@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_pagination_collects_across_multiple_pages(_):
    page1 = list(range(0, 1000))
    page2 = list(range(1000, 2000))
    page3 = list(range(2000, 2500))
    m = _method()
    m.side_effect = [
        _make_response(count=2500, items=page1[:1]),                        # probe
        _make_response(count=2500, items=page1, cursor_next="c1"),          # page 1
        _make_response(count=2500, items=page2, cursor_next="c2"),          # page 2
        _make_response(count=2500, items=page3, cursor_next="c3"),          # page 3
    ]
    assert get_latest(m, n=100) == (page1 + page2 + page3)[-100:]


@patch("verity471.helpers.stream_latest.time.time", return_value=1_000_000.0)
def test_pagination_stops_at_count_not_cursor(_):
    # count=1500; cursor is always present but loop must stop after 2 pages
    page1 = list(range(1000))
    page2 = list(range(1000, 1500))
    m = _method()
    m.side_effect = [
        _make_response(count=1500, items=page1[:1]),                        # probe
        _make_response(count=1500, items=page1, cursor_next="c1"),          # page 1
        _make_response(count=1500, items=page2, cursor_next="c2"),          # page 2 → stop
        _make_response(count=1500, items=[],    cursor_next="c3"),          # must NOT be called
    ]
    get_latest(m, n=50)
    assert m.call_count == 3  # probe + 2 pages


# ---------------------------------------------------------------------------
# _extract_items
# ---------------------------------------------------------------------------

def test_extract_items_returns_list_field():
    resp = MagicMock()
    resp.model_fields = {"count": None, "cursor_next": None, "reports": None}
    resp.reports = ["item1", "item2"]
    assert _extract_items(resp) == ["item1", "item2"]


def test_extract_items_skips_integer_count_fields():
    # ReportResponseStream carries multiple *_count integer sub-totals
    resp = MagicMock()
    resp.model_fields = {
        "count": None,
        "info_report_count": None,
        "fintel_report_count": None,
        "cursor_next": None,
        "reports": None,
    }
    resp.info_report_count = 14363
    resp.fintel_report_count = 1824
    resp.reports = ["r1", "r2"]
    assert _extract_items(resp) == ["r1", "r2"]


def test_extract_items_returns_empty_when_no_list_field():
    resp = MagicMock()
    resp.model_fields = {"count": None, "cursor_next": None}
    assert _extract_items(resp) == []
