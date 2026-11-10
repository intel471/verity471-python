# DigitalGoodBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_region** | **str** | Region where the product can be activated (e.g. Global, EU) | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**free_insurance_time** | **str** | Free replacement (insurance) period offered by the vendor (e.g. 15 Days) | [optional] 
**link** | **str** | URL to the listing on the market. | [optional] 
**origin_country** | **str** | Country of origin for goods/data. | [optional] 
**platform** | **str** | Platform the product is for | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**short_description** | **str** | Short title or teaser. | [optional] 
**works_on** | **str** | Devices or platforms the product works on (e.g. Windows, Android, PlayStation 5) | [optional] 

## Example

```python
from verity471.models.digital_good_basic_info import DigitalGoodBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DigitalGoodBasicInfo from a JSON string
digital_good_basic_info_instance = DigitalGoodBasicInfo.from_json(json)
# print the JSON string representation of the object
print(DigitalGoodBasicInfo.to_json())

# convert the object into a dict
digital_good_basic_info_dict = digital_good_basic_info_instance.to_dict()
# create an instance of DigitalGoodBasicInfo from a dict
digital_good_basic_info_from_dict = DigitalGoodBasicInfo.from_dict(digital_good_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


