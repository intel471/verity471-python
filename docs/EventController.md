# EventController

Controller information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**Ipv4**](Ipv4.md) | The &#x60;ipv4&#x60; of a controller | [optional] 
**url** | **str** | The &#x60;url&#x60; of a controller. | [optional] 

## Example

```python
from verity471.models.event_controller import EventController

# TODO update the JSON string below
json = "{}"
# create an instance of EventController from a JSON string
event_controller_instance = EventController.from_json(json)
# print the JSON string representation of the object
print(EventController.to_json())

# convert the object into a dict
event_controller_dict = event_controller_instance.to_dict()
# create an instance of EventController from a dict
event_controller_from_dict = EventController.from_dict(event_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


