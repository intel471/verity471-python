# ChatMessagesStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched message entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**messages** | [**List[ChatRoomMessageStream]**](ChatRoomMessageStream.md) | A page of matched message entities | [optional] 

## Example

```python
from verity471.models.chat_messages_streaming_page import ChatMessagesStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessagesStreamingPage from a JSON string
chat_messages_streaming_page_instance = ChatMessagesStreamingPage.from_json(json)
# print the JSON string representation of the object
print(ChatMessagesStreamingPage.to_json())

# convert the object into a dict
chat_messages_streaming_page_dict = chat_messages_streaming_page_instance.to_dict()
# create an instance of ChatMessagesStreamingPage from a dict
chat_messages_streaming_page_from_dict = ChatMessagesStreamingPage.from_dict(chat_messages_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


