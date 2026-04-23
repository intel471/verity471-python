# SpotReportResponse

Minimal schema for Spot report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Main content body of the report. This field may be omitted in streaming responses when content exceeds the configured maximum size; fetch full report by ID if needed. | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**derived_entities** | [**List[Entities]**](Entities.md) | List of entities derived from related reports | [optional] 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**id** | **str** | Unique identifier of the report | 
**information_ts** | **str** | Timestamp of the information contained in the report | 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | [optional] 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 
**last_updated_ts** | **str** | Timestamp of last report update | 
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports | [optional] 
**released_ts** | **str** | Timestamp when the report was published last time | 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**title** | **str** | Title of the report | 
**type** | **str** | Type of the report | 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 

## Example

```python
from verity471.models.spot_report_response import SpotReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpotReportResponse from a JSON string
spot_report_response_instance = SpotReportResponse.from_json(json)
# print the JSON string representation of the object
print(SpotReportResponse.to_json())

# convert the object into a dict
spot_report_response_dict = spot_report_response_instance.to_dict()
# create an instance of SpotReportResponse from a dict
spot_report_response_from_dict = SpotReportResponse.from_dict(spot_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


