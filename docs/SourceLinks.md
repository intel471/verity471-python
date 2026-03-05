# SourceLinks

Available links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external** | [**SourceLink**](SourceLink.md) |  | [optional] 
**verity_api** | [**SourceLink**](SourceLink.md) |  | [optional] 
**verity_portal** | [**SourceLink**](SourceLink.md) |  | [optional] 

## Example

```python
from verity471.models.source_links import SourceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SourceLinks from a JSON string
source_links_instance = SourceLinks.from_json(json)
# print the JSON string representation of the object
print(SourceLinks.to_json())

# convert the object into a dict
source_links_dict = source_links_instance.to_dict()
# create an instance of SourceLinks from a dict
source_links_from_dict = SourceLinks.from_dict(source_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


