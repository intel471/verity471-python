# GeoIp

Geographical information associated with the IP address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City name where the IP address is located | [optional] 
**country** | **str** | Country name where the IP address is located | [optional] 
**country_code** | **str** | Two-letter country code (ISO 3166-1 alpha-2) where the IP address is located | [optional] 
**isp** | [**IspData**](IspData.md) | Internet Service Provider information for the IP address | [optional] 
**subdivision** | **List[str]** | Administrative subdivisions (states, provinces, etc.) where the IP address is located | [optional] 

## Example

```python
from verity471.models.geo_ip import GeoIp

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIp from a JSON string
geo_ip_instance = GeoIp.from_json(json)
# print the JSON string representation of the object
print(GeoIp.to_json())

# convert the object into a dict
geo_ip_dict = geo_ip_instance.to_dict()
# create an instance of GeoIp from a dict
geo_ip_from_dict = GeoIp.from_dict(geo_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


