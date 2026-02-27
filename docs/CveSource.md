# CveSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the source. | 
**type** | **str** | Type of the source. | 
**url** | **str** | URL of the source. | 

## Example

```python
from verity471.models.cve_source import CveSource

# TODO update the JSON string below
json = "{}"
# create an instance of CveSource from a JSON string
cve_source_instance = CveSource.from_json(json)
# print the JSON string representation of the object
print(CveSource.to_json())

# convert the object into a dict
cve_source_dict = cve_source_instance.to_dict()
# create an instance of CveSource from a dict
cve_source_from_dict = CveSource.from_dict(cve_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


