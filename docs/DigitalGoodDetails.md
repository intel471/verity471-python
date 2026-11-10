# DigitalGoodDetails

Fields of a `digital_good` product; set only when `kind` is `digital_good`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**DigitalGoodBasicInfo**](DigitalGoodBasicInfo.md) |  | [optional] 
**policy** | [**PolicyInfo**](PolicyInfo.md) |  | [optional] 
**quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**rating** | [**RatingOverall**](RatingOverall.md) |  | [optional] 
**shipping** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 

## Example

```python
from verity471.models.digital_good_details import DigitalGoodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DigitalGoodDetails from a JSON string
digital_good_details_instance = DigitalGoodDetails.from_json(json)
# print the JSON string representation of the object
print(DigitalGoodDetails.to_json())

# convert the object into a dict
digital_good_details_dict = digital_good_details_instance.to_dict()
# create an instance of DigitalGoodDetails from a dict
digital_good_details_from_dict = DigitalGoodDetails.from_dict(digital_good_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


