# Forum

A forum that the actor is associated with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the forum | 
**title** | **str** | A forum that the actor is associated with | 

## Example

```python
from verity471.models.forum import Forum

# TODO update the JSON string below
json = "{}"
# create an instance of Forum from a JSON string
forum_instance = Forum.from_json(json)
# print the JSON string representation of the object
print(Forum.to_json())

# convert the object into a dict
forum_dict = forum_instance.to_dict()
# create an instance of Forum from a dict
forum_from_dict = Forum.from_dict(forum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


