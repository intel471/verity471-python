# RealDocumentDetails

Fields of a `real_document` product; set only when `kind` is `real_document`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**DocumentBasicInfo**](DocumentBasicInfo.md) |  | [optional] 
**victim** | [**VictimInfo**](VictimInfo.md) |  | [optional] 

## Example

```python
from verity471.models.real_document_details import RealDocumentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RealDocumentDetails from a JSON string
real_document_details_instance = RealDocumentDetails.from_json(json)
# print the JSON string representation of the object
print(RealDocumentDetails.to_json())

# convert the object into a dict
real_document_details_dict = real_document_details_instance.to_dict()
# create an instance of RealDocumentDetails from a dict
real_document_details_from_dict = RealDocumentDetails.from_dict(real_document_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


