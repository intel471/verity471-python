# RoomStream

Chat room entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**channel_id** | **str** | Chat room channel id | 
**description** | **str** | Chat room description | [optional] 
**id** | **str** | Chat room id | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | [optional] 
**message_count** | **int** | Number of messages in the room | 
**name** | **str** | Chat room name | 
**usernames** | **List[str]** | Chat room usernames | [optional] 

## Example

```python
from verity471.models.room_stream import RoomStream

# TODO update the JSON string below
json = "{}"
# create an instance of RoomStream from a JSON string
room_stream_instance = RoomStream.from_json(json)
# print the JSON string representation of the object
print(RoomStream.to_json())

# convert the object into a dict
room_stream_dict = room_stream_instance.to_dict()
# create an instance of RoomStream from a dict
room_stream_from_dict = RoomStream.from_dict(room_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


