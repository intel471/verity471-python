# ShippingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **List[str]** | Where the vendor ships to (e.g. Worldwide, United States) | [optional] 
**options** | **List[str]** | Shipping options with price and delivery time, as free text | [optional] 
**origin** | **str** | Ship-from location. | [optional] 
**time** | **str** | Delivery time as given by the listing (e.g. 1 Hours, 0 days, 1 hours) | [optional] 
**type** | **str** | Delivery method (e.g. Normal, COORDINATED, Send Code) | [optional] 

## Example

```python
from verity471.models.shipping_info import ShippingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingInfo from a JSON string
shipping_info_instance = ShippingInfo.from_json(json)
# print the JSON string representation of the object
print(ShippingInfo.to_json())

# convert the object into a dict
shipping_info_dict = shipping_info_instance.to_dict()
# create an instance of ShippingInfo from a dict
shipping_info_from_dict = ShippingInfo.from_dict(shipping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


