# AttachmentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_highlights** | **List[str]** |  | [optional] 
**attachment_original_url** | **str** |  | [optional] 
**classification** | [**AttachmentClassification**](AttachmentClassification.md) |  | [optional] 
**dimensions** | **str** |  | [optional] 
**file_available** | **bool** |  | 
**file_hash** | **str** |  | 
**file_name** | **str** |  | 
**file_size** | **int** |  | 
**file_url** | **str** |  | [optional] 
**highlights** | [**List[Highlight]**](Highlight.md) |  | [optional] 
**id** | **str** |  | 
**is_not_image** | **bool** |  | 
**mime_type** | **str** |  | 
**original_height** | **int** |  | [optional] 
**original_width** | **int** |  | [optional] 
**processing_status** | [**ProcessingStatus**](ProcessingStatus.md) |  | 
**recognized_logos** | **str** |  | [optional] 
**recognized_text** | **str** |  | [optional] 
**reporting_status** | [**ReportingStatus**](ReportingStatus.md) |  | 
**source_entity_id** | **str** |  | 
**thumbnail_available** | **bool** |  | 
**thumbnail_height** | **int** |  | [optional] 
**thumbnail_width** | **int** |  | [optional] 
**webp_available** | **bool** |  | 

## Example

```python
from verity471.models.attachment_data import AttachmentData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentData from a JSON string
attachment_data_instance = AttachmentData.from_json(json)
# print the JSON string representation of the object
print(AttachmentData.to_json())

# convert the object into a dict
attachment_data_dict = attachment_data_instance.to_dict()
# create an instance of AttachmentData from a dict
attachment_data_from_dict = AttachmentData.from_dict(attachment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


