# GeopolReportsResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adversary_profile_count** | **int** | Count of Adversary Profile reports | 
**count** | **int** | Number of total Geopol reports matching the query | 
**cursor_next** | **str** | Stream position identifier to continue scrolling from | [optional] 
**intelligence_bulletin_count** | **int** | Count of Intelligence Bulletin reports | 
**intelligence_estimate_count** | **int** | Count of Intelligence Estimate reports | 
**intelligence_summary_count** | **int** | Count of Intelligence Summary reports | 
**reports** | [**List[GeopolReportDetailsResponse]**](GeopolReportDetailsResponse.md) | List of Geopol reports in the current batch | [optional] 
**sigact_count** | **int** | Count of Significant Activity Report reports | 
**spot_count** | **int** | Count of Geopol Spot Report reports | 
**tension_point_profile_count** | **int** | Count of Tension Point Profile reports | 
**threat_brief_count** | **int** | Count of Threat Brief reports | 

## Example

```python
from verity471.models.geopol_reports_response_stream import GeopolReportsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of GeopolReportsResponseStream from a JSON string
geopol_reports_response_stream_instance = GeopolReportsResponseStream.from_json(json)
# print the JSON string representation of the object
print(GeopolReportsResponseStream.to_json())

# convert the object into a dict
geopol_reports_response_stream_dict = geopol_reports_response_stream_instance.to_dict()
# create an instance of GeopolReportsResponseStream from a dict
geopol_reports_response_stream_from_dict = GeopolReportsResponseStream.from_dict(geopol_reports_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


