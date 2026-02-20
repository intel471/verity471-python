# ForumObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of a forum | 
**title** | **str** | The name of the forum that the actor is associated with | 

## Example

```python
from verity471.models.forum_object import ForumObject

# TODO update the JSON string below
json = "{}"
# create an instance of ForumObject from a JSON string
forum_object_instance = ForumObject.from_json(json)
# print the JSON string representation of the object
print(ForumObject.to_json())

# convert the object into a dict
forum_object_dict = forum_object_instance.to_dict()
# create an instance of ForumObject from a dict
forum_object_from_dict = ForumObject.from_dict(forum_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


