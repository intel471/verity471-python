# ImServer

A messaging service that the actor is associated with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**service_type** | [**ChatServerType**](ChatServerType.md) |  | 

## Example

```python
from verity471.models.im_server import ImServer

# TODO update the JSON string below
json = "{}"
# create an instance of ImServer from a JSON string
im_server_instance = ImServer.from_json(json)
# print the JSON string representation of the object
print(ImServer.to_json())

# convert the object into a dict
im_server_dict = im_server_instance.to_dict()
# create an instance of ImServer from a dict
im_server_from_dict = ImServer.from_dict(im_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


