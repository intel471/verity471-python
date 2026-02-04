# Verity471

The official Python SDK for the Verity471 API.

The client abstracts low-level API concerns by performing automatic query and payload validation and exposing a clean, typed interface to Verity471 data.

It also bridges the gap to standard CTI workflows by providing built-in STIX mapping for supported 
data items, allowing easier integration with threat intelligence platforms.

API bindings are generated via [OpenAPI Generator](https://openapi-generator.tech), with manual extensions for validation and STIX support.

- API version: 1.0.0
  - creds: 1.0.0
  - girs: 1.0.0
  - indicators: 1.0.0
  - malware: 1.0.0
  - reports: 1.0.0
  - sources: 1.0.0

- Package version: 1.0.0
- Generator version: 7.19.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.10 

## Installation

### Install from PyPI (recommended)

```sh
pip install verity471
```

This installs the core SDK without optional STIX support.

#### Optional features

STIX support:

```
pip install "verity471[stix]"
```

Development and test dependencies:

```
pip install "verity471[test]"
```

Both extras can be installed together:

```
pip install "verity471[stix,test]"
```

### Install from GitHub

You can also install the SDK directly from the Git repository:

```sh
pip install git+ssh://git@github.com/intel471/verity471-python.git
```

With extras:

```
pip install "git+ssh://git@github.com/intel471/verity471-python.git#egg=verity471[stix,test]"
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import verity471
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:

    # Create an instance of the API class
    api_instance = verity471.IndicatorsApi(api_client)

    threat_type = 'malware' # str | Search indicators by threat type
    malware_family_name = 'trickbot' # str | Search indicators by malware family
    var_from = 1767225600000 # int | Search from specific date (UNIX timestamp in milliseconds)
    size = 10 # int | Number from 1 to 1000 (default to 1000)

    try:
        # Indicators stream
        api_response = api_instance.get_indicators_stream(threat_type=threat_type, malware_family_name=malware_family_name, var_from=var_from, size=size)
        print("The response of IndicatorsApi->get_indicators_stream:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IndicatorsApi->get_indicators_stream: %s\n" % e)

```

## Serialization

Each call to an API instance returns a structure composed of Python objects. The response can be serialized into one of the common formats, if needed.

### Python dict

To convert the response into a Python `dict`, call the `to_dict()` method on the response object.

```
serialized = api_response.to_dict()
```

### STIX format

> **Note**  
> STIX support requires optional dependencies.  
> Install with:
>
> ```sh
> pip install "verity471[stix]"
> ```

To convert the response into the [STIX format (v2.1)](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html), call the `to_stix()` method on the response object.
This method converts the API response into the corresponding STIX objects and returns them wrapped in a `Bundle` object (from [stix2](https://pypi.org/project/stix2/) package).
The `Bundle` object can be serialized into a JSON string using its `serialize()` method.

```
bundle = api_response.to_stix()
json_repr = bundle.serialize()
```

Some responses can be augmented with additional data obtained via extra API calls. This applies 
only to report-related stream endpoints.

Stream endpoints are designed for search. When a report is large, the returned payload may be truncated: 
inline images are always removed, and in some cases entire fields are omitted. When fields are omitted, 
the `is_truncated` flag is set to `true`. As a result, the streamed representation may not contain the 
full report content.

If an instance of `verity471.verity_stix.STIXMapperSettings` is passed to the `to_stix()` method 
with the `report_full_content` flag set to `True`, the mapper will issue additional API calls to 
retrieve the full representation of each truncated report referenced in the stream results. This allows 
to execute a stream (search) endpoint and serialize it into STIX while still obtaining complete 
report data.

The `STIXMapperSettings` instance must be initialized with the `verity471` package and an 
initialized `api_client`.

For the complete list of available settings, see the implementation of the `STIXMapperSettings` 
class in [verity471/verity_stix/__init__.py](verity471/verity_stix/__init__.py).

```
import verity471
from verity471.verity_stix import STIXMapperSettings

configuration = verity471.Configuration(...)

with verity471.ApiClient(configuration) as api_client:
    api_instance = verity471.ReportsApi(api_client)
    api_response = api_instance.get_reports_info_stream(size=1)
    mapper_settings = STIXMapperSettings(
        verity471,
        api_client,
        report_full_content=True
    )
    bundle = api_response.to_stix(mapper_settings)
```

If the objects returned by the endpoint for some reason can't be mapped into STIX format, `EmptyBundle` exception will be raised.

At the moment following API methods provide the response in STIX format:

Client's class/method | API endpoint | Produced outcome
------------------------|-------------|-----------------
`IndicatorsApi.get_indicators_stream` | `/indicators/stream` | `Indicator` and `Malware` SDOs related using `Relationship` object; `URL`, `IPv4Address`, `File`, `DomainName` or `EmailAddress`  Observable related with the `Indicator` SDO using `Relationship` object
`IndicatorsApi.get_indicator_by_id` | `/indicators/{id}` |
`ReportsApi.get_reports_breach_alert_stream` | `/reports/breach-alert/stream` | `Report` SDOs with related entities/victims via `object_refs` (`Identity`/Org, `Malware`, `ThreatActor`, `Vulnerability` and observables like `URL`, `DomainName`, `IPv4Address`, `IPv6Address`, `EmailAddress`, `AutonomousSystem`, `File`, `UserAccount`, `CryptocurrencyWallet`)
`ReportsApi.get_reports_breach_alert_id` | `/reports/breach-alert/{id}` |
`ReportsApi.get_reports_fintel_stream` | `/reports/fintel/stream` |
`ReportsApi.get_reports_fintel_id` | `/reports/fintel/{id}` |
`ReportsApi.get_reports_geopol_stream` | `/reports/geopol/stream` |
`ReportsApi.get_reports_geopol_id` | `/reports/geopol/{id}` |
`ReportsApi.get_reports_info_stream` | `/reports/info/stream` |
`ReportsApi.get_reports_info_id` | `/reports/info/{id}` |
`ReportsApi.get_reports_malware_stream` | `/reports/malware/stream` |
`ReportsApi.get_reports_malware_id` | `/reports/malware/{id}` |
`ReportsApi.get_reports_spot_stream` | `/reports/spot/stream` |
`ReportsApi.get_reports_spot_id` | `/reports/spot/{id}` |
`ReportsApi.get_reports_vulnerability_stream` | `/reports/vulnerability/stream` | `Vulnerability` SDOs 
`ReportsApi.get_reports_vulnerability_id` | `/reports/vulnerability/{id}` |  

*Empty cells inherit the value from the previous row.*

## Documentation for API Endpoints

All URIs are relative to *https://api.intel471.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CredentialsApi* | [**get_credential_sets_accessed_urls_stream**](docs/CredentialsApi.md#get_credential_sets_accessed_urls_stream) | **GET** /integrations/creds/v1/credential-sets/accessed-urls/stream | Credential set accessed url stream
*CredentialsApi* | [**get_credential_sets_id**](docs/CredentialsApi.md#get_credential_sets_id) | **GET** /integrations/creds/v1/credential-sets/{id} | Get credential set by ID
*CredentialsApi* | [**get_credential_sets_stream**](docs/CredentialsApi.md#get_credential_sets_stream) | **GET** /integrations/creds/v1/credential-sets/stream | Credential set stream
*CredentialsApi* | [**get_credentials_id**](docs/CredentialsApi.md#get_credentials_id) | **GET** /integrations/creds/v1/credentials/{id} | Get credential by ID
*CredentialsApi* | [**get_credentials_occurrences_id**](docs/CredentialsApi.md#get_credentials_occurrences_id) | **GET** /integrations/creds/v1/credentials/occurrences/{id} | Get credential occurrence by ID
*CredentialsApi* | [**get_credentials_occurrences_stream**](docs/CredentialsApi.md#get_credentials_occurrences_stream) | **GET** /integrations/creds/v1/credentials/occurrences/stream | Credential occurrence stream
*CredentialsApi* | [**get_credentials_stream**](docs/CredentialsApi.md#get_credentials_stream) | **GET** /integrations/creds/v1/credentials/stream | Credential stream
*EventsApi* | [**get_event_by_id**](docs/EventsApi.md#get_event_by_id) | **GET** /integrations/malware-intel/v1/events/{id} | Get event by id
*EventsApi* | [**get_events_stream**](docs/EventsApi.md#get_events_stream) | **GET** /integrations/malware-intel/v1/events/stream | Stream malware events using a cursor
*GIRsApi* | [**get_list_of_girs_in_a_hierarchical_structure**](docs/GIRsApi.md#get_list_of_girs_in_a_hierarchical_structure) | **GET** /integrations/girs/v1/girs/tree | 
*IndicatorsApi* | [**get_indicator_by_id**](docs/IndicatorsApi.md#get_indicator_by_id) | **GET** /integrations/indicators/v1/indicators/{id} | Get indicator by id
*IndicatorsApi* | [**get_indicators_stream**](docs/IndicatorsApi.md#get_indicators_stream) | **GET** /integrations/indicators/v1/indicators/stream | Stream indicators using a cursor
*MalwareApi* | [**get_malware_family_by_id**](docs/MalwareApi.md#get_malware_family_by_id) | **GET** /integrations/malware-intel/v1/malware/{id} | Get malware family details by id
*MalwareApi* | [**get_malware_list**](docs/MalwareApi.md#get_malware_list) | **GET** /integrations/malware-intel/v1/malware | Get list of malware families.
*ReportsApi* | [**get_reports_breach_alert_id**](docs/ReportsApi.md#get_reports_breach_alert_id) | **GET** /integrations/intel-report/v1/reports/breach-alert/{id} | Get a breach alert report details
*ReportsApi* | [**get_reports_breach_alert_stream**](docs/ReportsApi.md#get_reports_breach_alert_stream) | **GET** /integrations/intel-report/v1/reports/breach-alert/stream | Get all breach alert reports (stream)
*ReportsApi* | [**get_reports_fintel_id**](docs/ReportsApi.md#get_reports_fintel_id) | **GET** /integrations/intel-report/v1/reports/fintel/{id} | Get a fintel report details
*ReportsApi* | [**get_reports_fintel_stream**](docs/ReportsApi.md#get_reports_fintel_stream) | **GET** /integrations/intel-report/v1/reports/fintel/stream | Get all fintel reports (stream)
*ReportsApi* | [**get_reports_geopol_id**](docs/ReportsApi.md#get_reports_geopol_id) | **GET** /integrations/intel-report/v1/reports/geopol/{id} | Get a geopol report details
*ReportsApi* | [**get_reports_geopol_stream**](docs/ReportsApi.md#get_reports_geopol_stream) | **GET** /integrations/intel-report/v1/reports/geopol/stream | Get all geopol reports (stream)
*ReportsApi* | [**get_reports_info_id**](docs/ReportsApi.md#get_reports_info_id) | **GET** /integrations/intel-report/v1/reports/info/{id} | Get an info report details
*ReportsApi* | [**get_reports_info_stream**](docs/ReportsApi.md#get_reports_info_stream) | **GET** /integrations/intel-report/v1/reports/info/stream | Get all info reports (stream)
*ReportsApi* | [**get_reports_malware_id**](docs/ReportsApi.md#get_reports_malware_id) | **GET** /integrations/intel-report/v1/reports/malware/{id} | Get a malware report details
*ReportsApi* | [**get_reports_malware_stream**](docs/ReportsApi.md#get_reports_malware_stream) | **GET** /integrations/intel-report/v1/reports/malware/stream | Get all malware reports (stream)
*ReportsApi* | [**get_reports_spot_id**](docs/ReportsApi.md#get_reports_spot_id) | **GET** /integrations/intel-report/v1/reports/spot/{id} | Get a spot report details
*ReportsApi* | [**get_reports_spot_stream**](docs/ReportsApi.md#get_reports_spot_stream) | **GET** /integrations/intel-report/v1/reports/spot/stream | Get all spot reports (stream)
*ReportsApi* | [**get_reports_stream**](docs/ReportsApi.md#get_reports_stream) | **GET** /integrations/intel-report/v1/reports/stream | Get all reports (stream)
*ReportsApi* | [**get_reports_vulnerability_id**](docs/ReportsApi.md#get_reports_vulnerability_id) | **GET** /integrations/intel-report/v1/reports/vulnerability/{id} | Get a vulnerability report details
*ReportsApi* | [**get_reports_vulnerability_stream**](docs/ReportsApi.md#get_reports_vulnerability_stream) | **GET** /integrations/intel-report/v1/reports/vulnerability/stream | Get all vulnerabilities reports (stream)
*SourcesApi* | [**get_data_leak_sites_file_listings_id**](docs/SourcesApi.md#get_data_leak_sites_file_listings_id) | **GET** /integrations/sources/v1/data-leak-sites/file-listings/{id} | Get a data leak site file listing content
*SourcesApi* | [**get_data_leak_sites_posts_stream**](docs/SourcesApi.md#get_data_leak_sites_posts_stream) | **GET** /integrations/sources/v1/data-leak-sites/posts/stream | Get data leak sites posts (stream)
*SourcesApi* | [**get_forums_posts_post_id**](docs/SourcesApi.md#get_forums_posts_post_id) | **GET** /integrations/sources/v1/forums/posts/{post_id} | Get a forum post by id
*SourcesApi* | [**get_forums_posts_stream**](docs/SourcesApi.md#get_forums_posts_stream) | **GET** /integrations/sources/v1/forums/posts/stream | Get forums posts (stream)
*SourcesApi* | [**get_forums_private_messages_private_message_id**](docs/SourcesApi.md#get_forums_private_messages_private_message_id) | **GET** /integrations/sources/v1/forums/private-messages/{private_message_id} | Get a private message by id
*SourcesApi* | [**get_forums_private_messages_stream**](docs/SourcesApi.md#get_forums_private_messages_stream) | **GET** /integrations/sources/v1/forums/private-messages/stream | Get forums private messages (stream)
*SourcesApi* | [**get_messaging_services_messages_message_id**](docs/SourcesApi.md#get_messaging_services_messages_message_id) | **GET** /integrations/sources/v1/messaging-services/messages/{message_id} | Get a chat message by id
*SourcesApi* | [**get_messaging_services_messages_stream**](docs/SourcesApi.md#get_messaging_services_messages_stream) | **GET** /integrations/sources/v1/messaging-services/messages/stream | Get chat messages (stream)


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [ActivityLocation](docs/ActivityLocation.md)
 - [ActivityResponse](docs/ActivityResponse.md)
 - [ActorSubjectOfReport](docs/ActorSubjectOfReport.md)
 - [AdmiraltyCode](docs/AdmiraltyCode.md)
 - [AllMalwareProfiles](docs/AllMalwareProfiles.md)
 - [Assessment](docs/Assessment.md)
 - [AttachmentClassification](docs/AttachmentClassification.md)
 - [AttachmentData](docs/AttachmentData.md)
 - [AuthorActor1](docs/AuthorActor1.md)
 - [BadRequest](docs/BadRequest.md)
 - [BotSettings](docs/BotSettings.md)
 - [BreachAlertByIdResponse](docs/BreachAlertByIdResponse.md)
 - [BreachAlertResponse](docs/BreachAlertResponse.md)
 - [BreachAlertsResponseStream](docs/BreachAlertsResponseStream.md)
 - [ChatMessageStream](docs/ChatMessageStream.md)
 - [ChatMessagesStreamingPage](docs/ChatMessagesStreamingPage.md)
 - [ChatRoomMessageStream](docs/ChatRoomMessageStream.md)
 - [ChatServerTypeStream](docs/ChatServerTypeStream.md)
 - [Classification](docs/Classification.md)
 - [ClassificationResponse](docs/ClassificationResponse.md)
 - [Confidence](docs/Confidence.md)
 - [ConfidenceLevel](docs/ConfidenceLevel.md)
 - [Conflict](docs/Conflict.md)
 - [ControllerUrl](docs/ControllerUrl.md)
 - [CountryProfileResponse](docs/CountryProfileResponse.md)
 - [CredCredentialSetResponse](docs/CredCredentialSetResponse.md)
 - [CredDataResponse](docs/CredDataResponse.md)
 - [CredPasswordComplexityResponse](docs/CredPasswordComplexityResponse.md)
 - [CredPasswordResponse](docs/CredPasswordResponse.md)
 - [CredSetAccessedUrlDataResponse](docs/CredSetAccessedUrlDataResponse.md)
 - [CredSetDataResponse](docs/CredSetDataResponse.md)
 - [CredSetStatisticsResponse](docs/CredSetStatisticsResponse.md)
 - [CredStatisticsResponse](docs/CredStatisticsResponse.md)
 - [CredentialOccurrenceCredResponse](docs/CredentialOccurrenceCredResponse.md)
 - [CredentialOccurrenceDataResponse](docs/CredentialOccurrenceDataResponse.md)
 - [CredentialSource](docs/CredentialSource.md)
 - [CveSource](docs/CveSource.md)
 - [Cvss](docs/Cvss.md)
 - [DataLeakSiteFileListingUrl](docs/DataLeakSiteFileListingUrl.md)
 - [DataLeakSitePost1](docs/DataLeakSitePost1.md)
 - [DataLeakSitePostItem](docs/DataLeakSitePostItem.md)
 - [DataLeakSitePostThread](docs/DataLeakSitePostThread.md)
 - [DataLeakSitePostWebsite](docs/DataLeakSitePostWebsite.md)
 - [DataLeakSitePostsStreamingPage](docs/DataLeakSitePostsStreamingPage.md)
 - [Encryption](docs/Encryption.md)
 - [Entities](docs/Entities.md)
 - [EntityItem](docs/EntityItem.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseGirs](docs/ErrorResponseGirs.md)
 - [EventController](docs/EventController.md)
 - [EventData](docs/EventData.md)
 - [EventTag](docs/EventTag.md)
 - [EventsStream](docs/EventsStream.md)
 - [ExploitStatus](docs/ExploitStatus.md)
 - [File](docs/File.md)
 - [FintelReportSubType](docs/FintelReportSubType.md)
 - [FintelReportsResponseStream](docs/FintelReportsResponseStream.md)
 - [FintelResponse](docs/FintelResponse.md)
 - [Forbidden](docs/Forbidden.md)
 - [ForumsPostsStreamingPage](docs/ForumsPostsStreamingPage.md)
 - [ForumsPrivateMessagesStreamingPage](docs/ForumsPrivateMessagesStreamingPage.md)
 - [ForumsResponse1](docs/ForumsResponse1.md)
 - [GIR](docs/GIR.md)
 - [GeoIp](docs/GeoIp.md)
 - [GeopolReportDetailsResponse](docs/GeopolReportDetailsResponse.md)
 - [GeopolReportSubType](docs/GeopolReportSubType.md)
 - [GeopolReportsResponseStream](docs/GeopolReportsResponseStream.md)
 - [GetCredOccurrenceResponse](docs/GetCredOccurrenceResponse.md)
 - [GetCredOccurrenceResponseStream](docs/GetCredOccurrenceResponseStream.md)
 - [GetCredResponse](docs/GetCredResponse.md)
 - [GetCredResponseStream](docs/GetCredResponseStream.md)
 - [GetCredSetAccessedUrlResponse](docs/GetCredSetAccessedUrlResponse.md)
 - [GetCredSetAccessedUrlResponseStream](docs/GetCredSetAccessedUrlResponseStream.md)
 - [GetCredSetResponse](docs/GetCredSetResponse.md)
 - [GetCredSetResponseStream](docs/GetCredSetResponseStream.md)
 - [GirTree](docs/GirTree.md)
 - [GirsResponse](docs/GirsResponse.md)
 - [GirsTreeResponse](docs/GirsTreeResponse.md)
 - [Highlight](docs/Highlight.md)
 - [IndicatorData](docs/IndicatorData.md)
 - [IndicatorsStream](docs/IndicatorsStream.md)
 - [Industries](docs/Industries.md)
 - [InfoReportResponse](docs/InfoReportResponse.md)
 - [InfoReportsResponseStream](docs/InfoReportsResponseStream.md)
 - [InfoStealerResponseOption](docs/InfoStealerResponseOption.md)
 - [InfoStealerResponseSet](docs/InfoStealerResponseSet.md)
 - [IntegrationsEvent](docs/IntegrationsEvent.md)
 - [IntegrationsIndicator](docs/IntegrationsIndicator.md)
 - [IntelligenceEstimateResponse](docs/IntelligenceEstimateResponse.md)
 - [InterestLevel](docs/InterestLevel.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [Ipv4](docs/Ipv4.md)
 - [IspData](docs/IspData.md)
 - [KillChainPhase](docs/KillChainPhase.md)
 - [Link](docs/Link.md)
 - [Link1](docs/Link1.md)
 - [Links](docs/Links.md)
 - [Location](docs/Location.md)
 - [Malware](docs/Malware.md)
 - [MalwareFamily](docs/MalwareFamily.md)
 - [MalwareReportResponse](docs/MalwareReportResponse.md)
 - [MalwareReportsResponseStream](docs/MalwareReportsResponseStream.md)
 - [Motivation](docs/Motivation.md)
 - [NotFound](docs/NotFound.md)
 - [PatchStatus](docs/PatchStatus.md)
 - [Poc](docs/Poc.md)
 - [PostDetails1](docs/PostDetails1.md)
 - [PostResponse1](docs/PostResponse1.md)
 - [PrivateMessageDetails1](docs/PrivateMessageDetails1.md)
 - [PrivateMessageResponse1](docs/PrivateMessageResponse1.md)
 - [ProcessingStatus](docs/ProcessingStatus.md)
 - [RecipientDomain](docs/RecipientDomain.md)
 - [Redirect](docs/Redirect.md)
 - [ReportAttachment](docs/ReportAttachment.md)
 - [ReportContent](docs/ReportContent.md)
 - [ReportLocation](docs/ReportLocation.md)
 - [ReportResponseStream](docs/ReportResponseStream.md)
 - [ReportType](docs/ReportType.md)
 - [ReportingStatus](docs/ReportingStatus.md)
 - [ReportsVictimResponse](docs/ReportsVictimResponse.md)
 - [Revocation](docs/Revocation.md)
 - [RiskLevel](docs/RiskLevel.md)
 - [RoomStream](docs/RoomStream.md)
 - [SecurityAssessment](docs/SecurityAssessment.md)
 - [ServerStream](docs/ServerStream.md)
 - [Settings](docs/Settings.md)
 - [SignificantActivity](docs/SignificantActivity.md)
 - [SimplifiedMalwareProfile](docs/SimplifiedMalwareProfile.md)
 - [SourcesLinks](docs/SourcesLinks.md)
 - [SourcesResponse](docs/SourcesResponse.md)
 - [SpotReportResponse](docs/SpotReportResponse.md)
 - [SpotReportsResponseStream](docs/SpotReportsResponseStream.md)
 - [SubForumResponse1](docs/SubForumResponse1.md)
 - [Template](docs/Template.md)
 - [TensionPointResponse](docs/TensionPointResponse.md)
 - [ThreadResponse1](docs/ThreadResponse1.md)
 - [Threat](docs/Threat.md)
 - [ThreatData](docs/ThreatData.md)
 - [ThreatInfo](docs/ThreatInfo.md)
 - [ThreatRating](docs/ThreatRating.md)
 - [TranslationStatus](docs/TranslationStatus.md)
 - [Trigger](docs/Trigger.md)
 - [Unauthorized](docs/Unauthorized.md)
 - [VictimResponse](docs/VictimResponse.md)
 - [VulnerabilitiesReportDetailsResponse](docs/VulnerabilitiesReportDetailsResponse.md)
 - [VulnerabilitiesReportDetailsResponseStream](docs/VulnerabilitiesReportDetailsResponseStream.md)
 - [VulnerabilitiesReportsResponseStream](docs/VulnerabilitiesReportsResponseStream.md)
 - [VulnerabilityStatus](docs/VulnerabilityStatus.md)
 - [YaraData](docs/YaraData.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


## Author

<a href="mailto:support@intel471.com">Intel 471 Inc.</a>