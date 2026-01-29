# CredentialOccurrenceCredResponse

Sub-document containing credential information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique credential identifier. | 
**credential_login** | **str** | Login of the credential. | [optional] 
**credential_domain** | **str** | Domain of the credential. | [optional] 
**detection_domain** | **str** | Detection domain of the credential. | [optional] 
**affiliations** | **List[str]** | Affiliation of the credential. Allowed values: my_employees, vip_emails, my_customers, third_parties. | [optional] 
**password** | [**CredPasswordResponse**](CredPasswordResponse.md) |  | [optional] 

## Example

```python
from verity471.models.credential_occurrence_cred_response import CredentialOccurrenceCredResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceCredResponse from a JSON string
credential_occurrence_cred_response_instance = CredentialOccurrenceCredResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceCredResponse.to_json())

# convert the object into a dict
credential_occurrence_cred_response_dict = credential_occurrence_cred_response_instance.to_dict()
# create an instance of CredentialOccurrenceCredResponse from a dict
credential_occurrence_cred_response_from_dict = CredentialOccurrenceCredResponse.from_dict(credential_occurrence_cred_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


