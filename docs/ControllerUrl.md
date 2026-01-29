# ControllerUrl

Controller URL information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | &#x60;url&#x60; of a controller. | [optional] 

## Example

```python
from verity471.models.controller_url import ControllerUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerUrl from a JSON string
controller_url_instance = ControllerUrl.from_json(json)
# print the JSON string representation of the object
print(ControllerUrl.to_json())

# convert the object into a dict
controller_url_dict = controller_url_instance.to_dict()
# create an instance of ControllerUrl from a dict
controller_url_from_dict = ControllerUrl.from_dict(controller_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


