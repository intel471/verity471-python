"""Tests for the alert-target STIX mappers (posts, credentials, malware events,
malware families, data-leak-site posts) and the alerts orchestrator."""
import datetime
import json
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from verity471.helpers.alerts import AlertTarget
from verity471.models.get_cred_response import GetCredResponse
from verity471.models.get_cred_set_response import GetCredSetResponse
from verity471.models.post_details1 import PostDetails1
from verity471.verity_stix import STIXMapperSettings
from verity471.verity_stix.exceptions import StixMapperNotFound
from verity471.verity_stix.mappers.common import StixMapper
import verity471.verity_stix.mappers  # noqa: F401 - ensure all mappers register

from .conftest import PREFIX, read_fixture

API = f"{PREFIX}/fixtures/api_responses"


def _api_fixture(name):
    return read_fixture(f"{API}/{name}.json")


def _settings(**kw):
    kw.setdefault("client", MagicMock(name="client"))
    kw.setdefault("api_client", MagicMock(name="api_client"))
    kw.setdefault("report_full_content", False)
    return STIXMapperSettings(**kw)


def _by_type(bundle, stix_type):
    return [o for o in bundle.objects if o.type == stix_type]


# ---------------------------------------------------------------------------
# Registry dispatch: every alert-target fixture matches exactly one condition.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fixture, expected_mapper", [
    ("PostDetails1", "forum_post"),
    ("PrivateMessageDetails1", "forum_private_message"),
    ("ChatRoomMessageStream", "chat_message"),
    ("GetCredResponse", "credential"),
    ("GetCredOccurrenceResponse", "credential_occurrence"),
    ("GetCredSetResponse", "credential_set"),
    ("IntegrationsEvent", "malware_event"),
    ("SimplifiedMalwareProfile", "malware_family"),
])
def test_dispatch_is_unambiguous(fixture, expected_mapper):
    source = _api_fixture(fixture)
    matched = [name for name, (condition, _) in StixMapper.mappers.items() if condition(source)]
    assert matched == [expected_mapper], f"{fixture} matched {matched}"


def test_dls_post_item_dispatches_to_data_leak_site():
    source = _api_fixture("DataLeakSitePostsStreamingPage")["posts"][0]
    matched = [name for name, (condition, _) in StixMapper.mappers.items() if condition(source)]
    assert matched == ["data_leak_site_post"]


# ---------------------------------------------------------------------------
# Forum post / PM / chat -> Channel + Media-Content + publishes.
# ---------------------------------------------------------------------------

# PostDetails1 -> forum + sub-forum + thread; ChatRoomMessageStream -> server + room; PM -> forum only.
@pytest.mark.parametrize("fixture, expected_channels", [
    ("PostDetails1", 3),
    ("PrivateMessageDetails1", 1),
    ("ChatRoomMessageStream", 2),
])
def test_posts_emit_channel_hierarchy_and_publishes(fixture, expected_channels):
    bundle = StixMapper(_settings()).map(_api_fixture(fixture))
    channels = _by_type(bundle, "channel")
    media = _by_type(bundle, "media-content")
    assert len(media) == 1
    assert len(channels) == expected_channels
    # exactly one publishes, from a channel to the media-content (the innermost venue)
    publishes = [r for r in _by_type(bundle, "relationship")
                 if r.relationship_type == "publishes" and r.target_ref == media[0].id]
    assert len(publishes) == 1
    assert publishes[0].source_ref in {c.id for c in channels}
    # inner channels link to outer via related-to (one fewer than the channel count)
    channel_ids = {c.id for c in channels}
    chan_links = [r for r in _by_type(bundle, "relationship")
                  if r.relationship_type == "related-to"
                  and r.source_ref in channel_ids and r.target_ref in channel_ids]
    assert len(chan_links) == expected_channels - 1
    # author handle -> individual identity (not a persona / threat-actor)
    individuals = [i for i in _by_type(bundle, "identity") if i.identity_class == "individual"]
    assert individuals and individuals[0].name == "dummy"
    assert "persona" not in {o.type for o in bundle.objects}


