# ResourcesStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**resources** | [**List[IntegrationResourceResponse]**](IntegrationResourceResponse.md) | List of paginated resources | [optional] 

## Example

```python
from verity471.models.resources_streaming_page import ResourcesStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStreamingPage from a JSON string
resources_streaming_page_instance = ResourcesStreamingPage.from_json(json)
# print the JSON string representation of the object
print(ResourcesStreamingPage.to_json())

# convert the object into a dict
resources_streaming_page_dict = resources_streaming_page_instance.to_dict()
# create an instance of ResourcesStreamingPage from a dict
resources_streaming_page_from_dict = ResourcesStreamingPage.from_dict(resources_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


