# IntegrationResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**cookies_available** | **bool** | Whether the resource includes cookies | [optional] 
**id** | **str** | Resource id | 
**infostealer** | [**ResourceInfostealerInfo**](ResourceInfostealerInfo.md) |  | [optional] 
**link** | **str** | URL or domain of the site or service the resource&#39;s data is for | [optional] 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 
**login_available** | **bool** | Whether the resource includes a login (username or email) | [optional] 
**marketplace_id** | **str** | External marketplace id | 
**name** | **str** | Name of the site or service the resource&#39;s data is for, usually a domain (e.g. example.com) | [optional] 
**others** | **Dict[str, str]** |  | [optional] 
**password_available** | **bool** | Whether the resource includes a password | [optional] 
**product_id** | **str** | Id of the product this resource belongs to. Fetch it with &#x60;GET /products/{product_id}&#x60; | [optional] 
**product_info** | [**ResourceProductInfo**](ResourceProductInfo.md) |  | [optional] 
**stolen_data** | [**ResourceOtherInfo**](ResourceOtherInfo.md) |  | [optional] 

## Example

```python
from verity471.models.integration_resource_response import IntegrationResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationResourceResponse from a JSON string
integration_resource_response_instance = IntegrationResourceResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationResourceResponse.to_json())

# convert the object into a dict
integration_resource_response_dict = integration_resource_response_instance.to_dict()
# create an instance of IntegrationResourceResponse from a dict
integration_resource_response_from_dict = IntegrationResourceResponse.from_dict(integration_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


