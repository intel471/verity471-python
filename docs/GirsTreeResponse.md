# GirsTreeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of all GIRs returned. | 
**girs** | [**List[GirTree]**](GirTree.md) | A list of GIRs organized in a hierarchical tree structure. | 

## Example

```python
from verity471.models.girs_tree_response import GirsTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GirsTreeResponse from a JSON string
girs_tree_response_instance = GirsTreeResponse.from_json(json)
# print the JSON string representation of the object
print(GirsTreeResponse.to_json())

# convert the object into a dict
girs_tree_response_dict = girs_tree_response_instance.to_dict()
# create an instance of GirsTreeResponse from a dict
girs_tree_response_from_dict = GirsTreeResponse.from_dict(girs_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


