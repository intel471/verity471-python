# ActivityResponse

Period credential was active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_seen_ts** | **str** | Start of the credential activity range. | 
**last_seen_ts** | **str** | End of the credential activity range. | 

## Example

```python
from verity471.models.activity_response import ActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityResponse from a JSON string
activity_response_instance = ActivityResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityResponse.to_json())

# convert the object into a dict
activity_response_dict = activity_response_instance.to_dict()
# create an instance of ActivityResponse from a dict
activity_response_from_dict = ActivityResponse.from_dict(activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


