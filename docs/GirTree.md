# GirTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**children** | [**List[GirTree]**](GirTree.md) |  | [optional] 

## Example

```python
from verity471.models.gir_tree import GirTree

# TODO update the JSON string below
json = "{}"
# create an instance of GirTree from a JSON string
gir_tree_instance = GirTree.from_json(json)
# print the JSON string representation of the object
print(GirTree.to_json())

# convert the object into a dict
gir_tree_dict = gir_tree_instance.to_dict()
# create an instance of GirTree from a dict
gir_tree_from_dict = GirTree.from_dict(gir_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


