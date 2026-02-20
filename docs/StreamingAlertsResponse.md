# StreamingAlertsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**cursor_next** | **str** |  | [optional] 
**alerts** | [**List[StreamingWatcherAlert]**](StreamingWatcherAlert.md) |  | [optional] 

## Example

```python
from verity471.models.streaming_alerts_response import StreamingAlertsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingAlertsResponse from a JSON string
streaming_alerts_response_instance = StreamingAlertsResponse.from_json(json)
# print the JSON string representation of the object
print(StreamingAlertsResponse.to_json())

# convert the object into a dict
streaming_alerts_response_dict = streaming_alerts_response_instance.to_dict()
# create an instance of StreamingAlertsResponse from a dict
streaming_alerts_response_from_dict = StreamingAlertsResponse.from_dict(streaming_alerts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


