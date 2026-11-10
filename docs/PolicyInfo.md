# PolicyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms_and_service** | **str** | Terms of service text. | [optional] 

## Example

```python
from verity471.models.policy_info import PolicyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyInfo from a JSON string
policy_info_instance = PolicyInfo.from_json(json)
# print the JSON string representation of the object
print(PolicyInfo.to_json())

# convert the object into a dict
policy_info_dict = policy_info_instance.to_dict()
# create an instance of PolicyInfo from a dict
policy_info_from_dict = PolicyInfo.from_dict(policy_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


