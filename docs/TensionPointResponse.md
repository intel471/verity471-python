# TensionPointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**information_ts** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from verity471.models.tension_point_response import TensionPointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TensionPointResponse from a JSON string
tension_point_response_instance = TensionPointResponse.from_json(json)
# print the JSON string representation of the object
print(TensionPointResponse.to_json())

# convert the object into a dict
tension_point_response_dict = tension_point_response_instance.to_dict()
# create an instance of TensionPointResponse from a dict
tension_point_response_from_dict = TensionPointResponse.from_dict(tension_point_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


