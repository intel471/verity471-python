# IntegrationsEvent

Event data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) | Activity information related to the entity | [optional] 
**classification** | [**Classification**](Classification.md) | Classification information for the entity | [optional] 
**data** | [**EventData**](EventData.md) | Event-specific data | [optional] 
**id** | **str** | Unique identifier of the entity | [optional] 
**kill_chain_phases** | [**List[KillChainPhase]**](KillChainPhase.md) | List of kill chain phases associated with the entity | [optional] 
**threat** | [**ThreatMalware**](ThreatMalware.md) | Threat information associated with the entity | [optional] 
**type** | **str** | Type of Event | [optional] 

## Example

```python
from verity471.models.integrations_event import IntegrationsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationsEvent from a JSON string
integrations_event_instance = IntegrationsEvent.from_json(json)
# print the JSON string representation of the object
print(IntegrationsEvent.to_json())

# convert the object into a dict
integrations_event_dict = integrations_event_instance.to_dict()
# create an instance of IntegrationsEvent from a dict
integrations_event_from_dict = IntegrationsEvent.from_dict(integrations_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


