# ForumsPrivateMessagesStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched private message entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**private_messages** | [**List[PrivateMessageDetails1]**](PrivateMessageDetails1.md) | A page of matched private message entities | [optional] 

## Example

```python
from verity471.models.forums_private_messages_streaming_page import ForumsPrivateMessagesStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsPrivateMessagesStreamingPage from a JSON string
forums_private_messages_streaming_page_instance = ForumsPrivateMessagesStreamingPage.from_json(json)
# print the JSON string representation of the object
print(ForumsPrivateMessagesStreamingPage.to_json())

# convert the object into a dict
forums_private_messages_streaming_page_dict = forums_private_messages_streaming_page_instance.to_dict()
# create an instance of ForumsPrivateMessagesStreamingPage from a dict
forums_private_messages_streaming_page_from_dict = ForumsPrivateMessagesStreamingPage.from_dict(forums_private_messages_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


