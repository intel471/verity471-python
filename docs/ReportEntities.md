# ReportEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report | 
**type** | [**ReportType**](ReportType.md) |  | 
**sub_type** | **str** | Fintel or Geopol report subtype | [optional] 
**creation_ts** | **datetime** | Timestamp when the report was created (ISO 8601) | 
**last_updated_ts** | **datetime** | Timestamp when the report was last updated (ISO 8601) | 
**information_ts** | **datetime** | Timestamp of the information in the report (ISO 8601) | 
**released_ts** | **datetime** | Timestamp when the report was released (ISO 8601) | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from verity471.models.report_entities import ReportEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEntities from a JSON string
report_entities_instance = ReportEntities.from_json(json)
# print the JSON string representation of the object
print(ReportEntities.to_json())

# convert the object into a dict
report_entities_dict = report_entities_instance.to_dict()
# create an instance of ReportEntities from a dict
report_entities_from_dict = ReportEntities.from_dict(report_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


