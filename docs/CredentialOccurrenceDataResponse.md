# CredentialOccurrenceDataResponse

Credential occurrence with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** | Credential occurrence file path. | [optional] 
**accessed_url** | **str** | Accessed URL. | [optional] 
**credential** | [**CredentialOccurrenceCredResponse**](CredentialOccurrenceCredResponse.md) |  | [optional] 
**credential_set** | [**CredCredentialSetResponse**](CredCredentialSetResponse.md) |  | [optional] 
**info_stealer** | [**InfoStealerResponseOption**](InfoStealerResponseOption.md) |  | 
**software_name** | **str** | Name of the software. | [optional] 
**credential_type** | **str** | Type of the credential set this credential belongs to. | [optional] 

## Example

```python
from verity471.models.credential_occurrence_data_response import CredentialOccurrenceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialOccurrenceDataResponse from a JSON string
credential_occurrence_data_response_instance = CredentialOccurrenceDataResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialOccurrenceDataResponse.to_json())

# convert the object into a dict
credential_occurrence_data_response_dict = credential_occurrence_data_response_instance.to_dict()
# create an instance of CredentialOccurrenceDataResponse from a dict
credential_occurrence_data_response_from_dict = CredentialOccurrenceDataResponse.from_dict(credential_occurrence_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


