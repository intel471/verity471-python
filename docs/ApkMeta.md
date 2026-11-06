# ApkMeta

APK metadata information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility_service** | **str** | Accessibility service registered by the app. | [optional] 
**app_name** | **str** | Name of the app. | [optional] 
**certificate** | [**Certificate**](Certificate.md) | Signing certificate of the app. | [optional] 
**impersonated_app_name** | **str** | Name of the app being impersonated. | [optional] 
**impersonated_app_package** | **str** | Package name of the app being impersonated. | [optional] 
**loader** | **str** | Loader used by the app. | [optional] 
**main_activity** | **str** | Main activity of the app. | [optional] 
**package_name** | **str** | Package name of the app. | [optional] 

## Example

```python
from verity471.models.apk_meta import ApkMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ApkMeta from a JSON string
apk_meta_instance = ApkMeta.from_json(json)
# print the JSON string representation of the object
print(ApkMeta.to_json())

# convert the object into a dict
apk_meta_dict = apk_meta_instance.to_dict()
# create an instance of ApkMeta from a dict
apk_meta_from_dict = ApkMeta.from_dict(apk_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


