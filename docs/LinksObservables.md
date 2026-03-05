# LinksObservables

Links to the source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verity_api** | [**Link**](Link.md) |  | [optional] 
**verity_portal** | [**Link**](Link.md) |  | [optional] 
**external** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from verity471.models.links_observables import LinksObservables

# TODO update the JSON string below
json = "{}"
# create an instance of LinksObservables from a JSON string
links_observables_instance = LinksObservables.from_json(json)
# print the JSON string representation of the object
print(LinksObservables.to_json())

# convert the object into a dict
links_observables_dict = links_observables_instance.to_dict()
# create an instance of LinksObservables from a dict
links_observables_from_dict = LinksObservables.from_dict(links_observables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


