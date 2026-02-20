# EntityStreamPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**entities** | [**List[Entity]**](Entity.md) | A page of matched entities | [optional] 

## Example

```python
from verity471.models.entity_stream_page import EntityStreamPage

# TODO update the JSON string below
json = "{}"
# create an instance of EntityStreamPage from a JSON string
entity_stream_page_instance = EntityStreamPage.from_json(json)
# print the JSON string representation of the object
print(EntityStreamPage.to_json())

# convert the object into a dict
entity_stream_page_dict = entity_stream_page_instance.to_dict()
# create an instance of EntityStreamPage from a dict
entity_stream_page_from_dict = EntityStreamPage.from_dict(entity_stream_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


