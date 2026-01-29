# IspData

Internet Service Provider information for the IP address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autonomous_system** | **str** | Autonomous System Number (ASN) information | [optional] 
**isp** | **str** | Name of the Internet Service Provider | [optional] 
**network** | **str** | Network range information for the IP address | [optional] 
**organization** | **str** | Organization name associated with the IP address | [optional] 

## Example

```python
from verity471.models.isp_data import IspData

# TODO update the JSON string below
json = "{}"
# create an instance of IspData from a JSON string
isp_data_instance = IspData.from_json(json)
# print the JSON string representation of the object
print(IspData.to_json())

# convert the object into a dict
isp_data_dict = isp_data_instance.to_dict()
# create an instance of IspData from a dict
isp_data_from_dict = IspData.from_dict(isp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


