# CredStatisticsResponse

Statistics regarding returned objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessed_urls_count** | **int** | Number of accessed URLs. | [optional] 

## Example

```python
from verity471.models.cred_statistics_response import CredStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredStatisticsResponse from a JSON string
cred_statistics_response_instance = CredStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(CredStatisticsResponse.to_json())

# convert the object into a dict
cred_statistics_response_dict = cred_statistics_response_instance.to_dict()
# create an instance of CredStatisticsResponse from a dict
cred_statistics_response_from_dict = CredStatisticsResponse.from_dict(cred_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


