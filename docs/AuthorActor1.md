# AuthorActor1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historical_usernames** | **List[str]** | Author previous usernames | [optional] 
**id** | **str** | Unique id of actor | 
**user_name** | **str** | Username | 

## Example

```python
from verity471.models.author_actor1 import AuthorActor1

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorActor1 from a JSON string
author_actor1_instance = AuthorActor1.from_json(json)
# print the JSON string representation of the object
print(AuthorActor1.to_json())

# convert the object into a dict
author_actor1_dict = author_actor1_instance.to_dict()
# create an instance of AuthorActor1 from a dict
author_actor1_from_dict = AuthorActor1.from_dict(author_actor1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


