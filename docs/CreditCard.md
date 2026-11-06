# CreditCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank** | **str** | Issuing bank. | [optional] 
**bin** | **str** | First digits of PAN (BIN). | [optional] 
**var_class** | **str** | Card class: CREDIT or DEBIT | [optional] 
**expire_date** | **str** | Card expiry as &#x60;MM/YY&#x60; | [optional] 
**level** | **str** | Card tier (Platinum, …). | [optional] 
**number** | **str** | Card number. | [optional] 
**payment_system** | **str** | Visa, MasterCard, etc. (unified). | [optional] 

## Example

```python
from verity471.models.credit_card import CreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCard from a JSON string
credit_card_instance = CreditCard.from_json(json)
# print the JSON string representation of the object
print(CreditCard.to_json())

# convert the object into a dict
credit_card_dict = credit_card_instance.to_dict()
# create an instance of CreditCard from a dict
credit_card_from_dict = CreditCard.from_dict(credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


