# DrugDetails

Fields of a `drug` product; set only when `kind` is `drug`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**DrugBasicInfo**](DrugBasicInfo.md) |  | [optional] 
**policy** | [**PolicyInfo**](PolicyInfo.md) |  | [optional] 
**quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**rating** | [**RatingOverall**](RatingOverall.md) |  | [optional] 
**shipping** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 

## Example

```python
from verity471.models.drug_details import DrugDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DrugDetails from a JSON string
drug_details_instance = DrugDetails.from_json(json)
# print the JSON string representation of the object
print(DrugDetails.to_json())

# convert the object into a dict
drug_details_dict = drug_details_instance.to_dict()
# create an instance of DrugDetails from a dict
drug_details_from_dict = DrugDetails.from_dict(drug_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


