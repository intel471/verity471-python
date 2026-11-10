# ArticleBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access type given by the listing | [optional] 
**account_balance** | **str** | Balance as free text from the listing (e.g. &#x60;$1,234.50&#x60;, &#x60;150 USD&#x60;). The currency, when given, is part of the text | [optional] 
**account_type** | **str** | Account type given by the listing (e.g. personal, business) | [optional] 
**activation_region** | **str** |  | [optional] 
**additional_info** | **str** | Extra notes from the listing | [optional] 
**address** | **str** | Address given by the listing | [optional] 
**admin_type** | **str** | Admin/panel type or rank info. | [optional] 
**alexa_reach_rank** | **str** |  | [optional] 
**bulk_buying_options** | **List[str]** | Tiered bulk prices: quantity with total and per-unit price | [optional] 
**city** | **str** | City | [optional] 
**connection_type** | **str** | Access type (e.g. RDP, SSH). | [optional] 
**country** | **str** | Country associated with the listing | [optional] 
**cpr_score** | **str** | CPR score out of 10 (SEO metric, e.g. 0.1/10) | [optional] 
**cpu** | **int** | Number of CPU cores of the server | [optional] 
**denomination** | **str** | Face value or denomination where relevant. | [optional] 
**domain** | **str** | Domain name (proxies/sites). | [optional] 
**domain_authority** | **str** | Domain Authority score (SEO metric) | [optional] 
**driving_license_available** | **bool** | Whether a driving license is included | [optional] 
**driving_license_expire_date** | **str** | Driving license expiry date as given by the listing, not normalised | [optional] 
**edu_backlinks** | **str** | Number of backlinks from .edu sites, as listed: digits, sometimes with thousands separators (e.g. &#x60;1,341&#x60;) | [optional] 
**emails_number** | **str** |  | [optional] 
**escrow_available** | **bool** | Whether escrow is offered. | [optional] 
**escrow_info** | **str** | Escrow terms | [optional] 
**external_backlinks** | **str** | Number of external backlinks to the site (SEO metric), as listed: digits, sometimes with thousands separators (e.g. &#x60;1,341&#x60;) | [optional] 
**free_insurance_time** | **str** | Free replacement (insurance) period offered by the vendor (e.g. 15 Days) | [optional] 
**gender** | **str** | Gender of the person the data belongs to | [optional] 
**global_rank** | **str** |  | [optional] 
**google_directory_listed** | **bool** | Whether the site is listed in Google&#39;s directory | [optional] 
**gov_backlinks** | **str** | Number of backlinks from .gov sites, as listed: digits, sometimes with thousands separators (e.g. &#x60;1,341&#x60;) | [optional] 
**host_info** | **str** | Host software and version given by the listing | [optional] 
**hosting** | **str** | Hosting provider of the site or server (e.g. Hetzner Online GmbH) | [optional] 
**in_game_items** | [**InGameItems**](InGameItems.md) |  | [optional] 
**indexed_urls** | **str** | Number of the site&#39;s URLs indexed by search engines, as listed: digits, sometimes with thousands separators (e.g. &#x60;1,341&#x60;); -1 when unknown | [optional] 
**ip_blacklist** | **str** | IP blacklist status as given by the listing | [optional] 
**niche** | **str** | Vertical or niche (e.g. Banking) | [optional] 
**operating_system** | **str** | Victim OS. | [optional] 
**origin_country** | **str** | Country of origin for goods/data. | [optional] 
**page_authority** | **str** | Page Authority score (SEO metric) | [optional] 
**page_rank** | **str** | PageRank as given by the listing, usually out of 10 (e.g. 0/10) | [optional] 
**password** | **str** |  | [optional] 
**payment_method** | **str** | Accepted payment method(s). | [optional] 
**phone_number** | **str** | Phone number given by the listing | [optional] 
**ping** | **str** |  | [optional] 
**platform** | **str** | Platform the product is for | [optional] 
**port** | **int** | Port of the service (e.g. 587 for SMTP) | [optional] 
**pr_quality** | **str** | PageRank quality label (e.g. Very Weak) | [optional] 
**product_types** | **List[str]** | Product type tags given by the listing (e.g. Physical, Digital) | [optional] 
**provider** | **str** | Provider name | [optional] 
**proxy_score** | **int** |  | [optional] 
**proxy_type** | **str** | Proxy/RDP/SOCKS type. | [optional] 
**ram** | **str** | RAM of the server (e.g. 4 GB) | [optional] 
**referring_domains** | **str** | Number of domains linking to the site, as listed: digits, sometimes with thousands separators (e.g. &#x60;1,341&#x60;) | [optional] 
**region** | **str** | Region the product is for (e.g. GLOBAL, EUROPE) | [optional] 
**secure_sockets_layer** | **str** | Whether the site uses SSL, given as the scheme (e.g. https) | [optional] 
**seo_rank** | **str** | SEO rank score | [optional] 
**server** | **str** | Server given by the listing (e.g. a game or mail server) | [optional] 
**service** | **str** | Service name (e.g. a subscription) | [optional] 
**size** | **str** | Size as free text from the listing. Unrelated to the &#x60;size&#x60; query parameter, which sets the page size | [optional] 
**source** | **str** | Provenance label (e.g. hacked, stolen, created). | [optional] 
**spam_score** | **str** | Spam score as given by the listing (e.g. 0 / 18) | [optional] 
**speed** | **str** | Connection speed | [optional] 
**state** | **str** | State or region | [optional] 
**statement_date** | **str** | Statement date as given by the listing, not normalised | [optional] 
**stock_available** | **bool** | Whether stock is shown as available. | [optional] 
**topic** | **str** |  | [optional] 
**topic_value** | **str** | Topic value score (SEO metric) | [optional] 
**total_stock_price** | **float** | Total price of the stock. The listing gives no currency | [optional] 
**trust_metric** | **str** | Trust metric score (SEO metric) | [optional] 
**url_to_market** | **str** |  | [optional] 
**username** | **str** | Username of the account, usually masked | [optional] 
**verified_attributes** | **str** | Verification details, as free text | [optional] 
**visitors** | **str** | Traffic/visitor metric if listed. | [optional] 
**web_host_manager_available** | **bool** |  | [optional] 
**website** | **str** | Website the product gives access to | [optional] 
**works_on** | **str** | Devices or platforms the product works on (e.g. Windows, Android, PlayStation 5) | [optional] 
**zip** | **str** | Postal/ZIP code | [optional] 

## Example

```python
from verity471.models.article_basic_info import ArticleBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleBasicInfo from a JSON string
article_basic_info_instance = ArticleBasicInfo.from_json(json)
# print the JSON string representation of the object
print(ArticleBasicInfo.to_json())

# convert the object into a dict
article_basic_info_dict = article_basic_info_instance.to_dict()
# create an instance of ArticleBasicInfo from a dict
article_basic_info_from_dict = ArticleBasicInfo.from_dict(article_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


