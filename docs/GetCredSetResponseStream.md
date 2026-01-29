# GetCredSetResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total credential sets | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**credential_sets** | [**List[GetCredSetResponse]**](GetCredSetResponse.md) | Credential sets | [optional] 

## Example

```python
from verity471.models.get_cred_set_response_stream import GetCredSetResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetResponseStream from a JSON string
get_cred_set_response_stream_instance = GetCredSetResponseStream.from_json(json)
# print the JSON string representation of the object
print(GetCredSetResponseStream.to_json())

# convert the object into a dict
get_cred_set_response_stream_dict = get_cred_set_response_stream_instance.to_dict()
# create an instance of GetCredSetResponseStream from a dict
get_cred_set_response_stream_from_dict = GetCredSetResponseStream.from_dict(get_cred_set_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


