# PrivateMessageResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | Conversation id | [optional] 
**creation_ts** | **str** | Publish date in ISO 8601 format | 
**id** | **str** | Unique id of private message | 
**message** | **str** | Original Message | 
**subject** | **str** | Message subject | [optional] 
**translated_message** | **str** | Contains translated message if available | [optional] 
**translated_subject** | **str** | Contains translated message subject if available | [optional] 
**translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 

## Example

```python
from verity471.models.private_message_response1 import PrivateMessageResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageResponse1 from a JSON string
private_message_response1_instance = PrivateMessageResponse1.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageResponse1.to_json())

# convert the object into a dict
private_message_response1_dict = private_message_response1_instance.to_dict()
# create an instance of PrivateMessageResponse1 from a dict
private_message_response1_from_dict = PrivateMessageResponse1.from_dict(private_message_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


