# ShopDetails

Fields of a `shop` product; set only when `kind` is `shop`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**ShopBasicInfo**](ShopBasicInfo.md) |  | [optional] 

## Example

```python
from verity471.models.shop_details import ShopDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ShopDetails from a JSON string
shop_details_instance = ShopDetails.from_json(json)
# print the JSON string representation of the object
print(ShopDetails.to_json())

# convert the object into a dict
shop_details_dict = shop_details_instance.to_dict()
# create an instance of ShopDetails from a dict
shop_details_from_dict = ShopDetails.from_dict(shop_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


