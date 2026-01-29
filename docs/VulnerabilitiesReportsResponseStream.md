# VulnerabilitiesReportsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of total Vulnerabilities reports matching the query | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**reports** | [**List[VulnerabilitiesReportDetailsResponseStream]**](VulnerabilitiesReportDetailsResponseStream.md) | List of Vulnerabilities reports in the current batch | [optional] 

## Example

```python
from verity471.models.vulnerabilities_reports_response_stream import VulnerabilitiesReportsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerabilitiesReportsResponseStream from a JSON string
vulnerabilities_reports_response_stream_instance = VulnerabilitiesReportsResponseStream.from_json(json)
# print the JSON string representation of the object
print(VulnerabilitiesReportsResponseStream.to_json())

# convert the object into a dict
vulnerabilities_reports_response_stream_dict = vulnerabilities_reports_response_stream_instance.to_dict()
# create an instance of VulnerabilitiesReportsResponseStream from a dict
vulnerabilities_reports_response_stream_from_dict = VulnerabilitiesReportsResponseStream.from_dict(vulnerabilities_reports_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


