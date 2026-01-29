# GetCredSetAccessedUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique credential set accessed url identifier. | 
**data** | [**CredSetAccessedUrlDataResponse**](CredSetAccessedUrlDataResponse.md) |  | 
**classification** | [**ClassificationResponse**](ClassificationResponse.md) |  | [optional] 
**last_updated_ts** | **str** | Credential set accessed url last modification date. | 
**activity** | [**ActivityResponse**](ActivityResponse.md) |  | 

## Example

```python
from verity471.models.get_cred_set_accessed_url_response import GetCredSetAccessedUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetAccessedUrlResponse from a JSON string
get_cred_set_accessed_url_response_instance = GetCredSetAccessedUrlResponse.from_json(json)
# print the JSON string representation of the object
print(GetCredSetAccessedUrlResponse.to_json())

# convert the object into a dict
get_cred_set_accessed_url_response_dict = get_cred_set_accessed_url_response_instance.to_dict()
# create an instance of GetCredSetAccessedUrlResponse from a dict
get_cred_set_accessed_url_response_from_dict = GetCredSetAccessedUrlResponse.from_dict(get_cred_set_accessed_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


