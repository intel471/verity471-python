# CredSetStatisticsResponse

Statistics regarding returned objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_count** | **int** | Number of credentials. | [optional] 
**credential_occurrences_count** | **int** | Number of credential occurrences. | [optional] 
**accessed_urls_count** | **int** | Number of accessed URLs. | [optional] 

## Example

```python
from verity471.models.cred_set_statistics_response import CredSetStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredSetStatisticsResponse from a JSON string
cred_set_statistics_response_instance = CredSetStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(CredSetStatisticsResponse.to_json())

# convert the object into a dict
cred_set_statistics_response_dict = cred_set_statistics_response_instance.to_dict()
# create an instance of CredSetStatisticsResponse from a dict
cred_set_statistics_response_from_dict = CredSetStatisticsResponse.from_dict(cred_set_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


