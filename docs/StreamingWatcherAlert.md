# StreamingWatcherAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_ts** | **datetime** |  | 
**highlights** | [**List[HighlightWatchers]**](HighlightWatchers.md) |  | [optional] 
**id** | **int** |  | 
**is_trashed** | **bool** |  | 
**links** | [**Links**](Links.md) |  | 
**source_id** | **str** |  | 
**source_type** | **str** |  | 
**status** | **str** |  | 
**watcher_group_id** | **int** |  | 
**watcher_id** | **int** |  | 

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


