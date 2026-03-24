import json
from unittest.mock import MagicMock, patch

import pytest

from tests.conftest import PREFIX, read_fixture
from verity471 import fetch_alert_targets
import verity471


configuration = verity471.Configuration()


test_params = {
    'IndicatorsApi:get_indicator_by_id': ('IntegrationsIndicator', 'https://api.intel471.cloud/integrations/indicators/v1/indicators/malware-indicator--00000000-0000-0000-0000-000000000000', '[Indicator] file | 0000000000000000000000000000000000000000000000000000000000000000 | confidence: 50'),
    'EventsApi:get_event_by_id': ('IntegrationsEvent', 'https://api.intel471.cloud/integrations/malware-intel/v1/events/malware-event--00000000-0000-0000-0000-000000000000', '[Artifact Extraction] dummy'),
    'MalwareApi:get_malware_family_by_id': ('SimplifiedMalwareProfile', 'https://api.intel471.cloud/integrations/malware-intel/v1/malware/malware-family--00000000-0000-0000-0000-000000000000', '[Malware] dummy | dummy'),
    'CredentialsApi:get_credential_sets_id': ('GetCredSetResponse', 'https://api.intel471.cloud/integrations/creds/v1/credential-sets/cred-set--84c92b87-ed31-5103-8101-97b87c03a47a', '[Credential Set] dummy | 913706 records | 2023-01-16 00:00:00+00:00'),
    'CredentialsApi:get_credentials_id': ('GetCredResponse', 'https://api.intel471.cloud/integrations/creds/v1/credentials/cred--3f2abe55-8469-59db-b25a-f8268eb31f34', '[Credential] user@example.com | dummy | 2023-01-18T08:08:19.994Z'),
    'CredentialsApi:get_credentials_occurrences_id': ('GetCredOccurrenceResponse', 'https://api.intel471.cloud/integrations/creds/v1/credentials/occurrences/cred-occurrence--1edd10b4-e75d-5aa2-9b43-5e08c6a682cb', '[Credential Occurrence] dummy | 2023-01-18T08:08:19.994Z'),
    'ReportsApi:get_reports_breach_alert_id': ('BreachAlertByIdResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/breach-alert/report--fbbb23d6-713f-5f41-9ee4-45b3ff027017', '[Breach Alert] dummy | 2021-07-01T09:17:33Z'),
    'ReportsApi:get_reports_fintel_id': ('FintelResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/fintel/report--e71d387f-325e-5bfc-a43d-143876c6cfc0', '[Fintel] dummy | 2020-01-03T20:41:55Z | <p>Actor summaryThe actor AD0 is a long-standing member of the Russian-speaking ...</p>'),
    'ReportsApi:get_reports_geopol_id': ('GeopolReportDetailsResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/geopol/report--464ad694-6e92-5983-93f2-f0a7f4d84d7e', '[Geopol Report] dummy | 2024-04-16T16:41:10Z | <p>Event backgroundFollowing the Oct</p>'),
    'ReportsApi:get_reports_info_id': ('InfoReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/info/report--1d4f77cb-ee3b-5ec2-9291-8cf9356bdfb8', '[Info Report] dummy | 2014-06-25T23:49:04Z | <p>Within the last few days the online service Indexeus http://indexeus</p>'),
    'ReportsApi:get_reports_malware_id': ('MalwareReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/malware/report--8d11b63b-f7d6-5061-bb17-290ee5af9464', '[Malware Report] dummy | 2019-01-31T14:16:22Z | <p>Malware Analysis Report # Summary # Pony loader, aka Fareit, is a credential ...</p>'),
    'ReportsApi:get_reports_spot_id': ('SpotReportResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/spot/report--cb89fbf0-4a56-5f0c-8bd4-166b2115362f', '[Spot Report] dummy | 2019-01-17T16:59:57Z | dummy'),
    'ReportsApi:get_reports_vulnerability_id': ('VulnerabilitiesReportDetailsResponse', 'https://api.intel471.cloud/integrations/intel-report/v1/reports/vulnerability/vulnerability--451a1d7b-e555-5c25-bb21-f544d2ce6997', '[Vulnerability Report] dummy | dummy | dummy | RiskLevel.HIGH | VulnerabilityStatus.HISTORICAL'),
    'SourcesApi:get_forums_posts_post_id': ('PostDetails1', 'https://api.intel471.cloud/integrations/sources/v1/forums/posts/post--44a97352-e0bf-537a-8b51-13e16992586b', '[Forum Post] 2022-10-13T16:05:37Z'),
    'SourcesApi:get_forums_private_messages_private_message_id': ('PrivateMessageDetails1', 'https://api.intel471.cloud/integrations/sources/v1/forums/private-messages/private-message--d2c24f11-ed5a-5d6c-b4cc-83a5ff96c0b4', '[Forum PM] dummy | dummy | 2010-08-24T23:25:34Z'),
    'SourcesApi:get_messaging_services_messages_message_id': ('ChatRoomMessageStream', 'https://api.intel471.cloud/integrations/sources/v1/messaging-services/messages/message--da2a22d1-4d3e-5b79-b557-c275453f31f9', '[Message] dummy | 2017-02-27T02:37:48Z'),
}

@patch('verity471.rest.RESTClientObject')
@pytest.mark.parametrize('filename, query_url, expected_target_summary', test_params.values(), ids=test_params.keys())
def test_api_responses(rest_client_class_mock, filename, query_url, expected_target_summary):
    

    
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

        mock_alerts_response = MagicMock(name='alerts_response')
        mock_alert = MagicMock(name='alert')
        mock_alert.links.verity_api.href = query_url
        mock_alerts_response.alerts = [mock_alert]
        response = fetch_alert_targets(mock_alerts_response, api_client)
        assert response[0].target is not None
        assert response[0].target_summary == expected_target_summary