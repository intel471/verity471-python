# CredSetAccessedUrlDataResponse

Credential set accessed URL with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_url** | **str** | Accessed URL. | 
**accessed_domain** | **str** | Accessed domain. | [optional] 
**credential_set** | [**CredCredentialSetResponse**](CredCredentialSetResponse.md) |  | [optional] 

## Example

```python
from verity471.models.cred_set_accessed_url_data_response import CredSetAccessedUrlDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredSetAccessedUrlDataResponse from a JSON string
cred_set_accessed_url_data_response_instance = CredSetAccessedUrlDataResponse.from_json(json)
# print the JSON string representation of the object
print(CredSetAccessedUrlDataResponse.to_json())

# convert the object into a dict
cred_set_accessed_url_data_response_dict = cred_set_accessed_url_data_response_instance.to_dict()
# create an instance of CredSetAccessedUrlDataResponse from a dict
cred_set_accessed_url_data_response_from_dict = CredSetAccessedUrlDataResponse.from_dict(cred_set_accessed_url_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


