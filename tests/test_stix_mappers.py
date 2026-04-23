import json

import pytest

from verity471.verity_stix import STIXMapperSettings
from verity471.verity_stix.exceptions import StixMapperNotFound
from verity471.verity_stix.mappers import ReportMapper
from verity471.verity_stix.mappers.common import StixMapper
from verity471.verity_stix.mappers.entities import EntitiesMapper
from verity471.verity_stix.mappers.indicators import IndicatorsMapper
from verity471.verity_stix.mappers.reports import ReportType

from .conftest import PREFIX, read_fixture
from unittest.mock import MagicMock



def strip_random_values(bundle: dict) -> dict:
    bundle["id"] = None
    for i1, o in enumerate(bundle["objects"]):
        bundle["objects"][i1]["created"] = None
        bundle["objects"][i1]["modified"] = None
    return bundle


@pytest.mark.parametrize(
    "in_fixture, out_fixture",
    [
        pytest.param("indicators_ipv4_input.json", "indicators_ipv4_stix.json", id="indicators-ipv4"),
        pytest.param("indicators_file_input.json", "indicators_file_stix.json", id="indicators-file"),
        pytest.param("indicators_url_input.json", "indicators_url_stix.json", id="indicators-url"),
        pytest.param("indicators_yara_input.json", "indicators_yara_stix.json", id="indicators-yara"),
        pytest.param("indicators_domain_input.json", "indicators_domain_stix.json", id="indicators-domain"),
        pytest.param("indicators_email_input.json", "indicators_email_stix.json", id="indicators-email"),
        pytest.param("indicators_bph_input.json", "indicators_bph_stix.json", id="indicators-bph"),
        pytest.param("cves_input.json", "cves_stix.json", id="cves"),
        pytest.param("report_breach_alert_input.json", "report_breach_alert_stix.json", id="report_breach_alert"),
        pytest.param("report_fintel_input.json", "report_fintel_stix.json", id="report_fintel"),
        pytest.param("report_inforep_input.json", "report_inforep_stix.json", id="report_inforep"),
        pytest.param("report_spot_input.json", "report_spot_stix.json", id="report_spot"),
        pytest.param("report_malware_input.json", "report_malware_stix.json", id="report_malware"),
        pytest.param("report_geopol_input.json", "report_geopol_stix.json", id="report_geopol"),
    ]
)
@pytest.mark.parametrize(
    "by_id", [
        pytest.param(True, id="by-id"),
        pytest.param(False, id="stream"),
    ]
)
def test_stix_mappers(in_fixture, out_fixture, by_id):
    api_response = read_fixture(f'{PREFIX}/fixtures/{in_fixture}')
    if by_id:
        for value in api_response.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                api_response = value[0]
    expected_result = read_fixture(f'{PREFIX}/fixtures/{out_fixture}')

    mapper = StixMapper(STIXMapperSettings(
        client=MagicMock(name="client"), api_client=MagicMock(name="api_client"), report_full_content=False
    ))
    result = mapper.map(api_response)
    actual = json.loads(result.serialize())

    actual_norm = strip_random_values(actual)
    expected_norm = strip_random_values(expected_result)
    assert expected_norm == actual_norm


fragment_truncated = {"is_truncated": True}
fragment_attachments = {"attachments": [{"mime_type" : "image/png", "url" : "https://api.intel471.cloud/intel-report/v1/reports/.../attachments/4b76f7665f5331a91531a1ae0dd27e9755b1eef41288ab3f3feec0c6fd7bfbae"}]}


