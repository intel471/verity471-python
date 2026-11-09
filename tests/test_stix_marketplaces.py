"""Tests for the marketplaces STIX mappers (marketplace, vendor, product, resource)."""
import copy
import datetime
import json
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from verity471.helpers.alerts import AlertTarget
from verity471.models.integration_marketplace_response import IntegrationMarketplaceResponse
from verity471.models.integration_product_response import IntegrationProductResponse
from verity471.models.integration_resource_response import IntegrationResourceResponse
from verity471.verity_stix import STIXMapperSettings
from verity471.verity_stix.exceptions import EmptyBundle
from verity471.verity_stix.mappers.common import StixMapper
from verity471.verity_stix.mappers.marketplaces import product_url
import verity471.verity_stix.mappers  # noqa: F401 - ensure all mappers register

from .conftest import PREFIX, read_fixture

API = f"{PREFIX}/fixtures/api_responses"
Z = "00000000-0000-0000-0000-000000000000"
MARKETPLACE_ID = f"marketplace-website--{Z}"
PRODUCT_ID = f"marketplace-product--{Z}"


def _fixture(fixture_name, **overrides):
    data = copy.deepcopy(read_fixture(f"{API}/{fixture_name}.json"))
    data.update(overrides)
    return data


def _bot_product(**overrides):
    return _fixture("IntegrationProductResponse", kind="bot", title="US | Win10 | 2026", bot={
        "stealer": "lumma",
        "installed_ts": "2026-01-01",
        "infostealer": {"ip_address": "203.0.113.7", "country": "US",
                        "internet_service_provider": "Example ISP", "operating_system": "Windows 10"},
        "file": {"size": "12 MB"},
    }, **overrides)


def _by_type(bundle, stix_type):
    return [o for o in bundle.objects if o.type == stix_type]


def _rels(bundle, description=None):
    rels = _by_type(bundle, "relationship")
    return [r for r in rels if description is None or r.get("description") == description]


def _map(source, api_client=None, **settings_kw):
    return StixMapper(STIXMapperSettings(api_client=api_client, **settings_kw)).map(source)


def _api_client_with(marketplace=None, products=None):
    """Patch MarketplacesApi so get-by-id returns fixtures; returns (api_client, api_mock)."""
    api = MagicMock(name="MarketplacesApi")
    if marketplace is not None:
        api.return_value.get_marketplaces_marketplace_id.return_value = \
            IntegrationMarketplaceResponse.from_dict(marketplace)
    if products is not None:
        api.return_value.get_products_product_id.side_effect = \
            lambda pid: IntegrationProductResponse.from_dict(products[pid])
    return MagicMock(name="api_client"), api


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fixture, expected", [
    ("IntegrationMarketplaceResponse", "marketplace"),
    ("IntegrationProductResponse", "marketplace_product"),
    ("IntegrationResourceResponse", "marketplace_resource"),
    ("IntegrationVendorResponse", "marketplace_vendor"),
])
def test_item_dispatch_is_unambiguous(fixture, expected):
    source = _fixture(fixture)
    matched = [name for name, (condition, _) in StixMapper.mappers.items() if condition(source)]
    assert matched == [expected]


@pytest.mark.parametrize("key, fixture, expected", [
    ("marketplaces", "IntegrationMarketplaceResponse", "marketplaces"),
    ("products", "IntegrationProductResponse", "marketplace_products"),
    ("resources", "IntegrationResourceResponse", "marketplace_resources"),
    ("vendors", "IntegrationVendorResponse", "marketplace_vendors"),
])
def test_page_dispatch_is_unambiguous(key, fixture, expected):
    source = {"count": 1, "cursor_next": "x", key: [_fixture(fixture)]}
    matched = [name for name, (condition, _) in StixMapper.mappers.items() if condition(source)]
    assert matched == [expected]


# ---------------------------------------------------------------------------
# Marketplace and vendor
# ---------------------------------------------------------------------------

def test_marketplace_maps_to_channel():
    bundle = _map(_fixture("IntegrationMarketplaceResponse", alias="dummy-alias", is_active=False))
    [channel] = _by_type(bundle, "channel")
    assert channel.name == "[marketplace] - dummy"
    assert channel.channel_types == ["marketplace"]
    assert channel.aliases == ["dummy-alias"]
    assert "Tier '1'" in channel.description and "no longer active" in channel.description
    assert {r.source_name for r in channel.external_references} >= {"Verity471 Portal", "Marketplace"}


