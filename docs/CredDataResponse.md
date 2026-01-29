# CredDataResponse

Credential with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_login** | **str** | Login of the credential. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**affiliations** | **List[str]** | Affiliation of the credential. Allowed values: my_employees, vip_emails, my_customers, third_parties. | [optional] 
**password** | [**CredPasswordResponse**](CredPasswordResponse.md) |  | [optional] 
**credential_sets** | [**List[CredCredentialSetResponse]**](CredCredentialSetResponse.md) | Credential sets associated with the credential. | [optional] 
**info_stealer** | [**InfoStealerResponseSet**](InfoStealerResponseSet.md) |  | 
**accessed_url** | **str** | Accessed URL of the credential. | [optional] 
**credential_set_type** | **List[str]** | Type(s) of the credential set(s) this credential belongs to. | [optional] 

## Example

```python
from verity471.models.cred_data_response import CredDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredDataResponse from a JSON string
cred_data_response_instance = CredDataResponse.from_json(json)
# print the JSON string representation of the object
print(CredDataResponse.to_json())

# convert the object into a dict
cred_data_response_dict = cred_data_response_instance.to_dict()
# create an instance of CredDataResponse from a dict
cred_data_response_from_dict = CredDataResponse.from_dict(cred_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