def test_private_message_distinguishes_sender_and_recipient():
    src = _api_fixture("PrivateMessageDetails1")
    src["author"]["user_name"] = "alice"
    src["recipient"]["user_name"] = "bob"
    bundle = StixMapper(_settings()).map(src)
    media = _by_type(bundle, "media-content")[0]
    ident = {i.id: i.name for i in _by_type(bundle, "identity") if i.identity_class == "individual"}
    # the actor->post edges carry the role in their description
    roles = {ident.get(r.source_ref): r.description
             for r in _by_type(bundle, "relationship")
             if r.relationship_type == "related-to" and r.target_ref == media.id
             and r.source_ref in ident}
    assert roles == {"alice": "sender", "bob": "recipient"}


def test_chat_channels_use_server_type():
    bundle = StixMapper(_settings()).map(_api_fixture("ChatRoomMessageStream"))
    assert all(c.channel_types == ["discord"] for c in _by_type(bundle, "channel"))


def _forum_post(forum_title=None, forum_id=None, thread_id=None, post_id=None):
    src = _api_fixture("PostDetails1")
    if forum_title is not None:
        src["forum"]["title"] = forum_title
    if forum_id is not None:
        src["forum"]["id"] = forum_id
    if thread_id is not None:
        src["thread"]["id"] = thread_id
    if post_id is not None:
        src["post"]["id"] = post_id
    return src


def _channels(src):
    return _by_type(StixMapper(_settings()).map(src), "channel")


def test_same_forum_shares_forum_channel_across_posts():
    a = _channels(_forum_post(forum_title="XSS.is", thread_id="thread--a", post_id="post--1"))
    b = _channels(_forum_post(forum_title="XSS.is", thread_id="thread--b", post_id="post--2"))
    forum_a = next(c for c in a if c.channel_types == ["forum"])
    forum_b = next(c for c in b if c.channel_types == ["forum"])
    thread_a = next(c for c in a if c.channel_types == ["forum-thread"])
    thread_b = next(c for c in b if c.channel_types == ["forum-thread"])
    assert forum_a.id == forum_b.id          # same forum -> shared forum channel
    assert thread_a.id != thread_b.id        # different threads -> distinct thread channels


def test_forum_post_channel_hierarchy_is_forum_subforum_thread():
    bundle = StixMapper(_settings()).map(_api_fixture("PostDetails1"))
    types = {t for c in _by_type(bundle, "channel") for t in c.channel_types}
    assert types == {"forum", "forum-subforum", "forum-thread"}
    by_type = {c.channel_types[0]: c for c in _by_type(bundle, "channel")}
    rels = [(r.source_ref, r.target_ref) for r in _by_type(bundle, "relationship")
            if r.relationship_type == "related-to"]
    # thread --related-to--> sub-forum --related-to--> forum
    assert (by_type["forum-thread"].id, by_type["forum-subforum"].id) in rels
    assert (by_type["forum-subforum"].id, by_type["forum"].id) in rels


def test_titleless_forums_do_not_false_merge():
    # No forum title -> name falls back to the (distinct) forum id, not "Unknown forum".
    a = _channels(_forum_post(forum_title="", forum_id="forum--aaaa"))
    b = _channels(_forum_post(forum_title="", forum_id="forum--bbbb"))
    forum_a = next(c for c in a if c.channel_types == ["forum"])
    forum_b = next(c for c in b if c.channel_types == ["forum"])
    assert forum_a.id != forum_b.id
    assert "Unknown" not in forum_a.name and "Unknown" not in forum_b.name


# ---------------------------------------------------------------------------
# Credentials -> UserAccount(+credential) + email(belongs_to_ref) + domain.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fixture", ["GetCredResponse", "GetCredOccurrenceResponse"])
def test_credential_emits_user_account_and_linked_email(fixture):
    bundle = StixMapper(_settings()).map(_api_fixture(fixture))
    accounts = _by_type(bundle, "user-account")
    emails = _by_type(bundle, "email-addr")
    assert len(accounts) == 1 and len(emails) == 1
    assert accounts[0].account_login == "user@example.com"
    assert emails[0].belongs_to_ref == accounts[0].id
    assert "credential" not in {o.type for o in bundle.objects}  # no CustomObservableCredential


