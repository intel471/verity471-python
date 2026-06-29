# GetCredSetAccessedDomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**ActivityResponse**](ActivityResponse.md) |  | 
**classification** | [**ClassificationResponse**](ClassificationResponse.md) |  | [optional] 
**data** | [**CredSetAccessedDomainDataResponse**](CredSetAccessedDomainDataResponse.md) |  | 
**id** | **str** | Unique credential set accessed domain identifier. | 
**last_updated_ts** | **str** | Credential set accessed domain last modification date. | 

## Example

```python
from verity471.models.get_cred_set_accessed_domain_response import GetCredSetAccessedDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetAccessedDomainResponse from a JSON string
get_cred_set_accessed_domain_response_instance = GetCredSetAccessedDomainResponse.from_json(json)
# print the JSON string representation of the object
print(GetCredSetAccessedDomainResponse.to_json())

# convert the object into a dict
get_cred_set_accessed_domain_response_dict = get_cred_set_accessed_domain_response_instance.to_dict()
# create an instance of GetCredSetAccessedDomainResponse from a dict
get_cred_set_accessed_domain_response_from_dict = GetCredSetAccessedDomainResponse.from_dict(get_cred_set_accessed_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


