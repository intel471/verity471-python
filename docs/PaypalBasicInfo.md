# PaypalBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**account_type** | **str** | Account class (e.g. PayPal personal). | [optional] 
**additional_info** | **str** | Extra notes from listing. | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**bank** | **str** | Bank name. | [optional] 
**bank_access_available** | **bool** | Online banking access included | [optional] 
**bank_account** | **str** | Linked bank account details as free text, usually masked | [optional] 
**bank_account_available** | **bool** | Bank account linked. | [optional] 
**checked_ts** | **datetime** | Last check time stated by the listing | [optional] 
**cookies_available** | **bool** | Whether browser cookies are included | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**credit_card_available** | **bool** | Linked CC available (PayPal). | [optional] 
**credit_cards** | **str** | Cards associated with shop listing | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**email_access_available** | **bool** | Whether access to the email account is included | [optional] 
**email_confirmed** | **bool** | Email confirmed flag. | [optional] 
**email_domain** | **str** | Email domain on account. | [optional] 
**is_verified** | **bool** | Verified account flag. | [optional] 
**last_order** | **str** | Last order as given by the listing: an ISO date on some listings, free text (date, amount, words) on others | [optional] 
**last_transaction** | **str** | Last transaction date as given by the listing, not normalised: usually three dash-separated numbers, rarely ISO | [optional] 
**points** | **str** | Points balance given by the listing (rewards, credits) | [optional] 
**state** | **str** | State or region | [optional] 
**status_available** | **bool** | Status info available. | [optional] 
**verified_attributes** | **str** | Verification details text. | [optional] 

## Example

```python
from verity471.models.paypal_basic_info import PaypalBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaypalBasicInfo from a JSON string
paypal_basic_info_instance = PaypalBasicInfo.from_json(json)
# print the JSON string representation of the object
print(PaypalBasicInfo.to_json())

# convert the object into a dict
paypal_basic_info_dict = paypal_basic_info_instance.to_dict()
# create an instance of PaypalBasicInfo from a dict
paypal_basic_info_from_dict = PaypalBasicInfo.from_dict(paypal_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