@pytest.mark.parametrize(
    "report_full_content, stream_response_fragment, should_fetch",
    [
        pytest.param(True, fragment_truncated, True, id="truncated-1"),
        pytest.param(False, fragment_truncated, False, id="truncated-2"),
        pytest.param(True, {}, False, id="truncated-3"),
        pytest.param(True, fragment_attachments, True, id="attachments-1"),
        pytest.param(False, fragment_attachments, False, id="attachments-2"),
    ]
)
def test_report_mapper_fetches_full_report_on_demand(report_full_content, stream_response_fragment, should_fetch):
    api_cls = "ReportsApi"
    by_id_method_name = "get_reports_fintel_id"
    by_id_api_response = {
        "type": "fintel",
        "title": "BYID",
        "creation_ts": "2025-07-16T13:28:28Z",
        "id": "report--fc000675-a3ec-49b8-92a0-a0247f5e969e"
        }

    by_id_api_response_mock = MagicMock(name="By ID API response")
    by_id_api_response_mock.to_dict.return_value = by_id_api_response
    api_instance_mock = MagicMock(name="API instance")
    getattr(api_instance_mock, by_id_method_name).return_value = by_id_api_response_mock
    mock_api_client = MagicMock(name="mock_api_client")
    mock_verity471 = MagicMock(name="verity471")
    getattr(mock_verity471, api_cls).return_value = api_instance_mock

    mapper = ReportMapper(STIXMapperSettings(mock_verity471, mock_api_client, report_full_content=report_full_content))
    stream_api_response_report = {
        "type": "fintel",
        "title": "STREAM",
        "creation_ts": "2025-07-16T13:28:28Z",
        "id": "report--fc000675-a3ec-49b8-92a0-a0247f5e969e",
    }
    stream_api_response_report.update(stream_response_fragment)
    stream_api_response = {"count": "1", "reports": [stream_api_response_report]}
    bundle = mapper.map(stream_api_response)
    report = bundle.objects[-1]
    expected_name = "BYID" if should_fetch else "STREAM"
    assert report.name == expected_name


