# Quantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_from_vendor** | **int** | Qty from this vendor. | [optional] 
**available_on_market** | **float** | Can be fractional, e.g. a weight for drugs | [optional] 
**maximum_order** | **int** | Maximum units per order | [optional] 
**minimum_order** | **int** | Minimum units per order | [optional] 
**sold_from_vendor** | **int** | Sold by this vendor. | [optional] 
**stock** | **int** | Stock count. | [optional] 

## Example

```python
from verity471.models.quantity import Quantity

# TODO update the JSON string below
json = "{}"
# create an instance of Quantity from a JSON string
quantity_instance = Quantity.from_json(json)
# print the JSON string representation of the object
print(Quantity.to_json())

# convert the object into a dict
quantity_dict = quantity_instance.to_dict()
# create an instance of Quantity from a dict
quantity_from_dict = Quantity.from_dict(quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


