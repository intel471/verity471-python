# Observable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the observable | 
**type** | [**ObservableType**](ObservableType.md) |  | 
**value** | **str** | Value of the observable | 
**geo_ip** | [**GeoIpObservables**](GeoIpObservables.md) |  | [optional] 
**activity** | [**Activity**](Activity.md) |  | 
**report** | [**ReportObservables**](ReportObservables.md) |  | 

## Example

```python
from verity471.models.observable import Observable

# TODO update the JSON string below
json = "{}"
# create an instance of Observable from a JSON string
observable_instance = Observable.from_json(json)
# print the JSON string representation of the object
print(Observable.to_json())

# convert the object into a dict
observable_dict = observable_instance.to_dict()
# create an instance of Observable from a dict
observable_from_dict = Observable.from_dict(observable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


