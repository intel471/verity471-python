# DataLeakSitePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**attachment_data** | [**Dict[str, AttachmentData]**](AttachmentData.md) |  | 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | 
**inactive_since** | **str** |  | [optional] 
**is_inactive** | **bool** |  | [optional] 
**message** | **str** |  | 
**published_at** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from verity471.models.data_leak_site_post import DataLeakSitePost

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSitePost from a JSON string
data_leak_site_post_instance = DataLeakSitePost.from_json(json)
# print the JSON string representation of the object
print(DataLeakSitePost.to_json())

# convert the object into a dict
data_leak_site_post_dict = data_leak_site_post_instance.to_dict()
# create an instance of DataLeakSitePost from a dict
data_leak_site_post_from_dict = DataLeakSitePost.from_dict(data_leak_site_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


