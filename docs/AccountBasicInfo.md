# AccountBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**activation_region** | **str** | Region where the product can be activated (e.g. Global, EU) | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**available_games** | **List[str]** | Games available on the account | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**email_domain** | **str** | Email domain of the account | [optional] 
**free_insurance_time** | **str** | Free replacement (insurance) period offered by the vendor (e.g. 15 Days) | [optional] 
**game_statistics** | **List[str]** | Per-game statistics: game name with stats such as rank or PvP time | [optional] 
**in_game_items** | [**InGameItems**](InGameItems.md) |  | [optional] 
**last_activity_ts** | **datetime** | Last account/activity time (accounts). | [optional] 
**last_order** | **str** | Last order as given by the listing: an ISO date on some listings, free text (date, amount, words) on others | [optional] 
**link** | **str** | URL to the listing on the market. | [optional] 
**negative_points** | **List[str]** | Drawbacks listed by the vendor, as free text (e.g. Linked to PSN) | [optional] 
**origin_country** | **str** | Country of origin for goods/data. | [optional] 
**platform** | **str** | Platform the product is for | [optional] 
**points** | **str** | Points balance given by the listing (rewards, credits) | [optional] 
**positive_points** | **List[str]** | Selling points listed by the vendor, as free text (e.g. Access to email) | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**region** | **str** | Region the product is for (e.g. GLOBAL, EUROPE) | [optional] 
**registered_ts** | **datetime** | Account registration time. | [optional] 
**server** | **str** | Server given by the listing (e.g. a game or mail server) | [optional] 
**shop_name** | **str** | Shop the account is for, usually its domain | [optional] 
**shop_type** | **str** | Shop category | [optional] 
**short_description** | **str** | Short title or teaser. | [optional] 
**times_sold** | **int** | How many times this product has been sold | [optional] 
**works_on** | **str** | Devices or platforms the product works on (e.g. Windows, Android, PlayStation 5) | [optional] 
**zip** | **str** | Postal/ZIP code | [optional] 

## Example

```python
from verity471.models.account_basic_info import AccountBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBasicInfo from a JSON string
account_basic_info_instance = AccountBasicInfo.from_json(json)
# print the JSON string representation of the object
print(AccountBasicInfo.to_json())

# convert the object into a dict
account_basic_info_dict = account_basic_info_instance.to_dict()
# create an instance of AccountBasicInfo from a dict
account_basic_info_from_dict = AccountBasicInfo.from_dict(account_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


