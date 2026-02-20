# GeoIpObservables

Geo IP information for the observable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**subdivision** | **List[str]** |  | [optional] 
**isp** | [**Isp**](Isp.md) |  | [optional] 

## Example

```python
from verity471.models.geo_ip_observables import GeoIpObservables

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIpObservables from a JSON string
geo_ip_observables_instance = GeoIpObservables.from_json(json)
# print the JSON string representation of the object
print(GeoIpObservables.to_json())

# convert the object into a dict
geo_ip_observables_dict = geo_ip_observables_instance.to_dict()
# create an instance of GeoIpObservables from a dict
geo_ip_observables_from_dict = GeoIpObservables.from_dict(geo_ip_observables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


