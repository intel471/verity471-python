# ProductsStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**products** | [**List[IntegrationProductResponse]**](IntegrationProductResponse.md) | List of paginated products | [optional] 

## Example

```python
from verity471.models.products_streaming_page import ProductsStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsStreamingPage from a JSON string
products_streaming_page_instance = ProductsStreamingPage.from_json(json)
# print the JSON string representation of the object
print(ProductsStreamingPage.to_json())

# convert the object into a dict
products_streaming_page_dict = products_streaming_page_instance.to_dict()
# create an instance of ProductsStreamingPage from a dict
products_streaming_page_from_dict = ProductsStreamingPage.from_dict(products_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


