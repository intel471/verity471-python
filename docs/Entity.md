# Entity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the entity | 
**type** | [**EntityType**](EntityType.md) |  | 
**value** | **str** | The value of the entity | 
**activity** | [**Activity**](Activity.md) |  | 
**report** | [**ReportEntities**](ReportEntities.md) |  | [optional] 
**actor** | [**ActorObject**](ActorObject.md) |  | [optional] 

## Example

```python
from verity471.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print(Entity.to_json())

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_from_dict = Entity.from_dict(entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


