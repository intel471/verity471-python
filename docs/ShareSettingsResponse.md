# ShareSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**organisation_id** | **str** |  | 
**created** | **datetime** |  | 

## Example

```python
from verity471.models.share_settings_response import ShareSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShareSettingsResponse from a JSON string
share_settings_response_instance = ShareSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(ShareSettingsResponse.to_json())

# convert the object into a dict
share_settings_response_dict = share_settings_response_instance.to_dict()
# create an instance of ShareSettingsResponse from a dict
share_settings_response_from_dict = ShareSettingsResponse.from_dict(share_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