def test_vendor_without_client_links_bare_marketplace_channel():
    bundle = _map(_fixture("IntegrationVendorResponse"))
    [identity] = [i for i in _by_type(bundle, "identity") if i.identity_class == "individual"]
    [channel] = _by_type(bundle, "channel")
    assert channel.name == "[marketplace] - dummy"
    assert "rating: '4.5/5'" in identity.description.lower()
    assert "'99%' overall" in identity.description
    [rel] = _rels(bundle, "vendor")
    assert (rel.source_ref, rel.target_ref) == (identity.id, channel.id)


def test_vendor_with_client_uses_fetched_marketplace():
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"))
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map(_fixture("IntegrationVendorResponse"), api_client=api_client)
    [channel] = _by_type(bundle, "channel")
    assert "Tier '1'" in channel.description  # full marketplace, not the bare fallback


# ---------------------------------------------------------------------------
# Product
# ---------------------------------------------------------------------------

def test_product_without_client_maps_listing_and_vendor_only():
    bundle = _map(_fixture("IntegrationProductResponse"))
    [media] = _by_type(bundle, "media-content")
    assert media.url == product_url(PRODUCT_ID)
    assert media.media_category == "marketplace listing"
    assert {"verity471:marketplace_product", "verity471:product_kind_digital_good"} <= set(media.x_opencti_labels)
    assert "Price: '10 USD'" in media.x_opencti_description
    assert not _by_type(bundle, "channel")
    [rel] = _rels(bundle, "vendor")
    assert rel.target_ref == media.id


def test_product_with_client_is_published_by_marketplace_channel():
    marketplace = _fixture("IntegrationMarketplaceResponse")
    api_client, api = _api_client_with(marketplace=marketplace)
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map(_fixture("IntegrationProductResponse"), api_client=api_client)
    [channel] = _by_type(bundle, "channel")
    [media] = _by_type(bundle, "media-content")
    assert channel.id == _by_type(_map(marketplace), "channel")[0].id  # same node as the marketplace itself
    publishes = [r for r in _rels(bundle) if r.relationship_type == "publishes"]
    assert [(r.source_ref, r.target_ref) for r in publishes] == [(channel.id, media.id)]
    assert "on 'dummy'" in media.x_opencti_description


def test_bot_product_emits_infected_ip_and_stealer():
    bundle = _map(_bot_product())
    [media] = _by_type(bundle, "media-content")
    [ip] = _by_type(bundle, "ipv4-addr")
    [malware] = _by_type(bundle, "malware")
    assert ip.value == "203.0.113.7" and malware.name == "Lumma"
    assert {(r.source_ref, r.target_ref) for r in _rels(bundle, "infected machine")} == {(media.id, ip.id)}
    assert {(r.source_ref, r.target_ref) for r in _rels(bundle, "stealer")} == {(media.id, malware.id)}
    assert "Country: 'US'." in media.x_opencti_description


@pytest.mark.parametrize("value, expected", [
    ("redline", "RedLine"), ("stealc", "StealC"), ("newfamily", "Newfamily"), ("Lumma", "Lumma"),
])
def test_bot_stealer_display_name(value, expected):
    product = _bot_product()
    product["bot"]["stealer"] = value
    assert [m.name for m in _by_type(_map(product), "malware")] == [expected]


@pytest.mark.parametrize("value", ["unknown", "Unknown", " ", "n/a"])
def test_bot_placeholder_stealer_is_not_malware(value):
    product = _bot_product()
    product["bot"]["stealer"] = value
    bundle = _map(product)
    assert not _by_type(bundle, "malware")
    assert "Stealer:" not in _by_type(bundle, "media-content")[0].x_opencti_description


def test_bot_with_masked_ip_skips_observable():
    product = _bot_product()
    product["bot"]["infostealer"]["ip_address"] = "203.0.113.*"
    assert not _by_type(_map(product), "ipv4-addr")


def test_proxy_product_emits_ip_and_domain():
    product = _fixture("IntegrationProductResponse", kind="proxy", proxy={"basic_info": {
        "ip_address": "198.51.100.9", "domain": "proxy.example.net", "proxy_type": "SOCKS5"}})
    bundle = _map(product)
    assert [o.value for o in _by_type(bundle, "ipv4-addr")] == ["198.51.100.9"]
    assert [o.value for o in _by_type(bundle, "domain-name")] == ["proxy.example.net"]
    assert len(_rels(bundle, "proxy")) == 2