def test_credential_description_carries_strength_and_no_score():
    source = _api_fixture("GetCredResponse")
    source["data"]["password"]["strength"] = "strong"
    bundle = StixMapper(_settings()).map(source)
    account = json.loads(_by_type(bundle, "user-account")[0].serialize())
    # password strength lives in the description, NOT in the threat-score field
    assert "x_opencti_score" not in account
    # every data-derived token is single-quoted AND defanged (email -> user@example[.]com)
    assert account["x_opencti_description"].startswith("Credential for 'user@example[.]com'")
    assert "credential set 'dummy'" in account["x_opencti_description"]
    assert "Password strength: 'strong'." in account["x_opencti_description"]
    assert "verity471:credential" in account["x_opencti_labels"]


def test_forum_post_has_description_and_source_url():
    source = _api_fixture("PostDetails1")
    source["forum"]["title"] = "XSS.is"
    source["forum"]["description"] = "Russian-speaking forum"
    # most-specific external href (the thread's) wins as the post's source URL
    source["thread"]["links"] = {"external": {"href": "https://xss.is/thread/1"}}
    bundle = StixMapper(_settings()).map(source)
    media = json.loads(_by_type(bundle, "media-content")[0].serialize())
    # domains defanged in the description; type label present
    assert media["x_opencti_description"] == "Raw forum post from 'XSS[.]is'. 'Russian-speaking forum'"
    assert "verity471:raw_forum_post" in media["x_opencti_labels"]
    # source (external) href becomes a URL observable linked to the post
    urls = [u for u in _by_type(bundle, "url") if u.value == "https://xss.is/thread/1"]
    assert len(urls) == 1
    src_rel = [r for r in _by_type(bundle, "relationship")
               if r.relationship_type == "related-to" and r.source_ref == urls[0].id
               and r.description == "source"]
    assert len(src_rel) == 1


def test_description_defangs_urls_and_domains():
    source = _api_fixture("PostDetails1")
    source["forum"]["title"] = "evil.com"
    source["forum"]["description"] = "See http://malware.example/drop for details"
    media = json.loads(_by_type(StixMapper(_settings()).map(source), "media-content")[0].serialize())
    desc = media["x_opencti_description"]
    assert "evil[.]com" in desc
    assert "hxxp://malware[.]example" in desc
    assert "http://" not in desc and "evil.com" not in desc


def test_malware_family_has_type_label():
    bundle = StixMapper(_settings()).map(_api_fixture("SimplifiedMalwareProfile"))
    assert "verity471:malware_family" in _by_type(bundle, "malware")[0].labels


def test_event_malware_has_types_and_seen():
    bundle = StixMapper(_settings()).map(_api_fixture("IntegrationsEvent"))
    malware = _by_type(bundle, "malware")[0]
    assert str(malware.first_seen).startswith("2018-08-07")
    assert str(malware.last_seen).startswith("2018-08-07")
    assert malware.description  # GIR names / event type


def test_event_infrastructure_is_enriched():
    bundle = StixMapper(_settings()).map(_api_fixture("IntegrationsEvent"))
    infra = _by_type(bundle, "infrastructure")[0]
    # C2 infra now carries first/last seen, a description and GIR labels
    assert str(infra.first_seen).startswith("2018-08-07")
    assert str(infra.last_seen).startswith("2018-08-07")
    assert infra.description.startswith("Command-and-control infrastructure")
    assert any(l.startswith("Intel 471 - GIR ") for l in infra.labels)


def test_credential_password_stored_in_credential_field():
    source = _api_fixture("GetCredResponse")
    source["data"]["password"]["password_plain"] = "hunter2"
    bundle = StixMapper(_settings()).map(source)
    account = _by_type(bundle, "user-account")[0]
    assert account.credential == "hunter2"


def test_credential_set_maps_victim_organizations():
    source = _api_fixture("GetCredSetResponse")
    source["data"]["victims"] = [{"name": "ACME", "links": [{"external": {"href": "https://acme.example"}}]}]
    bundle = StixMapper(_settings()).map(source)
    orgs = [i for i in _by_type(bundle, "identity") if i.identity_class == "organization" and i.name == "ACME"]
    assert len(orgs) == 1
    assert orgs[0].contact_information == "https://acme.example"


