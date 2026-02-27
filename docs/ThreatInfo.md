# ThreatInfo

Detailed information about the threat described in the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Family classification of the threat. | 
**id** | **str** | Unique identifier of the threat. | 
**type** | **str** | Type of the threat. | 

## Example

```python
from verity471.models.threat_info import ThreatInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatInfo from a JSON string
threat_info_instance = ThreatInfo.from_json(json)
# print the JSON string representation of the object
print(ThreatInfo.to_json())

# convert the object into a dict
threat_info_dict = threat_info_instance.to_dict()
# create an instance of ThreatInfo from a dict
threat_info_from_dict = ThreatInfo.from_dict(threat_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


