# DataLeakSitePostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post** | [**DataLeakSitePost1**](DataLeakSitePost1.md) |  | 
**thread** | [**DataLeakSitePostThread**](DataLeakSitePostThread.md) |  | 
**website** | [**DataLeakSitePostWebsite**](DataLeakSitePostWebsite.md) |  | 

## Example

```python
from verity471.models.data_leak_site_post_item import DataLeakSitePostItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataLeakSitePostItem from a JSON string
data_leak_site_post_item_instance = DataLeakSitePostItem.from_json(json)
# print the JSON string representation of the object
print(DataLeakSitePostItem.to_json())

# convert the object into a dict
data_leak_site_post_item_dict = data_leak_site_post_item_instance.to_dict()
# create an instance of DataLeakSitePostItem from a dict
data_leak_site_post_item_from_dict = DataLeakSitePostItem.from_dict(data_leak_site_post_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