@pytest.mark.parametrize("source,expected_values", (
        # /iocs endpoint
        ({"type": "MaliciousURL", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "URL", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "MaliciousDomain", "value": "acme.com"}, {"type": "domain-name", "value": "acme.com"}),
        ({"type": "IPAddress", "value": "10.0.0.1"}, {"type": "ipv4-addr", "value": "10.0.0.1"}),
        ({"type": "IPv4Prefix", "value": "10.0.0.1/24"}, {"type": "ipv4-addr", "value": "10.0.0.1/24"}),
        ({"type": "IPv6Prefix", "value": "2a09:7c44::/32"}, {"type": "ipv6-addr", "value": "2a09:7c44::/32"}),
        ({"type": "AutonomousSystem", "value": "AS123456"}, {"type": "autonomous-system", "number": 123456}),
        ({"type": "MD5", "value": "acb9cf2560602aa023e9933b959974d1"}, {"type": "file", "hashes": {"MD5": "acb9cf2560602aa023e9933b959974d1"}}),
        ({"type": "SHA1", "value": "ae9de44e5f23758ffb6f4fa28065c6122c2e4467"}, {"type": "file", "hashes": {"SHA-1": "ae9de44e5f23758ffb6f4fa28065c6122c2e4467"}}),
        ({"type": "SHA256", "value": "890a0bfab48d0b93da8f7617b2e65621e8d7f8c93a854fa8596232d9bcb1b39e"}, {"type": "file", "hashes": {"SHA-256": "890a0bfab48d0b93da8f7617b2e65621e8d7f8c93a854fa8596232d9bcb1b39e"}}),
        ({"type": "FileName", "value": "acmecorp.exe"}, {"type": "file", "name": "acmecorp.exe"}),
        # /entities endpoint
        ({"type": "ActorDomain", "value": "acme.com"}, {"type": "domain-name", "value": "acme.com"}),
        ({"type": "Handle", "value": "acme"}, {"type": "threat-actor", "name": "acme"}),
        ({"type": "ActorOtherWebsite", "value": "https://acme.com"}, {"type": "url", "value": "https://acme.com"}),
        ({"type": "BitcoinAddress", "value": "1HUu6K9sFvN1cGV"}, {"type": "cryptocurrency-wallet", "value": "1HUu6K9sFvN1cGV"}),
        ({"type": "OtherCryptoCurrencies", "value": "1HUu6K9sFvN1cGV"}, {"type": "cryptocurrency-wallet", "value": "1HUu6K9sFvN1cGV"}),
        ({"type": "EmailAddress", "value": "changeme@acme.com"}, {"type": "email-addr", "value": "changeme@acme.com"}),
        ({"type": "AIM", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "AIM"}),
        ({"type": "Discord", "value": "https://discord.gg/2xx2xx2"}, {"type": "user-account", "user_id": "2xx2xx2", "account_type": "Discord"}),
        ({"type": "Facebook", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Facebook"}),
        ({"type": "GitHub", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "GitHub"}),
        ({"type": "ICQ", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "ICQ"}),
        ({"type": "Instagram", "value": "instagram.com/changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Instagram"}),
        ({"type": "Jabber", "value": "changeme@jabber.de"}, {"type": "user-account", "user_id": "changeme@jabber.de", "account_type": "Jabber"}),
        ({"type": "LinkedIn", "value": "https://www.linkedin.com/in/iamweasel-58312b1a6/"}, {"type": "user-account", "user_id": "iamweasel-58312b1a6", "account_type": "LinkedIn"}),
        ({"type": "MSN", "value": "changeme@acme.com"}, {"type": "user-account", "user_id": "changeme@acme.com", "account_type": "MSN"}),
        ({"type": "MoiMir", "value": "my.mail.ru/mail/changeme/"}, {"type": "user-account", "user_id": "changeme", "account_type": "MoiMir"}),
        ({"type": "Odnoklassniki", "value": "ok.ru/profile/11111800259"}, {"type": "user-account", "user_id": "11111800259", "account_type": "Odnoklassniki"}),
        ({"type": "QQ", "value": "111159547"}, {"type": "user-account", "user_id": "111159547", "account_type": "QQ"}),
        ({"type": "Skype", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Skype"}),
        ({"type": "Telegram", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Telegram"}),
        ({"type": "TOX", "value": "2B41B398739E6BECE4E93EAFA0C665"}, {"type": "user-account", "user_id": "2B41B398739E6BECE4E93EAFA0C665", "account_type": "TOX"}),
        ({"type": "Twitter", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Twitter"}),
        ({"type": "VK", "value": "vk.com/changeme_2"}, {"type": "user-account", "user_id": "changeme_2", "account_type": "VK"}),
        ({"type": "WeChat", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "WeChat"}),
        ({"type": "Wickr", "value": "changeme"}, {"type": "user-account", "user_id": "changeme", "account_type": "Wickr"}),
        ({"type": "YahooIM", "value": "changeme@yahoo.com"}, {"type": "user-account", "user_id": "changeme@yahoo.com", "account_type": "YahooIM"}),
        ({"type": "PerfectMoneyID", "value": "U1111111"}, {"type": "user-account", "user_id": "U1111111", "account_type": "PerfectMoneyID"}),
        ({"type": "QiwiWallet", "value": "11110519386"}, {"type": "user-account", "user_id": "11110519386", "account_type": "QiwiWallet"}),
        ({"type": "WebMoneyID", "value": "111112935229"}, {"type": "user-account", "user_id": "111112935229", "account_type": "WebMoneyID"}),
        ({"type": "WebMoneyPurse", "value": "Z111144083730"}, {"type": "user-account", "user_id": "Z111144083730", "account_type": "WebMoneyPurse"}),
        ({"type": "YandexMoney", "value": "111113131482342"}, {"type": "user-account", "user_id": "111113131482342", "account_type": "YandexMoney"}),
        ({"type": "X", "value": "@FooB"}, {"type": "user-account", "user_id": "@FooB", "account_type": "X"}),
        ({"type": "X", "value": "https://x.com/foob"}, {"type": "user-account", "user_id": "foob", "account_type": "X"}),
        ({"type": "Signal", "value": "foo.11"}, {"type": "user-account", "user_id": "foo.11", "account_type": "Signal"}),
        ({"type": "Phone", "value": "79874172111"}, {"type": "user-account", "user_id": "79874172111", "account_type": "Phone"}),
        ({"type": "CveID", "value": "CVE-2024-23113"}, {"type": "vulnerability", "name": "CVE-2024-23113"}),
        # Invalid stuff
        ({"type": "Handle", "value": "a"}, None),
        ({"type": "MD5", "value": "invalidMd5"}, None),
        ({"type": "MaliciousDomain", "value": "https://invalid.domain"}, None)
))
def test_observable_mapper(source, expected_values):
    mapper = EntitiesMapper()
    sco = mapper.map(**source)
    if expected_values is None:
        assert sco is expected_values
    else:
        for key, value in expected_values.items():
            assert getattr(sco, key) == value


@pytest.mark.parametrize("report_type,source,expected_values", (
    (ReportType.FINTEL, {"id": "ab1", "type": "fintel", "sources": [
        {"type": "external", "title": "ACME corp news", "links": {"external": {"href": "https://acme.corp/123"}}, "index": "1"}]},
     {"source_name": "ACME corp news", "url": "https://acme.corp/123"}),
    (ReportType.FINTEL, {"id": "ab1", "type": "fintel", "sources": [
        {"type": "external", "source_type": "External Link", "title": "Titan Information Report",
         "links": {"external": {"href": "https://titan.intel471.com/report/inforep/487a8"}}, "index": "1"}]},
     {"source_name": "External Link/Titan Information Report",
      "url": "https://titan.intel471.com/report/inforep/487a8"}),
    (ReportType.INFOREP, {"id": "ab1", "type": "info_report", "sources": [
        {"type": "external", "source_type": "Forum Post", "title": "[SOURCE CODE] HexSec | Android RAT",
         "links": {"external": {"href": "https://titan.intel471.com/post_thread/9cacd56"}}, "index": "1"}]},
     {"source_name": "Forum Post/[SOURCE CODE] HexSec | Android RAT",
      "url": "https://titan.intel471.com/post_thread/9cacd56"}),
    (ReportType.INFOREP, {"id": "ab1", "type": "info_report", "sources": [
        {"type": "external", "source_type": "Forum Post", "title": "[SOURCE CODE] HexSec | Android RAT",
         "links": {"external": {"href": "https://titan.intel471.com/post_thread/9cacd56"}}, "index": "1"}]},
     {"source_name": "Forum Post/[SOURCE CODE] HexSec | Android RAT",
      "url": "https://titan.intel471.com/post_thread/9cacd56"}),
    (ReportType.BREACH_ALERT, {"id": "ab1", "type": "breach_alert", "sources": [
        {"type": "internal", "source_type": "Forum Thread", "title": "acmesystems",
         "links": {"verity_portal": {"href": "https://titan.intel471.com/post_thread/2984"}}, "index": "1"}]},
     {"source_name": "[Verity471 Portal/Forum Thread] acmesystems",
      "url": "https://titan.intel471.com/post_thread/2984"}),
    (ReportType.SPOTREP, {"id": "ab1", "type": "spot_report", "sources": [
        {"type": "internal", "title": "Forum thread",
         "links": {"verity_portal": {"href": "https://titan.intel471.com/post_thread/2984"}}, "index": "1"}]},
     {"source_name": "[Verity471 Portal] Forum thread",
      "url": "https://titan.intel471.com/post_thread/2984"}),
))
def test_map_reports_external_references(report_type, source, expected_values):
    mapper = ReportMapper(STIXMapperSettings())
    external_refs = mapper._get_external_references(source)
    external_ref_0 = json.loads(external_refs[0].serialize())
    report_settings = ReportMapper.reports_settings.get(report_type)
    assert external_ref_0 == {"source_name": "Verity471 Portal", "url": f"https://verity.intel471.com/{report_settings.portal_url_fragment}/ab1"}
    if expected_values:
        external_ref_1 = json.loads(external_refs[1].serialize())
        assert external_ref_1 == expected_values


@pytest.mark.parametrize("report_type,source", (
    (ReportType.FINTEL.value, {"id": "ab1", "type": "fintel", "entities": [{"type": "MalwareFamily", "value": "acme"}]}),
    (ReportType.FINTEL.value, {"id": "ab1", "type": "info_report", "entities": [{"type": "MalwareFamily", "value": "acme"}]}),
    (ReportType.BREACH_ALERT.value, {"id": "ab1", "type": "breach_alert", "entities": [{"type": "MalwareFamily", "value": "acme"}]}),
    (ReportType.SPOTREP.value, {"id": "ab1", "type": "spot_report", "entities": [{"type": "MalwareFamily", "value": "acme"}]}),
    (ReportType.MALWARE.value, {"id": "ab1", "type": "malware_report", "entities": [], "threat": {"id": "ac1", "type": "malware", "family": "acme"}}),
))
def test_map_reports_entities(report_type, source):
    mapper = ReportMapper(STIXMapperSettings())
    entities = mapper._get_entities(source)
    entity = json.loads(list(entities.get())[0].serialize())
    assert entity["type"] == "malware"
    assert entity["name"] == "acme"
    malware_families_names = mapper._get_malware_families_names(entities)
    assert malware_families_names == ["acme"]


@pytest.mark.parametrize("report_type,source", (
    (ReportType.FINTEL.value, {"id": "ab1", "type": "fintel", "victims": [
        {"name": "ACME corp", "links": [{"external": {"href": "https://acme.corp"}}]}]}),
    (ReportType.INFOREP.value, {"id": "ab1", "type": "info_report", "victims": [
        {"name": "ACME corp", "links": [{"external": {"href": "https://acme.corp"}}]}]}),
    (ReportType.BREACH_ALERT.value, {"id": "ab1", "type": "breach_alert", "victims": [{
            "country": "United States",
            "industries": [
                {
                    "industry": "Financial and investment consulting industry",
                    "sector": "Professional services and consulting sector"
                }
            ],
            "name": "ACME corp",
            "region": "North America",
            "revenue": "US $100 million",
            "links": [{
                "external": {
                    "href": "https://acme.corp"
                }
            }]
        }]}),
    (ReportType.SPOTREP.value, {"id": "ab1", "type": "spot_report", "victims": [
        {"name": "ACME corp", "links": [{"external": {"href": "https://acme.corp"}}]}]}),
))
def test_map_reports_victims(report_type, source):
    mapper = ReportMapper(STIXMapperSettings())
    victims = list(mapper._get_victims(source).get())
    assert victims[0].type == "identity"
    assert victims[0].identity_class == "organization"
    assert victims[0].name == "ACME corp"
    assert victims[0].contact_information == "https://acme.corp"


def test_indicator_pattern_url_quote():
    mapper = IndicatorsMapper(STIXMapperSettings())
    result = mapper.map({"count": "1", "indicators": [{
        "activity": {"first_seen_ts": "2018-08-07T18:33:00Z", "last_seen_ts": "2018-08-07T18:33:00Z"},
        "data": {
            "url": "https://foo.bar.com/pixel.png'ogi,TO"
            },
        "pattern": "[url:value = 'https://foo.bar.com/pixel.png'ogi,TO']",
        "pattern_type": "stix",
        "pattern_version": "2.1",
        "type": "url",
        "threat": {"data": {"malware_family": {"name": "foo"}}},
        "expiration_ts": "2023-01-26T01:03:54Z",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mitre-attack",
                "phase_name": "command_and_control"
            }
        ],
        "confidence": 50,
        "description": "foo",
        "classification": {
            "girs": [
                {
                    "name": "Banking trojan malware",
                    "path": "1.1.4"
                }
            ]
        }
    }]})
    assert result is None


def test_reports_stream_not_mappable():
    """
    Only allow STIX mappings on type-specific endpoints, such as /reports/fintel/stream, etc.
    as /reports/stream's data is too limited.
    """
    mapper = StixMapper(STIXMapperSettings())
    with pytest.raises(StixMapperNotFound):
        mapper.map(
            {
                "count": 1740,
                "info_report_count": 0,
                "fintel_report_count": 1740,
                "breach_alert_count": 0,
                "spot_report_count": 0,
                "malware_report_count": 0,
                "vulnerability_report_count": 0,
                "geopol_report_count": 0,
                "cursor_next": "MjhiMWQ2ZGItMzJkNi00NDFkLWMyOTItOTk0YjI0YmRkMjE3OjE3NjI5NDAwNTI3MTA6cmVwb3J0LS1lNzFkMzg3Zi0zMjVlLTViZmMtYTQzZC0xNDM4NzZjNmNmYzA",
                "reports": [
                    {
                        "id": "report--e71d387f-325e-5bfc-a43d-143876c6cfc0",
                        "type": "fintel",
                        "sub_type": "actor_profile",
                        "title": "Foo",
                    }
                ]
            }
        )


def test_map_invalid_indicator():
    mapper = IndicatorsMapper(STIXMapperSettings())
    result = mapper.map({
        "id": "abc",
        "type": "domain",
        "data": {"domain": "http://foobar.com"},
        "confidence": 50,
        "pattern": "[domain-name:value = 'http://foobar.com']",
        "pattern_type": "stix",
        "pattern_version": "2.1",
        "threat": {"data": {"malware_family": {"name": "Foo"}}},
        "activity": {"first_seen_ts": "2026-01-23T15:24:54.356273Z"}
    })
    print(result.serialize())