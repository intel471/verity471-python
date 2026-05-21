# GetCredSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**ActivityResponse**](ActivityResponse.md) |  | 
**classification** | [**ClassificationResponse**](ClassificationResponse.md) |  | [optional] 
**data** | [**CredSetDataResponse**](CredSetDataResponse.md) |  | 
**id** | **str** | Unique credential set identifier. | 
**last_updated_ts** | **str** | Credential set last modification date. | 
**statistics** | [**CredSetStatisticsResponse**](CredSetStatisticsResponse.md) |  | [optional] 

## Example

```python
from verity471.models.get_cred_set_response import GetCredSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredSetResponse from a JSON string
get_cred_set_response_instance = GetCredSetResponse.from_json(json)
# print the JSON string representation of the object
print(GetCredSetResponse.to_json())

# convert the object into a dict
get_cred_set_response_dict = get_cred_set_response_instance.to_dict()
# create an instance of GetCredSetResponse from a dict
get_cred_set_response_from_dict = GetCredSetResponse.from_dict(get_cred_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


