# ThreatData

Threat data information for the entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletproof_hosting** | [**BulletproofHosting**](BulletproofHosting.md) | Information about the bulletproof hosting | [optional] 
**malware** | [**Malware**](Malware.md) | Information about the malware | [optional] 
**malware_family** | [**MalwareFamily**](MalwareFamily.md) | Information about the malware family | [optional] 

## Example

```python
from verity471.models.threat_data import ThreatData

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatData from a JSON string
threat_data_instance = ThreatData.from_json(json)
# print the JSON string representation of the object
print(ThreatData.to_json())

# convert the object into a dict
threat_data_dict = threat_data_instance.to_dict()
# create an instance of ThreatData from a dict
threat_data_from_dict = ThreatData.from_dict(threat_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


