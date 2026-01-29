# PostResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentData]**](AttachmentData.md) | Attachments and images in the post | [optional] 
**author** | [**AuthorActor1**](AuthorActor1.md) |  | [optional] 
**creation_ts** | **str** | Publish date in ISO 8601 format | 
**entities** | [**List[EntityItem]**](EntityItem.md) | Entities extracted from the post | [optional] 
**html** | **str** | HTML version of message | 
**id** | **str** | Post unique id | 
**last_updated_ts** | **str** | First time updated entity was seen | 
**message** | **str** | Original Message | 
**translated_message** | **str** | Contains translated message if available | [optional] 
**translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 

## Example

```python
from verity471.models.post_response1 import PostResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of PostResponse1 from a JSON string
post_response1_instance = PostResponse1.from_json(json)
# print the JSON string representation of the object
print(PostResponse1.to_json())

# convert the object into a dict
post_response1_dict = post_response1_instance.to_dict()
# create an instance of PostResponse1 from a dict
post_response1_from_dict = PostResponse1.from_dict(post_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


