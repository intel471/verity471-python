# GetCredSetAccessedUrlResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total access urls | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**access_urls** | [**List[GetCredSetAccessedUrlResponse]**](GetCredSetAccessedUrlResponse.md) | Access urls | [optional] 

## Example

```python
from verity471.models.get_cred_set_accessed_url_response_stream import GetCredSetAccessedUrlResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetAccessedUrlResponseStream from a JSON string
get_cred_set_accessed_url_response_stream_instance = GetCredSetAccessedUrlResponseStream.from_json(json)
# print the JSON string representation of the object
print(GetCredSetAccessedUrlResponseStream.to_json())

# convert the object into a dict
get_cred_set_accessed_url_response_stream_dict = get_cred_set_accessed_url_response_stream_instance.to_dict()
# create an instance of GetCredSetAccessedUrlResponseStream from a dict
get_cred_set_accessed_url_response_stream_from_dict = GetCredSetAccessedUrlResponseStream.from_dict(get_cred_set_accessed_url_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


