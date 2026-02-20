# Isp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**autonomous_system** | **str** |  | [optional] 
**isp** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 

## Example

```python
from verity471.models.isp import Isp

# TODO update the JSON string below
json = "{}"
# create an instance of Isp from a JSON string
isp_instance = Isp.from_json(json)
# print the JSON string representation of the object
print(Isp.to_json())

# convert the object into a dict
isp_dict = isp_instance.to_dict()
# create an instance of Isp from a dict
isp_from_dict = Isp.from_dict(isp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


