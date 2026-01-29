# CredPasswordResponse

Credential password details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**CredPasswordComplexityResponse**](CredPasswordComplexityResponse.md) |  | [optional] 
**strength** | **str** | Password strength. Allowed values: excellent, strong, medium, weak, poor, not_provided. | [optional] 
**id** | **str** | ID of the password. | [optional] 
**password_plain** | **str** | Password plain text. | [optional] 

## Example

```python
from verity471.models.cred_password_response import CredPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredPasswordResponse from a JSON string
cred_password_response_instance = CredPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(CredPasswordResponse.to_json())

# convert the object into a dict
cred_password_response_dict = cred_password_response_instance.to_dict()
# create an instance of CredPasswordResponse from a dict
cred_password_response_from_dict = CredPasswordResponse.from_dict(cred_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


