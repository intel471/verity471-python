# VictimInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Victim&#39;s street address | [optional] 
**city** | **str** | Victim&#39;s city | [optional] 
**country** | **str** | Victim&#39;s country | [optional] 
**email_address** | **str** | Victim&#39;s email address | [optional] 
**holder** | **str** | Cardholder name | [optional] 
**ip_address** | **str** | Victim&#39;s IP address | [optional] 
**link** | **str** | Target URL. | [optional] 
**name** | **str** | Victim name | [optional] 
**phone_number** | **str** | Victim&#39;s phone number | [optional] 
**state** | **str** | Victim&#39;s state or region | [optional] 
**zip** | **str** | Victim&#39;s postal/ZIP code | [optional] 

## Example

```python
from verity471.models.victim_info import VictimInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VictimInfo from a JSON string
victim_info_instance = VictimInfo.from_json(json)
# print the JSON string representation of the object
print(VictimInfo.to_json())

# convert the object into a dict
victim_info_dict = victim_info_instance.to_dict()
# create an instance of VictimInfo from a dict
victim_info_from_dict = VictimInfo.from_dict(victim_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


