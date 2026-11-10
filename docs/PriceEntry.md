# PriceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency as labelled by the listing, e.g. USD, EUR, GBP, CAD, RUR, BTC, XMR (not strictly ISO 4217) | 
**value** | **float** | Amount in &#x60;currency&#x60; | 

## Example

```python
from verity471.models.price_entry import PriceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PriceEntry from a JSON string
price_entry_instance = PriceEntry.from_json(json)
# print the JSON string representation of the object
print(PriceEntry.to_json())

# convert the object into a dict
price_entry_dict = price_entry_instance.to_dict()
# create an instance of PriceEntry from a dict
price_entry_from_dict = PriceEntry.from_dict(price_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


