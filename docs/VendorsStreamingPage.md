# VendorsStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**vendors** | [**List[IntegrationVendorResponse]**](IntegrationVendorResponse.md) | List of paginated vendors | [optional] 

## Example

```python
from verity471.models.vendors_streaming_page import VendorsStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorsStreamingPage from a JSON string
vendors_streaming_page_instance = VendorsStreamingPage.from_json(json)
# print the JSON string representation of the object
print(VendorsStreamingPage.to_json())

# convert the object into a dict
vendors_streaming_page_dict = vendors_streaming_page_instance.to_dict()
# create an instance of VendorsStreamingPage from a dict
vendors_streaming_page_from_dict = VendorsStreamingPage.from_dict(vendors_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


