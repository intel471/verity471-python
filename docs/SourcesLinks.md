# SourcesLinks

URL to get forum details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external** | [**Link**](Link.md) |  | [optional] 
**verity_api** | [**Link**](Link.md) |  | [optional] 
**verity_portal** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from verity471.models.sources_links import SourcesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SourcesLinks from a JSON string
sources_links_instance = SourcesLinks.from_json(json)
# print the JSON string representation of the object
print(SourcesLinks.to_json())

# convert the object into a dict
sources_links_dict = sources_links_instance.to_dict()
# create an instance of SourcesLinks from a dict
sources_links_from_dict = SourcesLinks.from_dict(sources_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


