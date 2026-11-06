# ResourceProductInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_ts** | **datetime** | When the product this resource belongs to was last updated at the source | [optional] 

## Example

```python
from verity471.models.resource_product_info import ResourceProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceProductInfo from a JSON string
resource_product_info_instance = ResourceProductInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceProductInfo.to_json())

# convert the object into a dict
resource_product_info_dict = resource_product_info_instance.to_dict()
# create an instance of ResourceProductInfo from a dict
resource_product_info_from_dict = ResourceProductInfo.from_dict(resource_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


