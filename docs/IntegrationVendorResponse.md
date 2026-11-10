# IntegrationVendorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**additional_links_forum** | **str** | Additional vendor forum link | [optional] 
**additional_links_reviews** | **str** | Additional vendor reviews link | [optional] 
**average_response_time** | **int** | Average vendor response time, in the unit reported by the marketplace | [optional] 
**id** | **str** | External vendor id | 
**link** | **str** | Vendor url | [optional] 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 
**marketplace_id** | **str** | External id of the marketplace the vendor sells on | [optional] 
**marketplace_name** | **str** | Name of the marketplace the vendor sells on, falls back to the marketplace alias | [optional] 
**name** | **str** | Vendor name, falls back to the document title | 
**rating** | [**RatingOverall**](RatingOverall.md) |  | [optional] 
**valid_rate_10_days** | **float** | Percentage (0–100) of valid goods over the last 10 days | [optional] 
**valid_rate_30_days** | **float** | Percentage (0–100) of valid goods over the last 30 days | [optional] 
**valid_rate_overall** | **float** | Percentage (0–100) of valid goods across all time | [optional] 

## Example

```python
from verity471.models.integration_vendor_response import IntegrationVendorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationVendorResponse from a JSON string
integration_vendor_response_instance = IntegrationVendorResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationVendorResponse.to_json())

# convert the object into a dict
integration_vendor_response_dict = integration_vendor_response_instance.to_dict()
# create an instance of IntegrationVendorResponse from a dict
integration_vendor_response_from_dict = IntegrationVendorResponse.from_dict(integration_vendor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


