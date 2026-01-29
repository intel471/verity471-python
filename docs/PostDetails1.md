# PostDetails1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forum** | [**ForumsResponse1**](ForumsResponse1.md) |  | [optional] 
**post** | [**PostResponse1**](PostResponse1.md) |  | 
**sub_forum** | [**SubForumResponse1**](SubForumResponse1.md) |  | [optional] 
**thread** | [**ThreadResponse1**](ThreadResponse1.md) |  | [optional] 

## Example

```python
from verity471.models.post_details1 import PostDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of PostDetails1 from a JSON string
post_details1_instance = PostDetails1.from_json(json)
# print the JSON string representation of the object
print(PostDetails1.to_json())

# convert the object into a dict
post_details1_dict = post_details1_instance.to_dict()
# create an instance of PostDetails1 from a dict
post_details1_from_dict = PostDetails1.from_dict(post_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


