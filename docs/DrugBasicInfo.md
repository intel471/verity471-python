# DrugBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_buying_options** | **List[str]** | Tiered bulk prices: quantity with total and per-unit price | [optional] 
**escrow_available** | **bool** | Whether escrow is offered. | [optional] 
**escrow_info** | **str** | Escrow terms | [optional] 
**link** | **str** | URL to the listing on the market. | [optional] 
**origin_country** | **str** | Country of origin for goods/data. | [optional] 
**payment_method** | **str** | Accepted payment method(s). | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**short_description** | **str** | Short title or teaser. | [optional] 

## Example

```python
from verity471.models.drug_basic_info import DrugBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DrugBasicInfo from a JSON string
drug_basic_info_instance = DrugBasicInfo.from_json(json)
# print the JSON string representation of the object
print(DrugBasicInfo.to_json())

# convert the object into a dict
drug_basic_info_dict = drug_basic_info_instance.to_dict()
# create an instance of DrugBasicInfo from a dict
drug_basic_info_from_dict = DrugBasicInfo.from_dict(drug_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


