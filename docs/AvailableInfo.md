# AvailableInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_available** | **bool** | Address included. | [optional] 
**city_available** | **bool** | City included. | [optional] 
**cvv_available** | **bool** | CVV included. | [optional] 
**date_of_birth_available** | **bool** | DOB included. | [optional] 
**email_available** | **bool** | Email included. | [optional] 
**holder_name_available** | **bool** | Cardholder name included. | [optional] 
**ip_available** | **bool** | IP included. | [optional] 
**is_refundable** | **bool** | Refundable per market rules. | [optional] 
**mother_maiden_name_available** | **bool** | MMN included | [optional] 
**phone_available** | **bool** | Phone included. | [optional] 
**social_security_number_available** | **bool** | SSN included. | [optional] 
**zip_available** | **bool** | ZIP included. | [optional] 

## Example

```python
from verity471.models.available_info import AvailableInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableInfo from a JSON string
available_info_instance = AvailableInfo.from_json(json)
# print the JSON string representation of the object
print(AvailableInfo.to_json())

# convert the object into a dict
available_info_dict = available_info_instance.to_dict()
# create an instance of AvailableInfo from a dict
available_info_from_dict = AvailableInfo.from_dict(available_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


