# InfoReportsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total Info reports matching the query | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**reports** | [**List[InfoReportResponse]**](InfoReportResponse.md) | List of Info reports in the current batch | [optional] 

## Example

```python
from verity471.models.info_reports_response_stream import InfoReportsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of InfoReportsResponseStream from a JSON string
info_reports_response_stream_instance = InfoReportsResponseStream.from_json(json)
# print the JSON string representation of the object
print(InfoReportsResponseStream.to_json())

# convert the object into a dict
info_reports_response_stream_dict = info_reports_response_stream_instance.to_dict()
# create an instance of InfoReportsResponseStream from a dict
info_reports_response_stream_from_dict = InfoReportsResponseStream.from_dict(info_reports_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


