# EntityItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entity type as snake_case string | 
**value** | **str** | Entity value | 

## Example

```python
from verity471.models.entity_item import EntityItem

# TODO update the JSON string below
json = "{}"
# create an instance of EntityItem from a JSON string
entity_item_instance = EntityItem.from_json(json)
# print the JSON string representation of the object
print(EntityItem.to_json())

# convert the object into a dict
entity_item_dict = entity_item_instance.to_dict()
# create an instance of EntityItem from a dict
entity_item_from_dict = EntityItem.from_dict(entity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


