# BankBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**bank_account** | **str** | Linked bank account details as free text, usually masked | [optional] 
**bank_account_available** | **bool** | Whether a linked bank account is included | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**checked_ts** | **datetime** | Last check time stated by the listing | [optional] 
**city** | **str** | City | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**credit_card_available** | **bool** | Whether a linked credit card is included | [optional] 
**credit_cards** | **str** | Cards associated with shop listing | [optional] 
**credit_score** | **int** | Credit score value | [optional] 
**date_of_birth_year** | **int** | Year of birth, four digits (e.g. 1985). The listing gives the year only, not a full date | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**driving_license_available** | **bool** | Whether a driving license is included | [optional] 
**email_domain** | **str** | Email domain of the account | [optional] 
**first_name** | **str** | First name | [optional] 
**last_order** | **str** | Last order as given by the listing: an ISO date on some listings, free text (date, amount, words) on others | [optional] 
**mother_maiden_name_available** | **bool** | Whether the mother&#39;s maiden name is included | [optional] 
**points** | **str** | Reward/credit points (e.g. bank listings). | [optional] 
**state** | **str** | State or region | [optional] 

## Example

```python
from verity471.models.bank_basic_info import BankBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BankBasicInfo from a JSON string
bank_basic_info_instance = BankBasicInfo.from_json(json)
# print the JSON string representation of the object
print(BankBasicInfo.to_json())

# convert the object into a dict
bank_basic_info_dict = bank_basic_info_instance.to_dict()
# create an instance of BankBasicInfo from a dict
bank_basic_info_from_dict = BankBasicInfo.from_dict(bank_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


