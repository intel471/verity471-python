# ResourceInfostealerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** | Browser the data was taken from, as reported by the source (e.g. chrome, edge, firefox) | [optional] 
**grabbed_ts** | **datetime** | When the infostealer grabbed the data | [optional] 

## Example

```python
from verity471.models.resource_infostealer_info import ResourceInfostealerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceInfostealerInfo from a JSON string
resource_infostealer_info_instance = ResourceInfostealerInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceInfostealerInfo.to_json())

# convert the object into a dict
resource_infostealer_info_dict = resource_infostealer_info_instance.to_dict()
# create an instance of ResourceInfostealerInfo from a dict
resource_infostealer_info_from_dict = ResourceInfostealerInfo.from_dict(resource_infostealer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


