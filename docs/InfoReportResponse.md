# InfoReportResponse

Minimal schema for inforep report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_subject_of_report** | [**List[ActorSubjectOfReport]**](ActorSubjectOfReport.md) | List of actors who are the subject of the report | [optional] 
**assessment** | [**Assessment**](Assessment.md) |  | 
**attachments** | [**List[ReportAttachment]**](ReportAttachment.md) | List of attachments related to the report | [optional] 
**body** | **str** | Raw report text. This field may be omitted in streaming and UI responses when content exceeds the configured maximum size; fetch full report by ID if needed. | [optional] 
**body_translated** | **str** | Raw report text translated to english. This field may be omitted when content exceeds the configured maximum size. | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**derived_entities** | [**List[Entities]**](Entities.md) | List of entities derived from the report | [optional] 
**entities** | [**List[Entities]**](Entities.md) | List of entities mentioned in the report | [optional] 
**executive_summary** | **str** | Executive summary | 
**id** | **str** | Unique identifier of the report | 
**information_ts** | **str** | Timestamp of the information contained in the report | 
**is_sensitive_source** | **bool** | Indicates if the report contains sensitive source derived information | 
**is_truncated** | **bool** | True when the body field was omitted due to exceeding size limit; fetch full report by ID if needed | [optional] 
**last_updated_ts** | **str** | Timestamp of last report update | 
**links** | [**Links**](Links.md) |  | 
**locations** | [**List[ReportLocation]**](ReportLocation.md) | List of locations related to the report | [optional] 
**motivation** | [**List[Motivation]**](Motivation.md) | List of motivations related to the report | [optional] 
**related_reports** | [**List[ReportContent]**](ReportContent.md) | List of related reports connected to this report | [optional] 
**released_ts** | **str** | Timestamp when the report was published last time | 
**researcher_comments** | **str** | Researcher comments | 
**source_characterization** | **str** | Characterization of the source of the report | 
**title** | **str** | Title of the report | 
**type** | **str** | Type of the report | 
**victims** | [**List[ReportsVictimResponse]**](ReportsVictimResponse.md) | List of purported victims mentioned in the report | [optional] 

## Example

```python
from verity471.models.info_report_response import InfoReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InfoReportResponse from a JSON string
info_report_response_instance = InfoReportResponse.from_json(json)
# print the JSON string representation of the object
print(InfoReportResponse.to_json())

# convert the object into a dict
info_report_response_dict = info_report_response_instance.to_dict()
# create an instance of InfoReportResponse from a dict
info_report_response_from_dict = InfoReportResponse.from_dict(info_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


