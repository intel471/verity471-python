# BreachAlertsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total reports | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**reports** | [**List[BreachAlertResponse]**](BreachAlertResponse.md) |  | [optional] 

## Example

```python
from verity471.models.breach_alerts_response_stream import BreachAlertsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of BreachAlertsResponseStream from a JSON string
breach_alerts_response_stream_instance = BreachAlertsResponseStream.from_json(json)
# print the JSON string representation of the object
print(BreachAlertsResponseStream.to_json())

# convert the object into a dict
breach_alerts_response_stream_dict = breach_alerts_response_stream_instance.to_dict()
# create an instance of BreachAlertsResponseStream from a dict
breach_alerts_response_stream_from_dict = BreachAlertsResponseStream.from_dict(breach_alerts_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


