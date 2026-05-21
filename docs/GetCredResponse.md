# GetCredResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**ActivityResponse**](ActivityResponse.md) |  | 
**classification** | [**ClassificationResponse**](ClassificationResponse.md) |  | [optional] 
**data** | [**CredDataResponse**](CredDataResponse.md) |  | 
**id** | **str** | Unique credential identifier. | 
**last_updated_ts** | **str** | Credential last modification date. | 
**statistics** | [**CredStatisticsResponse**](CredStatisticsResponse.md) |  | [optional] 

## Example

```python
from verity471.models.get_cred_response import GetCredResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredResponse from a JSON string
get_cred_response_instance = GetCredResponse.from_json(json)
# print the JSON string representation of the object
print(GetCredResponse.to_json())

# convert the object into a dict
get_cred_response_dict = get_cred_response_instance.to_dict()
# create an instance of GetCredResponse from a dict
get_cred_response_from_dict = GetCredResponse.from_dict(get_cred_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


