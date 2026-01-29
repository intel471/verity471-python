# GetCredResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total credentials | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**credentials** | [**List[GetCredResponse]**](GetCredResponse.md) | The credentials | [optional] 

## Example

```python
from verity471.models.get_cred_response_stream import GetCredResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredResponseStream from a JSON string
get_cred_response_stream_instance = GetCredResponseStream.from_json(json)
# print the JSON string representation of the object
print(GetCredResponseStream.to_json())

# convert the object into a dict
get_cred_response_stream_dict = get_cred_response_stream_instance.to_dict()
# create an instance of GetCredResponseStream from a dict
get_cred_response_stream_from_dict = GetCredResponseStream.from_dict(get_cred_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


