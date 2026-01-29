# Revocation

Revocation information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **bool** | Boolean value to indicate whether the entity is revoked | [optional] 

## Example

```python
from verity471.models.revocation import Revocation

# TODO update the JSON string below
json = "{}"
# create an instance of Revocation from a JSON string
revocation_instance = Revocation.from_json(json)
# print the JSON string representation of the object
print(Revocation.to_json())

# convert the object into a dict
revocation_dict = revocation_instance.to_dict()
# create an instance of Revocation from a dict
revocation_from_dict = Revocation.from_dict(revocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


