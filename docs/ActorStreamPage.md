# ActorStreamPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched actors | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**actors** | [**List[Actor]**](Actor.md) | A page of matched actors | [optional] 

## Example

```python
from verity471.models.actor_stream_page import ActorStreamPage

# TODO update the JSON string below
json = "{}"
# create an instance of ActorStreamPage from a JSON string
actor_stream_page_instance = ActorStreamPage.from_json(json)
# print the JSON string representation of the object
print(ActorStreamPage.to_json())

# convert the object into a dict
actor_stream_page_dict = actor_stream_page_instance.to_dict()
# create an instance of ActorStreamPage from a dict
actor_stream_page_from_dict = ActorStreamPage.from_dict(actor_stream_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


