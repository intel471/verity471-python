# EmbeddedWatcherGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** |  | 
**is_global** | **bool** |  | 
**is_subscribed** | **bool** |  | 
**name** | **str** |  | 
**organisation_id** | **str** |  | 
**owner_user_id** | **str** |  | 
**sharing_settings** | [**List[ShareSettingsResponse]**](ShareSettingsResponse.md) |  | [optional] 
**subscription_type** | [**SubscriptionType**](SubscriptionType.md) |  | [optional] 

## Example

```python
from verity471.models.embedded_watcher_group_response import EmbeddedWatcherGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWatcherGroupResponse from a JSON string
embedded_watcher_group_response_instance = EmbeddedWatcherGroupResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWatcherGroupResponse.to_json())

# convert the object into a dict
embedded_watcher_group_response_dict = embedded_watcher_group_response_instance.to_dict()
# create an instance of EmbeddedWatcherGroupResponse from a dict
embedded_watcher_group_response_from_dict = EmbeddedWatcherGroupResponse.from_dict(embedded_watcher_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


