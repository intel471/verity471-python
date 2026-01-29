# PrivateMessageDetails1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**AuthorActor1**](AuthorActor1.md) |  | [optional] 
**forum** | [**ForumsResponse1**](ForumsResponse1.md) |  | [optional] 
**private_message** | [**PrivateMessageResponse1**](PrivateMessageResponse1.md) |  | 
**recipient** | [**AuthorActor1**](AuthorActor1.md) |  | [optional] 

## Example

```python
from verity471.models.private_message_details1 import PrivateMessageDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageDetails1 from a JSON string
private_message_details1_instance = PrivateMessageDetails1.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageDetails1.to_json())

# convert the object into a dict
private_message_details1_dict = private_message_details1_instance.to_dict()
# create an instance of PrivateMessageDetails1 from a dict
private_message_details1_from_dict = PrivateMessageDetails1.from_dict(private_message_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