# ---------------------------------------------------------------------------
# Malware event / malware family.
# ---------------------------------------------------------------------------

def test_event_emits_malware_and_c2_infrastructure():
    bundle = StixMapper(_settings()).map(_api_fixture("IntegrationsEvent"))
    malware = _by_type(bundle, "malware")
    infra = _by_type(bundle, "infrastructure")
    assert malware and malware[0].is_family is True
    assert infra and infra[0].infrastructure_types == ["command-and-control"]
    rel_types = {r.relationship_type for r in _by_type(bundle, "relationship")}
    assert {"uses", "consists-of"} <= rel_types
    assert "verity471:malware_event_artifact_extraction" in malware[0].labels


def test_malware_family_is_family_with_os_software_and_seen():
    source = _api_fixture("SimplifiedMalwareProfile")
    source["aliases"] = ["alias1", "alias2"]
    source["classification"] = {"girs": [{"name": "Information Stealer Malware", "path": "1.2.3"}]}
    bundle = StixMapper(_settings()).map(source)
    malware = json.loads(_by_type(bundle, "malware")[0].serialize())
    assert malware["is_family"] is True
    assert set(malware["aliases"]) == {"alias1", "alias2"}
    # OS/platform is a linked Software observable via an explicit relationship
    # (OpenCTI doesn't render operating_system_refs, but does render relationships)
    software = _by_type(bundle, "software")
    assert [s.name for s in software] == ["windows"]
    assert "operating_system_refs" not in malware
    assert "architecture_execution_envs" not in malware
    os_rel = [r for r in _by_type(bundle, "relationship")
              if r.source_ref == malware["id"] and r.target_ref == software[0].id
              and r.relationship_type == "related-to" and r.description == "operating system"]
    assert len(os_rel) == 1
    # GIR -> malware_types, and first/last seen from activity
    assert "spyware" in malware["malware_types"]
    assert str(malware["first_seen"]).startswith("2023-10-25")
    assert str(malware["last_seen"]).startswith("2026-01-13")


# ---------------------------------------------------------------------------
# Data-leak-site post + CSAM attachment handling.
# ---------------------------------------------------------------------------

def test_dls_post_maps_channel_media_and_skips_csam_attachment():
    source = _api_fixture("DataLeakSitePostsStreamingPage")["posts"][0]
    source["post"]["attachments"] = [
        {"classification": "csam", "file_hash": "a" * 64, "file_name": "bad.jpg"},
        {"classification": "safe", "file_name": "leak.txt"},
    ]
    bundle = StixMapper(_settings()).map(source)
    files = _by_type(bundle, "file")
    assert len(files) == 1 and files[0].name == "leak.txt"
    assert _by_type(bundle, "channel") and _by_type(bundle, "media-content")


# ---------------------------------------------------------------------------
# Alerts orchestrator.
# ---------------------------------------------------------------------------

def _alert(source_id, portal="https://portal.example/x"):
    return SimpleNamespace(
        source_id=source_id,
        creation_ts=datetime.datetime(2026, 2, 19, 15, 34, 31, tzinfo=datetime.timezone.utc),
        links=SimpleNamespace(
            verity_portal=SimpleNamespace(href=portal),
            verity_api=SimpleNamespace(href="https://api.example/x"),
        ),
    )


def _watcher(name):
    return SimpleNamespace(name=name)


def _post_target():
    return PostDetails1.from_dict(_api_fixture("PostDetails1"))


def _credset_target():
    return GetCredSetResponse.from_dict(_api_fixture("GetCredSetResponse"))


def _map_alerts(alert_targets, **settings_kw):
    source = _api_fixture("AlertsStreamResponse")
    with patch("verity471.verity_stix.mappers.alerts.fetch_alert_targets", return_value=alert_targets):
        return StixMapper(_settings(**settings_kw)).map(source)


