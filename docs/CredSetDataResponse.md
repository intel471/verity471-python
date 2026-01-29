# CredSetDataResponse

Credential set with related objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential set. | [optional] 
**description** | **str** | Description of the credential set. | [optional] 
**record_count** | **int** | Number of records. | [optional] 
**disclosure_ts** | **datetime** | Date of disclosure. | [optional] 
**breach_ts** | **datetime** | Date of breach. | [optional] 
**collected_ts** | **datetime** | Date of collection. | [optional] 
**victims** | [**List[VictimResponse]**](VictimResponse.md) | List of purported victims. | [optional] 
**sources** | [**List[CredentialSource]**](CredentialSource.md) | List of sources. | [optional] 

## Example

```python
from verity471.models.cred_set_data_response import CredSetDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredSetDataResponse from a JSON string
cred_set_data_response_instance = CredSetDataResponse.from_json(json)
# print the JSON string representation of the object
print(CredSetDataResponse.to_json())

# convert the object into a dict
cred_set_data_response_dict = cred_set_data_response_instance.to_dict()
# create an instance of CredSetDataResponse from a dict
cred_set_data_response_from_dict = CredSetDataResponse.from_dict(cred_set_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


