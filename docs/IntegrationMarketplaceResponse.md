# IntegrationMarketplaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**alias** | **str** | Marketplace alias | [optional] 
**description** | **str** | Marketplace description | [optional] 
**id** | **str** | External marketplace id | 
**is_active** | **bool** | Whether the marketplace is currently active. Sources uses the inverse flag, &#x60;is_inactive&#x60; | [optional] 
**link** | **str** | Marketplace url | [optional] 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 
**name** | **str** | Marketplace display name, falls back to the marketplace alias | 
**tier** | **int** | Marketplace tier level | [optional] 

## Example

```python
from verity471.models.integration_marketplace_response import IntegrationMarketplaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationMarketplaceResponse from a JSON string
integration_marketplace_response_instance = IntegrationMarketplaceResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationMarketplaceResponse.to_json())

# convert the object into a dict
integration_marketplace_response_dict = integration_marketplace_response_instance.to_dict()
# create an instance of IntegrationMarketplaceResponse from a dict
integration_marketplace_response_from_dict = IntegrationMarketplaceResponse.from_dict(integration_marketplace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


