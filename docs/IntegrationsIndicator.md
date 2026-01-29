# IntegrationsIndicator

Indicator data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) | Activity information related to the entity | [optional] 
**classification** | [**Classification**](Classification.md) | Classification information for the entity | [optional] 
**confidence** | **int** | Confidence score for the indicator (0-100) | [optional] 
**data** | [**IndicatorData**](IndicatorData.md) | Indicator data containing specific details | [optional] 
**description** | **str** | Descriptive information about the indicator | [optional] 
**expiration_ts** | **datetime** | Timestamp when the indicator expires | [optional] 
**id** | **str** | Unique identifier of the entity | [optional] 
**kill_chain_phases** | [**List[KillChainPhase]**](KillChainPhase.md) | List of kill chain phases associated with the entity | [optional] 
**pattern** | **str** | Pattern string for the indicator | [optional] 
**pattern_type** | **str** | Type of pattern used for the indicator | [optional] 
**pattern_version** | **str** | Version of the pattern specification | [optional] 
**revocation** | [**Revocation**](Revocation.md) | Revocation information for the indicator, if applicable | [optional] 
**threat** | [**Threat**](Threat.md) | Threat information associated with the entity | [optional] 
**type** | **str** | Type of indicator | [optional] 

## Example

```python
from verity471.models.integrations_indicator import IntegrationsIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationsIndicator from a JSON string
integrations_indicator_instance = IntegrationsIndicator.from_json(json)
# print the JSON string representation of the object
print(IntegrationsIndicator.to_json())

# convert the object into a dict
integrations_indicator_dict = integrations_indicator_instance.to_dict()
# create an instance of IntegrationsIndicator from a dict
integrations_indicator_from_dict = IntegrationsIndicator.from_dict(integrations_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


