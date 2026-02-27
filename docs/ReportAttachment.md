# ReportAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the attachment | [optional] 
**file_name** | **str** | Name of the attachment file | 
**file_size** | **int** | Size of the attachment file in bytes | 
**malicious** | **bool** | Indicates if the attachment is malicious | 
**mime_type** | **str** | MIME type of the attachment | 
**url** | **str** | URL to download the attachment | 

## Example

```python
from verity471.models.report_attachment import ReportAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAttachment from a JSON string
report_attachment_instance = ReportAttachment.from_json(json)
# print the JSON string representation of the object
print(ReportAttachment.to_json())

# convert the object into a dict
report_attachment_dict = report_attachment_instance.to_dict()
# create an instance of ReportAttachment from a dict
report_attachment_from_dict = ReportAttachment.from_dict(report_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


