# Encryption

Encryption information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Type of &#x60;algorithm&#x60; used in the encryption. | [optional] 
**context** | **str** | The &#x60;context&#39; of the event. | [optional] 
**key** | **str** | The encryption &#x60;key&#x60;. | [optional] 

## Example

```python
from verity471.models.encryption import Encryption

# TODO update the JSON string below
json = "{}"
# create an instance of Encryption from a JSON string
encryption_instance = Encryption.from_json(json)
# print the JSON string representation of the object
print(Encryption.to_json())

# convert the object into a dict
encryption_dict = encryption_instance.to_dict()
# create an instance of Encryption from a dict
encryption_from_dict = Encryption.from_dict(encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