@pytest.mark.parametrize("value, emitted", [
    ("198.51.100.9:1080", "198.51.100.9"), ("198.51.*.*", None), ("198.51.100.xxx", None),
])
def test_proxy_ip_with_port_or_mask(value, emitted):
    product = _fixture("IntegrationProductResponse", kind="proxy", proxy={"basic_info": {"ip_address": value}})
    bundle = _map(product)
    assert [o.value for o in _by_type(bundle, "ipv4-addr")] == ([emitted] if emitted else [])
    assert f"IP: '{value}'" in _by_type(bundle, "media-content")[0].x_opencti_description.replace("[.]", ".")


def test_card_product_describes_card_without_personal_data():
    product = _fixture("IntegrationProductResponse", kind="card", card={
        "cc": {"bin": "411111", "payment_system": "VISA", "number": "4111111111111111"},
        "available_info": {"cvv_available": True, "date_of_birth_available": True},
        "victim": {"holder": "Jane Victim", "email_address": "jane@victim.example",
                   "phone_number": "+1 555 0100", "address": "1 Victim Street"},
    })
    bundle = _map(product)
    [media] = _by_type(bundle, "media-content")
    assert "BIN: '411111'." in media.x_opencti_description
    assert "Includes: CVV, date of birth." in media.x_opencti_description
    serialized = bundle.serialize()
    for secret in ("4111111111111111", "Jane Victim", "jane@victim", "555 0100", "Victim Street"):
        assert secret not in serialized


def test_full_card_numbers_in_listing_text_are_truncated():
    product = _fixture("IntegrationProductResponse", kind="card", title="4111 1111 1111 1111 | fresh",
                       description="<p>Card 5555555555554444, truncated 545212XXXXXX1234</p>")
    bundle = _map(product)
    [media] = _by_type(bundle, "media-content")
    assert media.title == "411111XXXXXX1111 | fresh"
    assert "555555XXXXXX4444" in media.content and "545212XXXXXX1234" in media.content
    serialized = bundle.serialize()
    assert "4111 1111 1111 1111" not in serialized and "5555555555554444" not in serialized


# ---------------------------------------------------------------------------
# Resource
# ---------------------------------------------------------------------------

def test_resource_without_client_emits_target_site_only():
    bundle = _map(_fixture("IntegrationResourceResponse"))
    [domain] = _by_type(bundle, "domain-name")
    [url] = _by_type(bundle, "url")
    assert domain.value == "example.com" and url.value == "https://example.com/login"
    assert {"verity471:marketplace_resource", "verity471:includes_login",
            "verity471:includes_password"} <= set(domain.x_opencti_labels)
    assert "verity471:includes_cookies" not in domain.x_opencti_labels
    assert not _rels(bundle)  # nothing to link to without the bot


def test_resource_with_client_links_to_fetched_bot_listing():
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"),
                                       products={PRODUCT_ID: _bot_product()})
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map(_fixture("IntegrationResourceResponse"), api_client=api_client)
    [media] = _by_type(bundle, "media-content")
    assert media.url == product_url(PRODUCT_ID)
    stolen = _rels(bundle, "stolen data")
    assert {r.target_ref for r in stolen} == {media.id} and len(stolen) == 2  # domain + url
    assert _by_type(bundle, "ipv4-addr") and _by_type(bundle, "malware") and _by_type(bundle, "channel")


def test_resource_with_service_name_takes_domain_from_link():
    bundle = _map(_fixture("IntegrationResourceResponse", name="Google",
                           link="https://accounts.google.com/signin"))
    assert [d.value for d in _by_type(bundle, "domain-name")] == ["accounts.google.com"]


def test_resource_without_site_observable_still_maps_bot_context():
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"),
                                       products={PRODUCT_ID: _bot_product()})
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map(_fixture("IntegrationResourceResponse", name="Google", link="Google"),
                      api_client=api_client)
    assert not _by_type(bundle, "domain-name") and not _by_type(bundle, "url")
    assert _by_type(bundle, "media-content") and _by_type(bundle, "malware")


def test_resource_without_site_or_client_raises_empty_bundle():
    with pytest.raises(EmptyBundle):
        _map(_fixture("IntegrationResourceResponse", name="Google", link="Google"))


