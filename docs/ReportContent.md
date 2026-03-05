# ReportContent

Minimal schema for report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessment** | [**Assessment**](Assessment.md) |  | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**id** | **str** | Unique identifier of the related report | 
**information_ts** | **str** | Timestamp of the information contained in the report | [optional] 
**last_updated_ts** | **str** | Timestamp of last report update | 
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**released_ts** | **str** | Timestamp when the report was published last time | 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**sub_type** | **str** | Fintel or Geopol report subtype, e.g. ACTOR_PROFILE | [optional] 
**summary** | **str** | Report summary | [optional] 
**title** | **str** | Title of the related report | 
**type** | [**ReportType**](ReportType.md) |  | 

## Example

```python
from verity471.models.report_content import ReportContent

# TODO update the JSON string below
json = "{}"
# create an instance of ReportContent from a JSON string
report_content_instance = ReportContent.from_json(json)
# print the JSON string representation of the object
print(ReportContent.to_json())

# convert the object into a dict
report_content_dict = report_content_instance.to_dict()
# create an instance of ReportContent from a dict
report_content_from_dict = ReportContent.from_dict(report_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


