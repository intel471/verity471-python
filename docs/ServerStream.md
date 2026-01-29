# ServerStream

Chat server entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Chat server id | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | [optional] 
**name** | **str** | Chat server name | 
**type** | **str** | Chat server type | 

## Example

```python
from verity471.models.server_stream import ServerStream

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStream from a JSON string
server_stream_instance = ServerStream.from_json(json)
# print the JSON string representation of the object
print(ServerStream.to_json())

# convert the object into a dict
server_stream_dict = server_stream_instance.to_dict()
# create an instance of ServerStream from a dict
server_stream_from_dict = ServerStream.from_dict(server_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


