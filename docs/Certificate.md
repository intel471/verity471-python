# Certificate

Certificate information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | Fingerprint of the certificate. | [optional] 
**issuer** | **str** | Issuer of the certificate. | [optional] 
**serial** | **str** | Serial number of the certificate. | [optional] 
**subject** | **str** | Subject of the certificate. | [optional] 
**valid_from** | **datetime** | Start of the certificate validity period. | [optional] 
**valid_to** | **datetime** | End of the certificate validity period. | [optional] 

## Example

```python
from verity471.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print(Certificate.to_json())

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_from_dict = Certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


