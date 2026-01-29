# SubForumResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**id** | **str** | Sub forum unique id | 
**title** | **str** | Sub forum title | 

## Example

```python
from verity471.models.sub_forum_response1 import SubForumResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of SubForumResponse1 from a JSON string
sub_forum_response1_instance = SubForumResponse1.from_json(json)
# print the JSON string representation of the object
print(SubForumResponse1.to_json())

# convert the object into a dict
sub_forum_response1_dict = sub_forum_response1_instance.to_dict()
# create an instance of SubForumResponse1 from a dict
sub_forum_response1_from_dict = SubForumResponse1.from_dict(sub_forum_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


