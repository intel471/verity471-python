# Activity

Activity information related to the entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_seen_ts** | **datetime** | First time the entity was seen | 
**last_seen_ts** | **datetime** | Last time the entity was seen | 

## Example

```python
from verity471.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


