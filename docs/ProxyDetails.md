# ProxyDetails

Fields of a `proxy` product; set only when `kind` is `proxy`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**ProxyBasicInfo**](ProxyBasicInfo.md) |  | [optional] 

## Example

```python
from verity471.models.proxy_details import ProxyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyDetails from a JSON string
proxy_details_instance = ProxyDetails.from_json(json)
# print the JSON string representation of the object
print(ProxyDetails.to_json())

# convert the object into a dict
proxy_details_dict = proxy_details_instance.to_dict()
# create an instance of ProxyDetails from a dict
proxy_details_from_dict = ProxyDetails.from_dict(proxy_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


