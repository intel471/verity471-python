# ForumsPostsStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched post entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**posts** | [**List[PostDetails1]**](PostDetails1.md) | A page of matched post entities | [optional] 

## Example

```python
from verity471.models.forums_posts_streaming_page import ForumsPostsStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsPostsStreamingPage from a JSON string
forums_posts_streaming_page_instance = ForumsPostsStreamingPage.from_json(json)
# print the JSON string representation of the object
print(ForumsPostsStreamingPage.to_json())

# convert the object into a dict
forums_posts_streaming_page_dict = forums_posts_streaming_page_instance.to_dict()
# create an instance of ForumsPostsStreamingPage from a dict
forums_posts_streaming_page_from_dict = ForumsPostsStreamingPage.from_dict(forums_posts_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


