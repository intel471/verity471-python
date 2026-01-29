# Ipv4

Information about an IPv4 address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_ip** | [**GeoIp**](GeoIp.md) | Geographical information associated with the IP address | [optional] 
**ip_address** | **str** | IPv4 address in dotted decimal notation | [optional] 

## Example

```python
from verity471.models.ipv4 import Ipv4

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv4 from a JSON string
ipv4_instance = Ipv4.from_json(json)
# print the JSON string representation of the object
print(Ipv4.to_json())

# convert the object into a dict
ipv4_dict = ipv4_instance.to_dict()
# create an instance of Ipv4 from a dict
ipv4_from_dict = Ipv4.from_dict(ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


