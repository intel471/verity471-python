# Threat

Threat information for the entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ThreatData**](ThreatData.md) | Detailed data about the threat | [optional] 
**type** | **str** | Type of the threat | [optional] 

## Example

```python
from verity471.models.threat import Threat

# TODO update the JSON string below
json = "{}"
# create an instance of Threat from a JSON string
threat_instance = Threat.from_json(json)
# print the JSON string representation of the object
print(Threat.to_json())

# convert the object into a dict
threat_dict = threat_instance.to_dict()
# create an instance of Threat from a dict
threat_from_dict = Threat.from_dict(threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


