# GeopolReportDetailsResponse

Minimal schema for Geopolitical report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_event** | **bool** | Report related active event | [optional] 
**attachments** | [**List[ReportAttachment]**](ReportAttachment.md) | List of attachments related to the report | [optional] 
**body** | **str** | Main content body of the report | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**country_profiles** | [**List[CountryProfileResponse]**](CountryProfileResponse.md) | Report related country profiles | [optional] 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**derived_entities** | [**List[Entities]**](Entities.md) | List of entities derived from the report | [optional] 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**id** | **str** | Unique identifier of the report | 
**information_ts** | **str** | Timestamp of information date | 
**intelligence_estimate** | [**IntelligenceEstimateResponse**](IntelligenceEstimateResponse.md) |  | [optional] 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | [optional] 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 
**last_updated_ts** | **str** | Timestamp of last report update | 
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**locations** | [**List[ReportLocation]**](ReportLocation.md) | List of locations related to the report | [optional] 
**regional_tension_points** | [**List[TensionPointResponse]**](TensionPointResponse.md) | Report related tension points | [optional] 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports connected to this report | [optional] 
**released_ts** | **str** | Timestamp when the report was published last time | 
**significant_activity** | [**SignificantActivity**](SignificantActivity.md) |  | [optional] 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**sub_type** | [**GeopolReportSubType**](GeopolReportSubType.md) |  | [optional] 
**title** | **str** | Title of the report | 
**type** | **str** | Type of the report | 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 

## Example

```python
from verity471.models.geopol_report_details_response import GeopolReportDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeopolReportDetailsResponse from a JSON string
geopol_report_details_response_instance = GeopolReportDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GeopolReportDetailsResponse.to_json())

# convert the object into a dict
geopol_report_details_response_dict = geopol_report_details_response_instance.to_dict()
# create an instance of GeopolReportDetailsResponse from a dict
geopol_report_details_response_from_dict = GeopolReportDetailsResponse.from_dict(geopol_report_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