def test_marketplace_description_is_defanged():
    bundle = _map(_fixture("IntegrationMarketplaceResponse",
                           description="Mirror: http://shopabc.onion and https://shop.example.com"))
    [channel] = _by_type(bundle, "channel")
    assert "hxxp://shopabc[.]onion" in channel.description
    assert "hxxps://shop[.]example[.]com" in channel.description


# ---------------------------------------------------------------------------
# Parent lookups
# ---------------------------------------------------------------------------

def test_marketplace_is_fetched_once_per_page():
    products = [_fixture("IntegrationProductResponse", id=f"marketplace-product--{i}") for i in range(3)]
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"))
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map({"count": 3, "cursor_next": None, "products": products}, api_client=api_client)
    assert api.return_value.get_marketplaces_marketplace_id.call_count == 1
    assert len(_by_type(bundle, "media-content")) == 3 and len(_by_type(bundle, "channel")) == 1


def test_failed_parent_fetch_is_cached_and_does_not_break_mapping(caplog):
    api = MagicMock(name="MarketplacesApi")
    api.return_value.get_marketplaces_marketplace_id.side_effect = RuntimeError("boom")
    products = [_fixture("IntegrationProductResponse", id=f"marketplace-product--{i}") for i in range(2)]
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map({"count": 2, "cursor_next": None, "products": products}, api_client=MagicMock())
    assert api.return_value.get_marketplaces_marketplace_id.call_count == 1
    assert len(_by_type(bundle, "media-content")) == 2 and not _by_type(bundle, "channel")
    assert "Could not fetch marketplaces:marketplace" in caplog.text


def test_page_skips_broken_item(caplog):
    good = _fixture("IntegrationProductResponse")
    broken = _fixture("IntegrationProductResponse", id=f"marketplace-product--broken", price="not-a-list")
    bundle = _map({"count": 2, "cursor_next": None, "products": [broken, good]})
    assert len(_by_type(bundle, "media-content")) == 1
    assert "Failed to map marketplace item marketplace-product--broken" in caplog.text


def test_empty_page_raises_empty_bundle():
    with pytest.raises(EmptyBundle):
        _map({"count": 0, "cursor_next": None, "products": []})


# ---------------------------------------------------------------------------
# Alerts integration
# ---------------------------------------------------------------------------

def _alert(source_id, minute=0):
    return SimpleNamespace(
        source_id=source_id,
        creation_ts=datetime.datetime(2026, 11, 1, 0, minute, tzinfo=datetime.timezone.utc),
        links=SimpleNamespace(verity_portal=SimpleNamespace(href="https://portal.example/x"),
                              verity_api=SimpleNamespace(href="https://api.example/x")),
    )


def _map_alerts(targets, api_client):
    source = read_fixture(f"{API}/AlertsStreamResponse.json")
    with patch("verity471.verity_stix.mappers.alerts.fetch_alert_targets", return_value=targets):
        return StixMapper(STIXMapperSettings(api_client=api_client, report_full_content=False)).map(source)


def test_resource_alert_incident_links_site_and_bot_context():
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"),
                                       products={PRODUCT_ID: _bot_product()})
    target = IntegrationResourceResponse.from_dict(_fixture("IntegrationResourceResponse"))
    at = AlertTarget(alert=_alert(target.id), target=target)
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map_alerts([at], api_client)
    [incident] = _by_type(bundle, "incident")
    linked = {r.target_ref for r in _rels(bundle) if r.source_ref == incident.id}
    for stix_type in ("domain-name", "url", "media-content", "ipv4-addr", "malware"):
        assert {o.id for o in _by_type(bundle, stix_type)} <= linked, stix_type


def test_product_alerts_share_one_marketplace_fetch():
    api_client, api = _api_client_with(marketplace=_fixture("IntegrationMarketplaceResponse"))
    targets = []
    for i in range(3):
        product = IntegrationProductResponse.from_dict(
            _fixture("IntegrationProductResponse", id=f"marketplace-product--{i}"))
        targets.append(AlertTarget(alert=_alert(product.id, minute=i), target=product))
    with patch("verity471.api.marketplaces_api.MarketplacesApi", api):
        bundle = _map_alerts(targets, api_client)
    assert api.return_value.get_marketplaces_marketplace_id.call_count == 1
    assert len(_by_type(bundle, "incident")) == 3
