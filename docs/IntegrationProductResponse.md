# IntegrationProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountDetails**](AccountDetails.md) |  | [optional] 
**activity** | [**Activity**](Activity.md) |  | 
**article** | [**ArticleDetails**](ArticleDetails.md) |  | [optional] 
**bank** | [**BankDetails**](BankDetails.md) |  | [optional] 
**bot** | [**BotDetails**](BotDetails.md) |  | [optional] 
**card** | [**CardDetails**](CardDetails.md) |  | [optional] 
**database** | [**DatabaseDetails**](DatabaseDetails.md) |  | [optional] 
**description** | **str** | Product description | [optional] 
**digital_good** | [**DigitalGoodDetails**](DigitalGoodDetails.md) |  | [optional] 
**drug** | [**DrugDetails**](DrugDetails.md) |  | [optional] 
**exploit** | [**ExploitDetails**](ExploitDetails.md) |  | [optional] 
**id** | **str** | External product id | 
**kind** | **str** | Product kind. A kind the API types (the &#x60;kind&#x60; filter values of &#x60;/products/stream&#x60;) has its own fields in the field named after it, e.g. &#x60;card&#x60;; any other value is a kind not typed yet, with no such field | 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 
**marketplace_id** | **str** | External marketplace id | 
**name** | **str** | Product name as given by the listing | [optional] 
**others** | **Dict[str, str]** |  | [optional] 
**paypal** | [**PaypalDetails**](PaypalDetails.md) |  | [optional] 
**personal_info** | [**PersonalInfoDetails**](PersonalInfoDetails.md) |  | [optional] 
**price** | [**List[PriceEntry]**](PriceEntry.md) | Listed price, one entry per currency the listing gives (e.g. USD, BTC, XMR) | [optional] 
**product** | [**ProductMeta**](ProductMeta.md) |  | [optional] 
**proxy** | [**ProxyDetails**](ProxyDetails.md) |  | [optional] 
**real_document** | [**RealDocumentDetails**](RealDocumentDetails.md) |  | [optional] 
**shop** | [**ShopDetails**](ShopDetails.md) |  | [optional] 
**title** | **str** | Product title | 
**vendor_id** | **str** | External vendor id | [optional] 
**vendor_name** | **str** | Vendor name | [optional] 

## Example

```python
from verity471.models.integration_product_response import IntegrationProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationProductResponse from a JSON string
integration_product_response_instance = IntegrationProductResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationProductResponse.to_json())

# convert the object into a dict
integration_product_response_dict = integration_product_response_instance.to_dict()
# create an instance of IntegrationProductResponse from a dict
integration_product_response_from_dict = IntegrationProductResponse.from_dict(integration_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


