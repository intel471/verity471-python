# BreachAlertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_or_group** | **str** | Actor or group name | 
**body** | **str** | Main content body of the report. This field may be omitted in streaming responses when content exceeds the configured maximum size; fetch full report by ID if needed. | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**confidence** | [**Confidence**](Confidence.md) |  | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**id** | **str** | Unique identifier of the report | 
**information_ts** | **str** | Timestamp of the information contained in the report | 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | [optional] 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 
**last_updated_ts** | **str** | Report last update datetime | 
**links** | [**Links**](Links.md) |  | 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports connected to this report | [optional] 
**released_ts** | **str** | Timestamp when the report was published last time | 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**title** | **str** | Title of the report | 
**type** | **str** | Type of the report | 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 

## Example

```python
from verity471.models.breach_alert_response import BreachAlertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BreachAlertResponse from a JSON string
breach_alert_response_instance = BreachAlertResponse.from_json(json)
# print the JSON string representation of the object
print(BreachAlertResponse.to_json())

# convert the object into a dict
breach_alert_response_dict = breach_alert_response_instance.to_dict()
# create an instance of BreachAlertResponse from a dict
breach_alert_response_from_dict = BreachAlertResponse.from_dict(breach_alert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


