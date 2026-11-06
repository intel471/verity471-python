# ProductMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_ts** | **datetime** | When was the product created on a market | [optional] 

## Example

```python
from verity471.models.product_meta import ProductMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMeta from a JSON string
product_meta_instance = ProductMeta.from_json(json)
# print the JSON string representation of the object
print(ProductMeta.to_json())

# convert the object into a dict
product_meta_dict = product_meta_instance.to_dict()
# create an instance of ProductMeta from a dict
product_meta_from_dict = ProductMeta.from_dict(product_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


