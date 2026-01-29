# VictimResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Purported victim name. | 
**urls** | **List[str]** | List of purported victim URLs. | [optional] 

## Example

```python
from verity471.models.victim_response import VictimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VictimResponse from a JSON string
victim_response_instance = VictimResponse.from_json(json)
# print the JSON string representation of the object
print(VictimResponse.to_json())

# convert the object into a dict
victim_response_dict = victim_response_instance.to_dict()
# create an instance of VictimResponse from a dict
victim_response_from_dict = VictimResponse.from_dict(victim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


