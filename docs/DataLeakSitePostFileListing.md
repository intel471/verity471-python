# DataLeakSitePostFileListing

Post file listing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | API url for download file listing | [optional] 

## Example

```python
from verity471.models.data_leak_site_post_file_listing import DataLeakSitePostFileListing

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSitePostFileListing from a JSON string
data_leak_site_post_file_listing_instance = DataLeakSitePostFileListing.from_json(json)
# print the JSON string representation of the object
print(DataLeakSitePostFileListing.to_json())

# convert the object into a dict
data_leak_site_post_file_listing_dict = data_leak_site_post_file_listing_instance.to_dict()
# create an instance of DataLeakSitePostFileListing from a dict
data_leak_site_post_file_listing_from_dict = DataLeakSitePostFileListing.from_dict(data_leak_site_post_file_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


