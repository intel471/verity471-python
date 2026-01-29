# DataLeakSitePost1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentData]**](AttachmentData.md) | Attachments and images in the post | [optional] 
**creation_ts** | **str** | First scraping date in ISO 8601 format | 
**file_listing** | [**DataLeakSiteFileListingUrl**](DataLeakSiteFileListingUrl.md) |  | [optional] 
**inactive_since** | **str** | The date post became inactive or was reactivated again in ISO 8601 format | [optional] 
**is_inactive** | **bool** | True if post is inactive | [optional] 
**message** | **str** | Message of post | 
**published_at** | **str** | Post publish date in ISO 8601 format | [optional] 
**title** | **str** | Title of post | 

## Example

```python
from verity471.models.data_leak_site_post1 import DataLeakSitePost1

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSitePost1 from a JSON string
data_leak_site_post1_instance = DataLeakSitePost1.from_json(json)
# print the JSON string representation of the object
print(DataLeakSitePost1.to_json())

# convert the object into a dict
data_leak_site_post1_dict = data_leak_site_post1_instance.to_dict()
# create an instance of DataLeakSitePost1 from a dict
data_leak_site_post1_from_dict = DataLeakSitePost1.from_dict(data_leak_site_post1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


