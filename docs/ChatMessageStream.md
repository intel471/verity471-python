# ChatMessageStream

Message entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentData]**](AttachmentData.md) | Message attachments and images | [optional] 
**author** | [**AuthorActor1**](AuthorActor1.md) |  | [optional] 
**creation_ts** | **str** | Timestamp when the message was published first time | 
**html** | **str** | Message text in html format | 
**id** | **str** | Unique id of message | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | [optional] 
**text** | **str** | Message text | 

## Example

```python
from verity471.models.chat_message_stream import ChatMessageStream

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageStream from a JSON string
chat_message_stream_instance = ChatMessageStream.from_json(json)
# print the JSON string representation of the object
print(ChatMessageStream.to_json())

# convert the object into a dict
chat_message_stream_dict = chat_message_stream_instance.to_dict()
# create an instance of ChatMessageStream from a dict
chat_message_stream_from_dict = ChatMessageStream.from_dict(chat_message_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


