# GetCredOccurrenceResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total credential occurrences | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**credential_occurrences** | [**List[GetCredOccurrenceResponse]**](GetCredOccurrenceResponse.md) | Credential occurrences | [optional] 

## Example

```python
from verity471.models.get_cred_occurrence_response_stream import GetCredOccurrenceResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredOccurrenceResponseStream from a JSON string
get_cred_occurrence_response_stream_instance = GetCredOccurrenceResponseStream.from_json(json)
# print the JSON string representation of the object
print(GetCredOccurrenceResponseStream.to_json())

# convert the object into a dict
get_cred_occurrence_response_stream_dict = get_cred_occurrence_response_stream_instance.to_dict()
# create an instance of GetCredOccurrenceResponseStream from a dict
get_cred_occurrence_response_stream_from_dict = GetCredOccurrenceResponseStream.from_dict(get_cred_occurrence_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


