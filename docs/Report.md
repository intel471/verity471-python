# Report


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_ts** | **datetime** | Timestamp when the report was created (ISO 8601) | 
**id** | **str** | Unique identifier of the report | 
**information_ts** | **datetime** | Timestamp of the information in the report (ISO 8601) | 
**last_updated_ts** | **datetime** | Timestamp when the report was last updated (ISO 8601) | 
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**released_ts** | **datetime** | Timestamp when the report was released (ISO 8601) | 
**sub_type** | **str** | Fintel or Geopol report subtype | [optional] 
**type** | [**ReportType**](ReportType.md) |  | 

## Example

```python
from verity471.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print(Report.to_json())

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_from_dict = Report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


