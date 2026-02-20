# GetWatcherGroupResponseWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**watchers_groups** | [**List[GetWatcherGroupResponse]**](GetWatcherGroupResponse.md) |  | [optional] 

## Example

```python
from verity471.models.get_watcher_group_response_wrapper import GetWatcherGroupResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GetWatcherGroupResponseWrapper from a JSON string
get_watcher_group_response_wrapper_instance = GetWatcherGroupResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(GetWatcherGroupResponseWrapper.to_json())

# convert the object into a dict
get_watcher_group_response_wrapper_dict = get_watcher_group_response_wrapper_instance.to_dict()
# create an instance of GetWatcherGroupResponseWrapper from a dict
get_watcher_group_response_wrapper_from_dict = GetWatcherGroupResponseWrapper.from_dict(get_watcher_group_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


