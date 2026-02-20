# ActorObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**handles** | **List[str]** | Actor names - from most current in use first, and list historical handles. | [optional] 
**forum** | [**ForumObject**](ForumObject.md) |  | [optional] 

## Example

```python
from verity471.models.actor_object import ActorObject

# TODO update the JSON string below
json = "{}"
# create an instance of ActorObject from a JSON string
actor_object_instance = ActorObject.from_json(json)
# print the JSON string representation of the object
print(ActorObject.to_json())

# convert the object into a dict
actor_object_dict = actor_object_instance.to_dict()
# create an instance of ActorObject from a dict
actor_object_from_dict = ActorObject.from_dict(actor_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


