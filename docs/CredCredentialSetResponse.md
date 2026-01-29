# CredCredentialSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique credential set identifier. | [optional] 
**name** | **str** | Name of the credential set. | [optional] 

## Example

```python
from verity471.models.cred_credential_set_response import CredCredentialSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredCredentialSetResponse from a JSON string
cred_credential_set_response_instance = CredCredentialSetResponse.from_json(json)
# print the JSON string representation of the object
print(CredCredentialSetResponse.to_json())

# convert the object into a dict
cred_credential_set_response_dict = cred_credential_set_response_instance.to_dict()
# create an instance of CredCredentialSetResponse from a dict
cred_credential_set_response_from_dict = CredCredentialSetResponse.from_dict(cred_credential_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


