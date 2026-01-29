# IndicatorData

Indicator data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain information | [optional] 
**email** | **str** | Email information | [optional] 
**file** | [**File**](File.md) | File information | [optional] 
**ipv4** | [**Ipv4**](Ipv4.md) | IPv4 information | [optional] 
**url** | **str** | URL information | [optional] 
**yara** | [**YaraData**](YaraData.md) | YARA information | [optional] 

## Example

```python
from verity471.models.indicator_data import IndicatorData

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorData from a JSON string
indicator_data_instance = IndicatorData.from_json(json)
# print the JSON string representation of the object
print(IndicatorData.to_json())

# convert the object into a dict
indicator_data_dict = indicator_data_instance.to_dict()
# create an instance of IndicatorData from a dict
indicator_data_from_dict = IndicatorData.from_dict(indicator_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


