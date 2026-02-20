# ObservableStreamPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of matched observables | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**observables** | [**List[Observable]**](Observable.md) | A page of matched observables | [optional] 

## Example

```python
from verity471.models.observable_stream_page import ObservableStreamPage

# TODO update the JSON string below
json = "{}"
# create an instance of ObservableStreamPage from a JSON string
observable_stream_page_instance = ObservableStreamPage.from_json(json)
# print the JSON string representation of the object
print(ObservableStreamPage.to_json())

# convert the object into a dict
observable_stream_page_dict = observable_stream_page_instance.to_dict()
# create an instance of ObservableStreamPage from a dict
observable_stream_page_from_dict = ObservableStreamPage.from_dict(observable_stream_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


