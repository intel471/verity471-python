# GetWatcherResponseWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**watchers** | [**List[GetWatcherResponse]**](GetWatcherResponse.md) |  | [optional] 

## Example

```python
from verity471.models.get_watcher_response_wrapper import GetWatcherResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GetWatcherResponseWrapper from a JSON string
get_watcher_response_wrapper_instance = GetWatcherResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(GetWatcherResponseWrapper.to_json())

# convert the object into a dict
get_watcher_response_wrapper_dict = get_watcher_response_wrapper_instance.to_dict()
# create an instance of GetWatcherResponseWrapper from a dict
get_watcher_response_wrapper_from_dict = GetWatcherResponseWrapper.from_dict(get_watcher_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


