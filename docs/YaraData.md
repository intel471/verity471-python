# YaraData

Yara data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | Yara signature | [optional] 
**title** | **str** | Title of the Yara rule | [optional] 

## Example

```python
from verity471.models.yara_data import YaraData

# TODO update the JSON string below
json = "{}"
# create an instance of YaraData from a JSON string
yara_data_instance = YaraData.from_json(json)
# print the JSON string representation of the object
print(YaraData.to_json())

# convert the object into a dict
yara_data_dict = yara_data_instance.to_dict()
# create an instance of YaraData from a dict
yara_data_from_dict = YaraData.from_dict(yara_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


