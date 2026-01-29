# BreachAlertByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report | 
**type** | **str** | Type of the report | 
**title** | **str** | Title of the report | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**released_ts** | **str** | Timestamp when the report was published last time | 
**last_updated_ts** | **str** | Report last update datetime | 
**information_ts** | **str** | Timestamp of the information contained in the report | 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 
**actor_or_group** | **str** | Actor or group name | 
**body** | **str** | Main content body of the report. This field may be omitted in streaming responses when content exceeds the configured maximum size; fetch full report by ID if needed. | [optional] 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | [optional] 
**confidence** | [**Confidence**](Confidence.md) |  | 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 
**links** | [**Links**](Links.md) |  | 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports connected to this report | [optional] 

## Example

```python
from verity471.models.breach_alert_by_id_response import BreachAlertByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BreachAlertByIdResponse from a JSON string
breach_alert_by_id_response_instance = BreachAlertByIdResponse.from_json(json)
# print the JSON string representation of the object
print(BreachAlertByIdResponse.to_json())

# convert the object into a dict
breach_alert_by_id_response_dict = breach_alert_by_id_response_instance.to_dict()
# create an instance of BreachAlertByIdResponse from a dict
breach_alert_by_id_response_from_dict = BreachAlertByIdResponse.from_dict(breach_alert_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


