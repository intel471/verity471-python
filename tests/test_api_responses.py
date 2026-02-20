import json
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
import verity471

from .conftest import PREFIX, read_fixture


configuration = verity471.Configuration()


def normalize_for_comparison(obj):
    """Normalize a dictionary by converting datetime objects to ISO strings."""
    if isinstance(obj, datetime):
        # Convert datetime to ISO format with 'Z' suffix for UTC
        iso_str = obj.isoformat()
        # Replace +00:00 with Z to match the JSON format
        if iso_str.endswith('+00:00'):
            return iso_str[:-6] + 'Z'
        # If timezone-naive, assume UTC and add Z
        elif obj.tzinfo is None:
            return iso_str + 'Z'
        else:
            return iso_str
    elif isinstance(obj, dict):
        return {k: normalize_for_comparison(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [normalize_for_comparison(item) for item in obj]
    else:
        return obj

test_params = {
    'IndicatorsApi:get_indicators_stream': ('IndicatorsApi', 'get_indicators_stream', {'size': 1}, 'IndicatorStreamResponse', 'https://api.intel471.cloud/integrations/indicators/v1/indicators/stream?size=1'),
    'IndicatorsApi:get_indicator_by_id': ('IndicatorsApi', 'get_indicator_by_id', {'id': 'malware-indicator--00000000-0000-0000-0000-000000000000'}, 'IntegrationsIndicator', 'https://api.intel471.cloud/integrations/indicators/v1/indicators/malware-indicator--00000000-0000-0000-0000-000000000000'),
    'EventsApi:get_events_stream': ('EventsApi', 'get_events_stream', {'size': 1}, 'EventsStreamResponse', 'https://api.intel471.cloud/integrations/malware-intel/v1/events/stream?size=1'),
    'EventsApi:get_event_by_id': ('EventsApi', 'get_event_by_id', {'id': 'malware-event--00000000-0000-0000-0000-000000000000'}, 'IntegrationsEvent', 'https://api.intel471.cloud/integrations/malware-intel/v1/events/malware-event--00000000-0000-0000-0000-000000000000'),
    'GIRsApi:get_list_of_girs_in_a_hierarchical_structure': ('GIRsApi', 'get_list_of_girs_in_a_hierarchical_structure', {}, 'GirsTreeResponse', 'https://api.intel471.cloud/integrations/girs/v1/girs/tree'),
    'MalwareApi:get_malware_list': ('MalwareApi', 'get_malware_list', {'size': 1}, 'AllMalwareProfilesResponse', 'https://api.intel471.cloud/integrations/malware-intel/v1/malware?size=1'),
    'MalwareApi:get_malware_family_by_id': ('MalwareApi', 'get_malware_family_by_id', {'id': 'malware-family--00000000-0000-0000-0000-000000000000'}, 'SimplifiedMalwareProfile', 'https://api.intel471.cloud/integrations/malware-intel/v1/malware/malware-family--00000000-0000-0000-0000-000000000000'),
    'CredentialsApi:get_credential_sets_accessed_urls_stream': ('CredentialsApi', 'get_credential_sets_accessed_urls_stream', {'size': 1}, 'GetCredSetAccessedUrlResponseStream', 'https://api.intel471.cloud/integrations/creds/v1/credential-sets/accessed-urls/stream?size=1'),
    'CredentialsApi:get_credential_sets_id': ('CredentialsApi', 'get_credential_sets_id', {'id': 'cred-set--84c92b87-ed31-5103-8101-97b87c03a47a'}, 'GetCredSetResponse', 'https://api.intel471.cloud/integrations/creds/v1/credential-sets/cred-set--84c92b87-ed31-5103-8101-97b87c03a47a'),
    'CredentialsApi:get_credential_sets_stream': ('CredentialsApi', 'get_credential_sets_stream', {'size': 1}, 'GetCredSetResponseStream', 'https://api.intel471.cloud/integrations/creds/v1/credential-sets/stream?size=1'),
    'CredentialsApi:get_credentials_id': ('CredentialsApi', 'get_credentials_id', {'id': 'cred--3f2abe55-8469-59db-b25a-f8268eb31f34'}, 'GetCredResponse', 'https://api.intel471.cloud/integrations/creds/v1/credentials/cred--3f2abe55-8469-59db-b25a-f8268eb31f34'),
    'CredentialsApi:get_credentials_occurrences_id': ('CredentialsApi', 'get_credentials_occurrences_id', {'id': 'cred-occurrence--1edd10b4-e75d-5aa2-9b43-5e08c6a682cb'}, 'GetCredOccurrenceResponse', 'https://api.intel471.cloud/integrations/creds/v1/credentials/occurrences/cred-occurrence--1edd10b4-e75d-5aa2-9b43-5e08c6a682cb'),
    'CredentialsApi:get_credentials_occurrences_stream': ('CredentialsApi', 'get_credentials_occurrences_stream', {'size': 1}, 'GetCredOccurrenceResponseStream', 'https://api.intel471.cloud/integrations/creds/v1/credentials/occurrences/stream?size=1'),
    'CredentialsApi:get_credentials_stream': ('CredentialsApi', 'get_credentials_stream', {'size': 1}, 'GetCredResponseStream', 'https://api.intel471.cloud/integrations/creds/v1/credentials/stream?size=1'),
    'ReportsApi:get_reports_breach_alert_id': ('ReportsApi', 'get_reports_breach_alert_id', {'id': 'report--fbbb23d6-713f-5f41-9ee4-45b3ff027017'}, 'BreachAlertByIdResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/breach-alert/report--fbbb23d6-713f-5f41-9ee4-45b3ff027017'),
    'ReportsApi:get_reports_breach_alert_stream': ('ReportsApi', 'get_reports_breach_alert_stream', {'size': 1}, 'BreachAlertsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/breach-alert/stream?size=1'),
    'ReportsApi:get_reports_fintel_id': ('ReportsApi', 'get_reports_fintel_id', {'id': 'report--e71d387f-325e-5bfc-a43d-143876c6cfc0'}, 'FintelResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/fintel/report--e71d387f-325e-5bfc-a43d-143876c6cfc0'),
    'ReportsApi:get_reports_fintel_stream': ('ReportsApi', 'get_reports_fintel_stream', {'size': 1}, 'FintelReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/fintel/stream?size=1'),
    'ReportsApi:get_reports_geopol_id': ('ReportsApi', 'get_reports_geopol_id', {'id': 'report--464ad694-6e92-5983-93f2-f0a7f4d84d7e'}, 'GeopolReportDetailsResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/geopol/report--464ad694-6e92-5983-93f2-f0a7f4d84d7e'),
    'ReportsApi:get_reports_geopol_stream': ('ReportsApi', 'get_reports_geopol_stream', {'size': 1}, 'GeopolReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/geopol/stream?size=1'),
    'ReportsApi:get_reports_info_id': ('ReportsApi', 'get_reports_info_id', {'id': 'report--1d4f77cb-ee3b-5ec2-9291-8cf9356bdfb8'}, 'InfoReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/info/report--1d4f77cb-ee3b-5ec2-9291-8cf9356bdfb8'),
    'ReportsApi:get_reports_info_stream': ('ReportsApi', 'get_reports_info_stream', {'size': 1}, 'InfoReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/info/stream?size=1'),
    'ReportsApi:get_reports_malware_id': ('ReportsApi', 'get_reports_malware_id', {'id': 'report--8d11b63b-f7d6-5061-bb17-290ee5af9464'}, 'MalwareReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/malware/report--8d11b63b-f7d6-5061-bb17-290ee5af9464'),
    'ReportsApi:get_reports_malware_stream': ('ReportsApi', 'get_reports_malware_stream', {'size': 1}, 'MalwareReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/malware/stream?size=1'),
    'ReportsApi:get_reports_spot_id': ('ReportsApi', 'get_reports_spot_id', {'id': 'report--cb89fbf0-4a56-5f0c-8bd4-166b2115362f'}, 'SpotReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/spot/report--cb89fbf0-4a56-5f0c-8bd4-166b2115362f'),
    'ReportsApi:get_reports_spot_stream': ('ReportsApi', 'get_reports_spot_stream', {'size': 1}, 'SpotReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/spot/stream?size=1'),
    'ReportsApi:get_reports_stream': ('ReportsApi', 'get_reports_stream', {'size': 1}, 'ReportResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/stream?size=1'),
    'ReportsApi:get_reports_vulnerability_id': ('ReportsApi', 'get_reports_vulnerability_id', {'id': 'vulnerability--451a1d7b-e555-5c25-bb21-f544d2ce6997'}, 'VulnerabilitiesReportDetailsResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/vulnerability/vulnerability--451a1d7b-e555-5c25-bb21-f544d2ce6997'),
    'ReportsApi:get_reports_vulnerability_stream': ('ReportsApi', 'get_reports_vulnerability_stream', {'size': 1}, 'VulnerabilitiesReportsResponseStream', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/vulnerability/stream?size=1'),
    # 'SourcesApi:get_data_leak_sites_file_listings_id': ('SourcesApi', 'get_data_leak_sites_file_listings_id', {'id': 'myid-1234'}, 'DataLeakSiteFileListingResponse', 'https://api.intel471.cloud/integrations/sources/v1/data-leak-sites/file-listings/myid-1234'),
    'SourcesApi:get_data_leak_sites_posts_stream': ('SourcesApi', 'get_data_leak_sites_posts_stream', {'size': 1}, 'DataLeakSitePostsStreamingPage', 'https://api.intel471.cloud/integrations/sources/v1/data-leak-sites/posts/stream?size=1'),
    'SourcesApi:get_forums_posts_post_id': ('SourcesApi', 'get_forums_posts_post_id', {'post_id': 'post--44a97352-e0bf-537a-8b51-13e16992586b'}, 'PostDetails1', 'https://api.intel471.cloud/integrations/sources/v1/forums/posts/post--44a97352-e0bf-537a-8b51-13e16992586b'),
    'SourcesApi:get_forums_posts_stream': ('SourcesApi', 'get_forums_posts_stream', {'size': 1}, 'ForumsPostsStreamingPage', 'https://api.intel471.cloud/integrations/sources/v1/forums/posts/stream?size=1'),
    'SourcesApi:get_forums_private_messages_private_message_id': ('SourcesApi', 'get_forums_private_messages_private_message_id', {'private_message_id': 'private-message--d2c24f11-ed5a-5d6c-b4cc-83a5ff96c0b4'}, 'PrivateMessageDetails1', 'https://api.intel471.cloud/integrations/sources/v1/forums/private-messages/private-message--d2c24f11-ed5a-5d6c-b4cc-83a5ff96c0b4'),
    'SourcesApi:get_forums_private_messages_stream': ('SourcesApi', 'get_forums_private_messages_stream', {'size': 1}, 'ForumsPrivateMessagesStreamingPage', 'https://api.intel471.cloud/integrations/sources/v1/forums/private-messages/stream?size=1'),
    'SourcesApi:get_messaging_services_messages_message_id': ('SourcesApi', 'get_messaging_services_messages_message_id', {'message_id': 'message--da2a22d1-4d3e-5b79-b557-c275453f31f9'}, 'ChatRoomMessageStream', 'https://api.intel471.cloud/integrations/sources/v1/messaging-services/messages/message--da2a22d1-4d3e-5b79-b557-c275453f31f9'),
    'SourcesApi:get_messaging_services_messages_stream': ('SourcesApi', 'get_messaging_services_messages_stream', {'size': 1}, 'ChatMessagesStreamingPage', 'https://api.intel471.cloud/integrations/sources/v1/messaging-services/messages/stream?size=1'),
    'EntitiesApi:get_entities_stream': ('EntitiesApi', 'get_entities_stream', {'entity': 'intel.com', 'size': 1}, 'EntitiesStreamResponse', 'https://api.intel471.cloud/integrations/entities/v1/entities/stream?entity=intel.com&size=1'),
    'ObservablesApi:get_observables_stream': ('ObservablesApi', 'get_observables_stream', {'observable': 'domain'}, 'ObservablesStreamResponse', 'https://api.intel471.cloud/integrations/observables/v1/observables/stream?observable=domain'),
    'AlertsApi:get_alerts_stream': ('AlertsApi', 'get_alerts_stream', {'size': 1}, 'AlertsStreamResponse', 'https://api.intel471.cloud/integrations/watchers/v1/alerts/stream?size=1'),
    'WatchersApi:get_watchers': ('WatchersApi', 'get_watchers', {}, 'WatchersResponse', 'https://api.intel471.cloud/integrations/watchers/v1/watchers'),
    'WatchersApi:get_watcher_groups': ('WatchersApi', 'get_watcher_groups', {}, 'WatcherGroupsResponse', 'https://api.intel471.cloud/integrations/watchers/v1/watcher-groups'),
    'ActorsApi:get_actors_stream': ('ActorsApi', 'get_actors_stream', {'actor': 'yalishanda', 'size': 100}, 'ActorsStreamResponse', 'https://api.intel471.cloud/integrations/actors/v1/actors/stream?actor=yalishanda&size=100'),
}

@patch('verity471.rest.RESTClientObject')
@pytest.mark.parametrize('api_cls_name, method_name, kwargs, filename, query_url', test_params.values(), ids=test_params.keys())
def test_api_responses(rest_client_class_mock, api_cls_name, method_name, kwargs, filename, query_url):
    rest_client_response = MagicMock(name='rest_client_response')
    rest_client_response.status = 200
    rest_client_response.reason = 'OK'
    rest_client_response.headers = {'content-type': 'application/json; charset=utf-8'}
    response = read_fixture(f'{PREFIX}/fixtures/api_responses/{filename}.json')
    rest_client_response.data = json.dumps(response).encode('utf-8')

    rest_client_instance_mock = MagicMock(name='rest_client_instance')
    rest_client_instance_mock.request.return_value = rest_client_response

    rest_client_class_mock.side_effect = [rest_client_instance_mock]

    with verity471.ApiClient(configuration) as api_client:
        api_instance = getattr(verity471, api_cls_name)(api_client)
        api_response = getattr(api_instance, method_name)(**kwargs)

        assert rest_client_instance_mock.request.call_args_list[0][0][1] == query_url
        normalized_response = normalize_for_comparison(api_response.to_dict())
        assert normalized_response == response
