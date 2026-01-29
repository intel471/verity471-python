# ChatRoomMessageStream

Chats Message and room

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_room** | [**RoomStream**](RoomStream.md) |  | [optional] 
**message** | [**ChatMessageStream**](ChatMessageStream.md) |  | 
**server** | [**ServerStream**](ServerStream.md) |  | [optional] 

## Example

```python
from verity471.models.chat_room_message_stream import ChatRoomMessageStream

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRoomMessageStream from a JSON string
chat_room_message_stream_instance = ChatRoomMessageStream.from_json(json)
# print the JSON string representation of the object
print(ChatRoomMessageStream.to_json())

# convert the object into a dict
chat_room_message_stream_dict = chat_room_message_stream_instance.to_dict()
# create an instance of ChatRoomMessageStream from a dict
chat_room_message_stream_from_dict = ChatRoomMessageStream.from_dict(chat_room_message_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


