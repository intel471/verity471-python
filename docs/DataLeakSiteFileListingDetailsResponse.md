# DataLeakSiteFileListingDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**chunk_number** | **int** |  | 
**download** | [**DataLeakSiteFileListingDownload**](DataLeakSiteFileListingDownload.md) |  | 
**file** | [**DataLeakSiteFileListingFileRef**](DataLeakSiteFileListingFileRef.md) |  | 
**id** | **str** |  | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | 
**post** | [**DataLeakSiteFileListingPostRef**](DataLeakSiteFileListingPostRef.md) |  | 
**thread** | [**DataLeakSiteFileListingThreadRef**](DataLeakSiteFileListingThreadRef.md) |  | 
**website** | [**DataLeakSiteFileListingWebsiteRef**](DataLeakSiteFileListingWebsiteRef.md) |  | [optional] 

## Example

```python
from verity471.models.data_leak_site_file_listing_details_response import DataLeakSiteFileListingDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSiteFileListingDetailsResponse from a JSON string
data_leak_site_file_listing_details_response_instance = DataLeakSiteFileListingDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(DataLeakSiteFileListingDetailsResponse.to_json())

# convert the object into a dict
data_leak_site_file_listing_details_response_dict = data_leak_site_file_listing_details_response_instance.to_dict()
# create an instance of DataLeakSiteFileListingDetailsResponse from a dict
data_leak_site_file_listing_details_response_from_dict = DataLeakSiteFileListingDetailsResponse.from_dict(data_leak_site_file_listing_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


