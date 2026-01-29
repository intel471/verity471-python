# ReportLocation

Location information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Region name related to the report | 
**country** | **str** | Country name related to the report | [optional] 
**iso** | **str** | Country iso code related to the report | [optional] 
**link** | **str** | Linkage type or relation to the location | [optional] 

## Example

```python
from verity471.models.report_location import ReportLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLocation from a JSON string
report_location_instance = ReportLocation.from_json(json)
# print the JSON string representation of the object
print(ReportLocation.to_json())

# convert the object into a dict
report_location_dict = report_location_instance.to_dict()
# create an instance of ReportLocation from a dict
report_location_from_dict = ReportLocation.from_dict(report_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


