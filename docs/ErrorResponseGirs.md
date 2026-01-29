# ErrorResponseGirs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from verity471.models.error_response_girs import ErrorResponseGirs

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseGirs from a JSON string
error_response_girs_instance = ErrorResponseGirs.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseGirs.to_json())

# convert the object into a dict
error_response_girs_dict = error_response_girs_instance.to_dict()
# create an instance of ErrorResponseGirs from a dict
error_response_girs_from_dict = ErrorResponseGirs.from_dict(error_response_girs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


