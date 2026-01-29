# GetCredOccurrenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique credential occurrence identifier. | 
**data** | [**CredentialOccurrenceDataResponse**](CredentialOccurrenceDataResponse.md) |  | 
**classification** | [**ClassificationResponse**](ClassificationResponse.md) |  | [optional] 
**last_updated_ts** | **str** | Credential occurrence last modification date. | 
**activity** | [**ActivityResponse**](ActivityResponse.md) |  | 

## Example

```python
from verity471.models.get_cred_occurrence_response import GetCredOccurrenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredOccurrenceResponse from a JSON string
get_cred_occurrence_response_instance = GetCredOccurrenceResponse.from_json(json)
# print the JSON string representation of the object
print(GetCredOccurrenceResponse.to_json())

# convert the object into a dict
get_cred_occurrence_response_dict = get_cred_occurrence_response_instance.to_dict()
# create an instance of GetCredOccurrenceResponse from a dict
get_cred_occurrence_response_from_dict = GetCredOccurrenceResponse.from_dict(get_cred_occurrence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


