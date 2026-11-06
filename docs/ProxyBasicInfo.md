# ProxyBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**css_blacklist** | **str** | CSS blacklist status | [optional] 
**dns_address** | **str** | DNS server/IP. | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**internet_service_provider** | **str** | Internet service provider of the proxy IP | [optional] 
**ip_address** | **str** | IP (proxies, shells, etc.). | [optional] 
**is_online** | **bool** | Whether the proxy is online | [optional] 
**ping** | **str** | Ping as given by the listing (e.g. 33 ms) | [optional] 
**proxy_type** | **str** | Proxy/RDP/SOCKS type. | [optional] 
**sbl_blacklist** | **str** | Spamhaus SBL status | [optional] 
**speed** | **str** | Connection speed | [optional] 
**state** | **str** | State or region | [optional] 
**xbl_blacklist** | **str** | Spamhaus XBL blacklist status (Clear or Bad) | [optional] 
**zip** | **str** | Postal/ZIP code | [optional] 

## Example

```python
from verity471.models.proxy_basic_info import ProxyBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyBasicInfo from a JSON string
proxy_basic_info_instance = ProxyBasicInfo.from_json(json)
# print the JSON string representation of the object
print(ProxyBasicInfo.to_json())

# convert the object into a dict
proxy_basic_info_dict = proxy_basic_info_instance.to_dict()
# create an instance of ProxyBasicInfo from a dict
proxy_basic_info_from_dict = ProxyBasicInfo.from_dict(proxy_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


