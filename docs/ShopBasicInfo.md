# ShopBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**account_type** | **str** | Account type given by the listing (e.g. personal, business) | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**bank_account** | **str** | Linked bank account details as free text, usually masked | [optional] 
**bank_account_available** | **bool** | Whether a linked bank account is included | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**checked_ts** | **datetime** | Last check time stated by the listing | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**credit_cards** | **str** | Cards associated with shop listing | [optional] 
**date_of_birth_year** | **int** | Year of birth, four digits (e.g. 1985). The listing gives the year only, not a full date | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**email_access_available** | **bool** | Email access included | [optional] 
**email_domain** | **str** | Email domain of the account | [optional] 
**gender** | **str** | Gender of the person the data belongs to | [optional] 
**last_order** | **str** | Last order as free text from the listing (date, amount, words). A listing carries either this or &#x60;last_order_ts&#x60;, never both | [optional] 
**last_order_ts** | **datetime** | Last order time, when the listing gives it as a timestamp. A listing carries either this or &#x60;last_order&#x60;, never both | [optional] 
**points** | **str** | Points balance given by the listing (rewards, credits) | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**shop_name** | **str** | Shop the account is for, usually its domain | [optional] 
**shop_type** | **str** | Shop category | [optional] 
**state** | **str** | State or region | [optional] 
**zip** | **str** | Postal/ZIP code | [optional] 

## Example

```python
from verity471.models.shop_basic_info import ShopBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShopBasicInfo from a JSON string
shop_basic_info_instance = ShopBasicInfo.from_json(json)
# print the JSON string representation of the object
print(ShopBasicInfo.to_json())

# convert the object into a dict
shop_basic_info_dict = shop_basic_info_instance.to_dict()
# create an instance of ShopBasicInfo from a dict
shop_basic_info_from_dict = ShopBasicInfo.from_dict(shop_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


