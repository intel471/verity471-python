# PersonalInfoBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**account_number_available** | **bool** | Whether the bank account number is included | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**address_available** | **bool** | Whether the address is included | [optional] 
**age** | **int** |  | [optional] 
**background_check_available** | **bool** | Whether a background check is included | [optional] 
**background_report_available** | **bool** | Background report included | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**checked_ts** | **datetime** | Last check time stated by the listing | [optional] 
**city** | **str** | City | [optional] 
**company_name** | **str** | Company name | [optional] 
**company_type** | **str** | Company type/industry | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**credit_cards** | **str** | Payment cards included in the listing | [optional] 
**credit_record_available** | **bool** | Credit report included | [optional] 
**credit_score** | **int** | Credit score value. | [optional] 
**credit_score_available** | **bool** | Credit score included | [optional] 
**date_of_birth** | **str** | Date of birth as given by the listing, usually masked to the year (&#x60;YYYY/**/**&#x60;) | [optional] 
**date_of_birth_available** | **bool** | Whether the date of birth is included | [optional] 
**date_of_birth_year** | **int** | Year of birth, four digits (e.g. 1985). The listing gives the year only, not a full date | [optional] 
**domain** | **str** | Domain name | [optional] 
**driving_license_available** | **bool** | Driving license available | [optional] 
**driving_license_photo_available** | **bool** | License photo included | [optional] 
**driving_license_state** | **str** | License issuing state | [optional] 
**email_access_available** | **bool** | Whether access to the email account is included | [optional] 
**employer_name** | **str** | Employer name | [optional] 
**employment_type** | **str** | Employment type | [optional] 
**escrow_available** | **bool** | Whether escrow is offered. | [optional] 
**escrow_info** | **str** | Escrow terms | [optional] 
**first_name** | **str** | First name | [optional] 
**full_name** | **str** | Full name of the person, usually masked | [optional] 
**gender** | **str** | Victim Gender | [optional] 
**last_order** | **str** | Last order as given by the listing: an ISO date on some listings, free text (date, amount, words) on others | [optional] 
**link** | **str** | URL to the listing on the market. | [optional] 
**mother_maiden_name_available** | **bool** | MMN included | [optional] 
**phone_available** | **bool** | Whether a phone number is included | [optional] 
**points** | **str** | Points balance given by the listing (rewards, credits) | [optional] 
**principal_office_street** | **str** | Company street address | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**routing_number_available** | **bool** | Whether the bank routing number is included | [optional] 
**short_description** | **str** | Short title or teaser. | [optional] 
**social_insurance_number** | **str** | SIN (Canada), masked | [optional] 
**social_security_number** | **str** | SSN (US), masked | [optional] 
**social_security_number_available** | **bool** | Whether the SSN is included | [optional] 
**state** | **str** | State/region | [optional] 
**zip** | **str** | Postal/ZIP. | [optional] 

## Example

```python
from verity471.models.personal_info_basic_info import PersonalInfoBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalInfoBasicInfo from a JSON string
personal_info_basic_info_instance = PersonalInfoBasicInfo.from_json(json)
# print the JSON string representation of the object
print(PersonalInfoBasicInfo.to_json())

# convert the object into a dict
personal_info_basic_info_dict = personal_info_basic_info_instance.to_dict()
# create an instance of PersonalInfoBasicInfo from a dict
personal_info_basic_info_from_dict = PersonalInfoBasicInfo.from_dict(personal_info_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


