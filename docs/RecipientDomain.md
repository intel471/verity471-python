# RecipientDomain

Recipient domain information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of recipient domains. | [optional] 
**domain** | **str** | Recipient domain. | [optional] 

## Example

```python
from verity471.models.recipient_domain import RecipientDomain

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDomain from a JSON string
recipient_domain_instance = RecipientDomain.from_json(json)
# print the JSON string representation of the object
print(RecipientDomain.to_json())

# convert the object into a dict
recipient_domain_dict = recipient_domain_instance.to_dict()
# create an instance of RecipientDomain from a dict
recipient_domain_from_dict = RecipientDomain.from_dict(recipient_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


