# GetWatcherResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**watcher_group_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**dsl_query** | **str** |  | 
**created_by** | **str** |  | 
**is_muted** | **bool** |  | 
**data_sets** | **List[str]** |  | [optional] 
**query_fields** | **List[str]** |  | [optional] 
**notification_settings** | [**List[NotificationSettingsResponse]**](NotificationSettingsResponse.md) |  | [optional] 
**updated_by** | **str** |  | [optional] 
**creation_ts** | **datetime** |  | 
**last_updated_ts** | **datetime** |  | 

## Example

```python
from verity471.models.get_watcher_response import GetWatcherResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWatcherResponse from a JSON string
get_watcher_response_instance = GetWatcherResponse.from_json(json)
# print the JSON string representation of the object
print(GetWatcherResponse.to_json())

# convert the object into a dict
get_watcher_response_dict = get_watcher_response_instance.to_dict()
# create an instance of GetWatcherResponse from a dict
get_watcher_response_from_dict = GetWatcherResponse.from_dict(get_watcher_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


