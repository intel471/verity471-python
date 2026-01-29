# CredPasswordComplexityResponse

Details of the password's complexity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lowercase** | **int** | The number of lowercase letters in the password. | [optional] 
**uppercase** | **int** | The number of uppercase letters in the password. | [optional] 
**numbers** | **int** | The number of digits in the password. | [optional] 
**symbols** | **int** | The number of symbols in the password. | [optional] 
**punctuation_marks** | **int** | The number of punctuation marks in the password. | [optional] 
**separators** | **int** | The number of separators in the password. | [optional] 
**other** | **int** | The number of other characters in the password. | [optional] 
**length** | **int** | The length of the password. | [optional] 
**score** | **float** | The password score. | [optional] 
**weakness** | **float** | The password weakness. | [optional] 
**entropy** | **float** | The password entropy. | [optional] 

## Example

```python
from verity471.models.cred_password_complexity_response import CredPasswordComplexityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredPasswordComplexityResponse from a JSON string
cred_password_complexity_response_instance = CredPasswordComplexityResponse.from_json(json)
# print the JSON string representation of the object
print(CredPasswordComplexityResponse.to_json())

# convert the object into a dict
cred_password_complexity_response_dict = cred_password_complexity_response_instance.to_dict()
# create an instance of CredPasswordComplexityResponse from a dict
cred_password_complexity_response_from_dict = CredPasswordComplexityResponse.from_dict(cred_password_complexity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


