# CardDetails

Fields of a `card` product; set only when `kind` is `card`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_info** | [**AvailableInfo**](AvailableInfo.md) |  | [optional] 
**basic_info** | [**CardBasicInfo**](CardBasicInfo.md) |  | [optional] 
**cc** | [**CreditCard**](CreditCard.md) |  | [optional] 
**sales_price** | [**List[PriceEntry]**](PriceEntry.md) | Reduced (sale) price, one entry per currency the listing gives | [optional] 
**victim** | [**VictimInfo**](VictimInfo.md) |  | [optional] 

## Example

```python
from verity471.models.card_details import CardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CardDetails from a JSON string
card_details_instance = CardDetails.from_json(json)
# print the JSON string representation of the object
print(CardDetails.to_json())

# convert the object into a dict
card_details_dict = card_details_instance.to_dict()
# create an instance of CardDetails from a dict
card_details_from_dict = CardDetails.from_dict(card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


