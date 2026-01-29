# DataLeakSitePostsStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched post entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**posts** | [**List[DataLeakSitePostItem]**](DataLeakSitePostItem.md) | A page of matched post entities with nested thread and website | [optional] 

## Example

```python
from verity471.models.data_leak_site_posts_streaming_page import DataLeakSitePostsStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSitePostsStreamingPage from a JSON string
data_leak_site_posts_streaming_page_instance = DataLeakSitePostsStreamingPage.from_json(json)
# print the JSON string representation of the object
print(DataLeakSitePostsStreamingPage.to_json())

# convert the object into a dict
data_leak_site_posts_streaming_page_dict = data_leak_site_posts_streaming_page_instance.to_dict()
# create an instance of DataLeakSitePostsStreamingPage from a dict
data_leak_site_posts_streaming_page_from_dict = DataLeakSitePostsStreamingPage.from_dict(data_leak_site_posts_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


