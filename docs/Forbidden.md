# Forbidden

Forbidden response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**timestamp** | **datetime** | Timestamp of the error | 

## Example

```python
from verity471.models.forbidden import Forbidden

# TODO update the JSON string below
json = "{}"
# create an instance of Forbidden from a JSON string
forbidden_instance = Forbidden.from_json(json)
# print the JSON string representation of the object
print(Forbidden.to_json())

# convert the object into a dict
forbidden_dict = forbidden_instance.to_dict()
# create an instance of Forbidden from a dict
forbidden_from_dict = Forbidden.from_dict(forbidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


