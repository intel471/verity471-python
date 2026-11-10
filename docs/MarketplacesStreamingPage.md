# MarketplacesStreamingPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched entities | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**marketplaces** | [**List[IntegrationMarketplaceResponse]**](IntegrationMarketplaceResponse.md) | List of paginated marketplaces | [optional] 

## Example

```python
from verity471.models.marketplaces_streaming_page import MarketplacesStreamingPage

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacesStreamingPage from a JSON string
marketplaces_streaming_page_instance = MarketplacesStreamingPage.from_json(json)
# print the JSON string representation of the object
print(MarketplacesStreamingPage.to_json())

# convert the object into a dict
marketplaces_streaming_page_dict = marketplaces_streaming_page_instance.to_dict()
# create an instance of MarketplacesStreamingPage from a dict
marketplaces_streaming_page_from_dict = MarketplacesStreamingPage.from_dict(marketplaces_streaming_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


