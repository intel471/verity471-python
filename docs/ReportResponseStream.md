# ReportResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_alert_count** | **int** | Number of breach alert reports | 
**count** | **int** | Total number of reports | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**fintel_report_count** | **int** | Number of fintel reports | 
**geopol_report_count** | **int** | Number of geopol reports | 
**info_report_count** | **int** | Number of information reports | 
**malware_report_count** | **int** | Number of malware reports | 
**reports** | [**List[ReportContent]**](ReportContent.md) | List of detailed reports | [optional] 
**spot_report_count** | **int** | Number of spot reports | 
**vulnerability_report_count** | **int** | Number of vulnerability reports | 

## Example

```python
from verity471.models.report_response_stream import ReportResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResponseStream from a JSON string
report_response_stream_instance = ReportResponseStream.from_json(json)
# print the JSON string representation of the object
print(ReportResponseStream.to_json())

# convert the object into a dict
report_response_stream_dict = report_response_stream_instance.to_dict()
# create an instance of ReportResponseStream from a dict
report_response_stream_from_dict = ReportResponseStream.from_dict(report_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


