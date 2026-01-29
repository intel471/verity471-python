# GeopolReportDetailsResponse

Minimal schema for Geopolitical report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report | 
**type** | **str** | Type of the report | 
**sub_type** | [**GeopolReportSubType**](GeopolReportSubType.md) |  | [optional] 
**title** | **str** | Title of the report | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**released_ts** | **str** | Timestamp when the report was published last time | 
**last_updated_ts** | **str** | Timestamp of last report update | 
**information_ts** | **str** | Timestamp of information date | 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**links** | [**Links**](Links.md) |  | 
**body** | **str** | Main content body of the report | [optional] 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**locations** | [**List[ReportLocation]**](ReportLocation.md) | List of locations related to the report | [optional] 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | [optional] 
**attachments** | [**List[ReportAttachment]**](ReportAttachment.md) | List of attachments related to the report | [optional] 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports connected to this report | [optional] 
**country_profiles** | [**List[CountryProfileResponse]**](CountryProfileResponse.md) | Report related country profiles | [optional] 
**regional_tension_points** | [**List[TensionPointResponse]**](TensionPointResponse.md) | Report related tension points | [optional] 
**derived_entities** | [**List[Entities]**](Entities.md) | List of entities derived from the report | [optional] 
**active_event** | **bool** | Report related active event | [optional] 
**intelligence_estimate** | [**IntelligenceEstimateResponse**](IntelligenceEstimateResponse.md) |  | [optional] 
**significant_activity** | [**SignificantActivity**](SignificantActivity.md) |  | [optional] 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 

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


