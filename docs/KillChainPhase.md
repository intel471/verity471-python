# KillChainPhase

Kill chain phase information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kill_chain_name** | **str** | Name of the kill chain framework | [optional] 
**phase_name** | **str** | Name of the phase within the kill chain | [optional] 

## Example

```python
from verity471.models.kill_chain_phase import KillChainPhase

# TODO update the JSON string below
json = "{}"
# create an instance of KillChainPhase from a JSON string
kill_chain_phase_instance = KillChainPhase.from_json(json)
# print the JSON string representation of the object
print(KillChainPhase.to_json())

# convert the object into a dict
kill_chain_phase_dict = kill_chain_phase_instance.to_dict()
# create an instance of KillChainPhase from a dict
kill_chain_phase_from_dict = KillChainPhase.from_dict(kill_chain_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


