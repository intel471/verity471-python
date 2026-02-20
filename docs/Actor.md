# Actor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the actor | 
**activity** | [**Activity**](Activity.md) |  | 
**handles** | **List[str]** | Actor names - from most current in use first, and list historical handles. | [optional] 
**forum** | [**Forum**](Forum.md) |  | [optional] 
**im_server** | [**ImServer**](ImServer.md) |  | [optional] 
**report** | [**Report**](Report.md) |  | [optional] 

## Example

```python
from verity471.models.actor import Actor

# TODO update the JSON string below
json = "{}"
# create an instance of Actor from a JSON string
actor_instance = Actor.from_json(json)
# print the JSON string representation of the object
print(Actor.to_json())

# convert the object into a dict
actor_dict = actor_instance.to_dict()
# create an instance of Actor from a dict
actor_from_dict = Actor.from_dict(actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


