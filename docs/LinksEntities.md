# LinksEntities

Links to the source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verity_api** | [**Link**](Link.md) |  | [optional] 
**verity_portal** | [**Link**](Link.md) |  | [optional] 
**external** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from verity471.models.links_entities import LinksEntities

# TODO update the JSON string below
json = "{}"
# create an instance of LinksEntities from a JSON string
links_entities_instance = LinksEntities.from_json(json)
# print the JSON string representation of the object
print(LinksEntities.to_json())

# convert the object into a dict
links_entities_dict = links_entities_instance.to_dict()
# create an instance of LinksEntities from a dict
links_entities_from_dict = LinksEntities.from_dict(links_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


