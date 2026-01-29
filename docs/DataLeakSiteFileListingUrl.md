# DataLeakSiteFileListingUrl

Post file listing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | API url for download file listing | 

## Example

```python
from verity471.models.data_leak_site_file_listing_url import DataLeakSiteFileListingUrl

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSiteFileListingUrl from a JSON string
data_leak_site_file_listing_url_instance = DataLeakSiteFileListingUrl.from_json(json)
# print the JSON string representation of the object
print(DataLeakSiteFileListingUrl.to_json())

# convert the object into a dict
data_leak_site_file_listing_url_dict = data_leak_site_file_listing_url_instance.to_dict()
# create an instance of DataLeakSiteFileListingUrl from a dict
data_leak_site_file_listing_url_from_dict = DataLeakSiteFileListingUrl.from_dict(data_leak_site_file_listing_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


