# LinksSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**title** | **str** | Title of the source | [optional] 
**type** | **str** | Type of the source | 

## Example

```python
from verity471.models.links_source import LinksSource

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSource from a JSON string
links_source_instance = LinksSource.from_json(json)
# print the JSON string representation of the object
print(LinksSource.to_json())

# convert the object into a dict
links_source_dict = links_source_instance.to_dict()
# create an instance of LinksSource from a dict
links_source_from_dict = LinksSource.from_dict(links_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


