# StreamingWatcherAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**watcher_group_id** | **int** |  | 
**watcher_id** | **int** |  | 
**status** | **str** |  | 
**source_type** | **str** |  | 
**source_id** | **str** |  | 
**links** | [**Links**](Links.md) |  | 
**highlights** | [**List[HighlightWatchers]**](HighlightWatchers.md) |  | [optional] 
**creation_ts** | **datetime** |  | 
**is_trashed** | **bool** |  | 

## Example

```python
from verity471.models.streaming_watcher_alert import StreamingWatcherAlert

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingWatcherAlert from a JSON string
streaming_watcher_alert_instance = StreamingWatcherAlert.from_json(json)
# print the JSON string representation of the object
print(StreamingWatcherAlert.to_json())

# convert the object into a dict
streaming_watcher_alert_dict = streaming_watcher_alert_instance.to_dict()
# create an instance of StreamingWatcherAlert from a dict
streaming_watcher_alert_from_dict = StreamingWatcherAlert.from_dict(streaming_watcher_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


