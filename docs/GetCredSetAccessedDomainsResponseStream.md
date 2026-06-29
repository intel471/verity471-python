# GetCredSetAccessedDomainsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_domains** | [**List[GetCredSetAccessedDomainResponse]**](GetCredSetAccessedDomainResponse.md) | Access domains | [optional] 
**count** | **int** | Number of total access domains | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 

## Example

```python
from verity471.models.get_cred_set_accessed_domains_response_stream import GetCredSetAccessedDomainsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetAccessedDomainsResponseStream from a JSON string
get_cred_set_accessed_domains_response_stream_instance = GetCredSetAccessedDomainsResponseStream.from_json(json)
# print the JSON string representation of the object
print(GetCredSetAccessedDomainsResponseStream.to_json())

# convert the object into a dict
get_cred_set_accessed_domains_response_stream_dict = get_cred_set_accessed_domains_response_stream_instance.to_dict()
# create an instance of GetCredSetAccessedDomainsResponseStream from a dict
get_cred_set_accessed_domains_response_stream_from_dict = GetCredSetAccessedDomainsResponseStream.from_dict(get_cred_set_accessed_domains_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


