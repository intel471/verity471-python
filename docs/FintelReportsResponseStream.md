# FintelReportsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total Fintel reports matching the query | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**reports** | [**List[FintelResponse]**](FintelResponse.md) | List of Fintel reports in the current batch | [optional] 

## Example

```python
from verity471.models.fintel_reports_response_stream import FintelReportsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of FintelReportsResponseStream from a JSON string
fintel_reports_response_stream_instance = FintelReportsResponseStream.from_json(json)
# print the JSON string representation of the object
print(FintelReportsResponseStream.to_json())

# convert the object into a dict
fintel_reports_response_stream_dict = fintel_reports_response_stream_instance.to_dict()
# create an instance of FintelReportsResponseStream from a dict
fintel_reports_response_stream_from_dict = FintelReportsResponseStream.from_dict(fintel_reports_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


