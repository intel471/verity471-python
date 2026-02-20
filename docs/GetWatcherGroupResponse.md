# GetWatcherGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_by** | **str** |  | 
**owner_user_id** | **str** |  | 
**organisation_id** | **str** |  | 
**watcher_ids** | **List[int]** |  | [optional] 
**is_editable** | **bool** |  | 
**is_global** | **bool** |  | 
**is_subscribed** | **bool** |  | 
**is_muted** | **bool** |  | 
**notification_settings** | [**List[NotificationSettingsResponse]**](NotificationSettingsResponse.md) |  | [optional] 
**sharing_settings** | [**List[ShareSettingsResponse]**](ShareSettingsResponse.md) |  | [optional] 
**updated_by** | **str** |  | [optional] 
**creation_ts** | **datetime** |  | 
**last_updated_ts** | **datetime** |  | 

## Example

```python
from verity471.models.get_watcher_group_response import GetWatcherGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWatcherGroupResponse from a JSON string
get_watcher_group_response_instance = GetWatcherGroupResponse.from_json(json)
# print the JSON string representation of the object
print(GetWatcherGroupResponse.to_json())

# convert the object into a dict
get_watcher_group_response_dict = get_watcher_group_response_instance.to_dict()
# create an instance of GetWatcherGroupResponse from a dict
get_watcher_group_response_from_dict = GetWatcherGroupResponse.from_dict(get_watcher_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


