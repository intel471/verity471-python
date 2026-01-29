# SpotReportsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total Spot reports matching the query | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**reports** | [**List[SpotReportResponse]**](SpotReportResponse.md) | List of Spot reports in the current batch | [optional] 

## Example

```python
from verity471.models.spot_reports_response_stream import SpotReportsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of SpotReportsResponseStream from a JSON string
spot_reports_response_stream_instance = SpotReportsResponseStream.from_json(json)
# print the JSON string representation of the object
print(SpotReportsResponseStream.to_json())

# convert the object into a dict
spot_reports_response_stream_dict = spot_reports_response_stream_instance.to_dict()
# create an instance of SpotReportsResponseStream from a dict
spot_reports_response_stream_from_dict = SpotReportsResponseStream.from_dict(spot_reports_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


