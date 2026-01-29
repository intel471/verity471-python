# SignificantActivity

Report related significant activity data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**event_tag** | [**EventTag**](EventTag.md) |  | 

## Example

```python
from verity471.models.significant_activity import SignificantActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SignificantActivity from a JSON string
significant_activity_instance = SignificantActivity.from_json(json)
# print the JSON string representation of the object
print(SignificantActivity.to_json())

# convert the object into a dict
significant_activity_dict = significant_activity_instance.to_dict()
# create an instance of SignificantActivity from a dict
significant_activity_from_dict = SignificantActivity.from_dict(significant_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