def test_alert_wraps_target_in_incident_with_watcher_context():
    at = AlertTarget(alert=_alert("post--1"), target=_post_target(),
                     watcher=_watcher("w1"), watcher_group=_watcher("g1"))
    bundle = _map_alerts([at])
    incidents = _by_type(bundle, "incident")
    assert len(incidents) == 1
    inc = incidents[0]
    assert inc.incident_type == "alert"
    assert inc.source == "Intel 471 Verity"
    assert "watcher:w1" in inc.labels and "watcher_group:g1" in inc.labels
    assert inc.external_references[0].url == "https://portal.example/x"
    # incident -> content via related-to
    related = [r for r in _by_type(bundle, "relationship")
               if r.relationship_type == "related-to" and r.source_ref == inc.id]
    assert related


def test_incident_carries_gir_labels_and_description():
    from verity471.models.integrations_event import IntegrationsEvent
    ev = IntegrationsEvent.from_dict(_api_fixture("IntegrationsEvent"))
    at = AlertTarget(alert=_alert("malware-event--1"), target=ev,
                     watcher=_watcher("w1"), watcher_group=_watcher("g1"))
    inc = _by_type(_map_alerts([at]), "incident")[0]
    # GIR labels from the event's malware are surfaced on the incident
    assert any(l.startswith("Intel 471 - GIR ") for l in inc.labels)
    # incident has a populated description and first/last seen
    assert inc.description
    assert inc.first_seen is not None and inc.last_seen is not None


def test_credential_set_alert_is_data_breach_incident():
    at = AlertTarget(alert=_alert("cred-set--1"), target=_credset_target(),
                     watcher=_watcher("w1"), watcher_group=_watcher("g1"))
    bundle = _map_alerts([at])
    inc = _by_type(bundle, "incident")[0]
    assert inc.incident_type == "data-breach"


def test_multiple_watchers_same_target_collapse_to_one_incident():
    ats = [
        AlertTarget(alert=_alert("post--1"), target=_post_target(), watcher=_watcher("w1"), watcher_group=_watcher("g1")),
        AlertTarget(alert=_alert("post--1"), target=_post_target(), watcher=_watcher("w2"), watcher_group=_watcher("g1")),
    ]
    bundle = _map_alerts(ats)
    incidents = _by_type(bundle, "incident")
    assert len(incidents) == 1
    assert {"watcher:w1", "watcher:w2", "watcher_group:g1"} <= set(incidents[0].labels)


def test_label_only_mode_emits_no_incident_and_tags_content():
    at = AlertTarget(alert=_alert("post--1"), target=_post_target(),
                     watcher=_watcher("w1"), watcher_group=_watcher("g1"))
    bundle = _map_alerts([at], alerts_create_incident=False)
    assert not _by_type(bundle, "incident")
    channel = _by_type(bundle, "channel")[0]
    assert "watcher:w1" in channel.labels


def test_empty_targets_returns_none():
    source = _api_fixture("AlertsStreamResponse")
    with patch("verity471.verity_stix.mappers.alerts.fetch_alert_targets", return_value=[]):
        # AlertsMapper.map returns None -> StixMapper raises EmptyBundle
        from verity471.verity_stix.exceptions import EmptyBundle
        with pytest.raises(EmptyBundle):
            StixMapper(_settings()).map(source)


def test_alerts_require_api_client():
    source = _api_fixture("AlertsStreamResponse")
    with pytest.raises(StixMapperNotFound):
        StixMapper(STIXMapperSettings(api_client=None)).map(source)


@pytest.mark.parametrize("report_full_content", [True, False])
def test_report_targets_are_fetched_with_inline_images(report_full_content):
    # A report reached through an alert must be fetched the same way as one
    # mapped directly from the reports API, i.e. with its images inlined.
    source = _api_fixture("AlertsStreamResponse")
    at = AlertTarget(alert=_alert("post--1"), target=_post_target())
    with patch("verity471.verity_stix.mappers.alerts.fetch_alert_targets",
               return_value=[at]) as fetch_mock:
        StixMapper(_settings(report_full_content=report_full_content)).map(source)
    assert fetch_mock.call_args.kwargs["include_inline_images"] is report_full_content
