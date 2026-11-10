# DocumentBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Extra notes from the listing | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**available_images** | **str** | Which document images exist | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**checked_ts** | **datetime** | Last check time stated by the listing | [optional] 
**city** | **str** | City | [optional] 
**company_address** | **str** | Company address | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**date_of_birth_available** | **bool** | Whether the date of birth is included | [optional] 
**date_of_birth_year** | **int** | Year of birth, four digits (e.g. 1985). The listing gives the year only, not a full date | [optional] 
**document_type** | **str** | Document kind (DL, passport, …). | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**driving_license_available** | **bool** | Whether a driving license is included | [optional] 
**employer_identification_number** | **str** | US Employer Identification Number (EIN) of the company | [optional] 
**expiration_date** | **str** | Document expiry date as given by the listing, not normalised (e.g. 10.06.2025) | [optional] 
**expiration_year** | **int** | Year the document expires, four digits. The listing gives the year only, not a full date | [optional] 
**first_name** | **str** | First name | [optional] 
**gender** | **str** | Gender of the person the data belongs to | [optional] 
**last_order** | **str** | Last order as given by the listing: an ISO date on some listings, free text (date, amount, words) on others | [optional] 
**mother_maiden_name_available** | **bool** | Whether the mother&#39;s maiden name is included | [optional] 
**payment_ts** | **datetime** | Payment/transaction timestamp | [optional] 
**points** | **str** | Points balance given by the listing (rewards, credits) | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**state** | **str** | State or region | [optional] 
**year** | **int** | Year stated on the listing, four digits | [optional] 

## Example

```python
from verity471.models.document_basic_info import DocumentBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBasicInfo from a JSON string
document_basic_info_instance = DocumentBasicInfo.from_json(json)
# print the JSON string representation of the object
print(DocumentBasicInfo.to_json())

# convert the object into a dict
document_basic_info_dict = document_basic_info_instance.to_dict()
# create an instance of DocumentBasicInfo from a dict
document_basic_info_from_dict = DocumentBasicInfo.from_dict(document_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


