# CredSetAccessedDomainDataResponse

Credential set accessed Domain with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_domain** | **str** | Accessed domain. | 
**credential_set** | [**CredCredentialSetResponse**](CredCredentialSetResponse.md) |  | [optional] 

## Example

```python
from verity471.models.cred_set_accessed_domain_data_response import CredSetAccessedDomainDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredSetAccessedDomainDataResponse from a JSON string
cred_set_accessed_domain_data_response_instance = CredSetAccessedDomainDataResponse.from_json(json)
# print the JSON string representation of the object
print(CredSetAccessedDomainDataResponse.to_json())

# convert the object into a dict
cred_set_accessed_domain_data_response_dict = cred_set_accessed_domain_data_response_instance.to_dict()
# create an instance of CredSetAccessedDomainDataResponse from a dict
cred_set_accessed_domain_data_response_from_dict = CredSetAccessedDomainDataResponse.from_dict(cred_set_accessed_domain_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


