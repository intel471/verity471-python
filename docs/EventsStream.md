# EventsStream

Stream of events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of events matching the query | [optional] 
**cursor_next** | **str** | Cursor for retrieving the next page of results | [optional] 
**events** | [**List[IntegrationsEvent]**](IntegrationsEvent.md) | List of events | [optional] 

## Example

```python
from verity471.models.events_stream import EventsStream

# TODO update the JSON string below
json = "{}"
# create an instance of EventsStream from a JSON string
events_stream_instance = EventsStream.from_json(json)
# print the JSON string representation of the object
print(EventsStream.to_json())

# convert the object into a dict
events_stream_dict = events_stream_instance.to_dict()
# create an instance of EventsStream from a dict
events_stream_from_dict = EventsStream.from_dict(events_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


