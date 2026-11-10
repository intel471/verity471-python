# ResourceOtherInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | **List[str]** | Kinds of data included (e.g. LoginData, HolderDetails) | [optional] 
**source** | **str** | Where in the log the data was collected (e.g. Saved Logins, Form Grabber) | [optional] 

## Example

```python
from verity471.models.resource_other_info import ResourceOtherInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceOtherInfo from a JSON string
resource_other_info_instance = ResourceOtherInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceOtherInfo.to_json())

# convert the object into a dict
resource_other_info_dict = resource_other_info_instance.to_dict()
# create an instance of ResourceOtherInfo from a dict
resource_other_info_from_dict = ResourceOtherInfo.from_dict(resource_other_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


