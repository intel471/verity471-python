# verity471.MarketplacesApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_marketplaces_marketplace_id**](MarketplacesApi.md#get_marketplaces_marketplace_id) | **GET** /integrations/marketplaces/v1/marketplaces/{marketplace_id} | Get a marketplace by id
[**get_marketplaces_stream**](MarketplacesApi.md#get_marketplaces_stream) | **GET** /integrations/marketplaces/v1/marketplaces/stream | Get marketplaces (stream)
[**get_products_product_id**](MarketplacesApi.md#get_products_product_id) | **GET** /integrations/marketplaces/v1/products/{product_id} | Get a product by id
[**get_products_stream**](MarketplacesApi.md#get_products_stream) | **GET** /integrations/marketplaces/v1/products/stream | Get products (stream)
[**get_resources_resource_id**](MarketplacesApi.md#get_resources_resource_id) | **GET** /integrations/marketplaces/v1/resources/{resource_id} | Get a resource by id
[**get_resources_stream**](MarketplacesApi.md#get_resources_stream) | **GET** /integrations/marketplaces/v1/resources/stream | Get resources (stream)
[**get_vendors_stream**](MarketplacesApi.md#get_vendors_stream) | **GET** /integrations/marketplaces/v1/vendors/stream | Get vendors (stream)
[**get_vendors_vendor_id**](MarketplacesApi.md#get_vendors_vendor_id) | **GET** /integrations/marketplaces/v1/vendors/{vendor_id} | Get a vendor by id


# **get_marketplaces_marketplace_id**
> IntegrationMarketplaceResponse get_marketplaces_marketplace_id(marketplace_id)

Get a marketplace by id

Get marketplace by marketplace id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.integration_marketplace_response import IntegrationMarketplaceResponse
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    marketplace_id = 'marketplace-website--d5f2e739-d757-5f68-86e8-def0632d7bc5' # str | 

    try:
        # Get a marketplace by id
        api_response = api_instance.get_marketplaces_marketplace_id(marketplace_id)
        print("The response of MarketplacesApi->get_marketplaces_marketplace_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_marketplaces_marketplace_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_id** | **str**|  | 

### Return type

[**IntegrationMarketplaceResponse**](IntegrationMarketplaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The marketplace |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplaces_stream**
> MarketplacesStreamingPage get_marketplaces_stream(text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)

Get marketplaces (stream)

Returns a cursor-paginated list of marketplaces matching the filters. Each item has the same shape as GET /marketplaces/{marketplace_id}. Results are ordered by ingestion time, oldest first.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.marketplaces_streaming_page import MarketplacesStreamingPage
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search based on a keyword (optional)
    var_from = 56 # int | Inclusive lower bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no lower bound. (optional)
    until = 56 # int | Inclusive upper bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no upper bound. (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get marketplaces (stream)
        api_response = api_instance.get_marketplaces_stream(text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of MarketplacesApi->get_marketplaces_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_marketplaces_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search based on a keyword | [optional] 
 **var_from** | **int**| Inclusive lower bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no lower bound. | [optional] 
 **until** | **int**| Inclusive upper bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no upper bound. | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**MarketplacesStreamingPage**](MarketplacesStreamingPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of marketplaces and the cursor for the next page |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_product_id**
> IntegrationProductResponse get_products_product_id(product_id)

Get a product by id

Get product details by product id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.integration_product_response import IntegrationProductResponse
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    product_id = 'marketplace-product--e6d28f37-a118-54ef-889c-20b1f65d33c4' # str | 

    try:
        # Get a product by id
        api_response = api_instance.get_products_product_id(product_id)
        print("The response of MarketplacesApi->get_products_product_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_products_product_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**IntegrationProductResponse**](IntegrationProductResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The product; its fields depend on &#x60;kind&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_stream**
> ProductsStreamingPage get_products_stream(text_filter=text_filter, var_from=var_from, until=until, kind=kind, marketplace_id=marketplace_id, vendor_id=vendor_id, size=size, cursor=cursor)

Get products (stream)

Returns a cursor-paginated list of products matching the filters. Each item has the same shape as GET /products/{product_id}. Results are ordered by ingestion time, oldest first.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.product_kind import ProductKind
from verity471.models.products_streaming_page import ProductsStreamingPage
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search based on a keyword (optional)
    var_from = 56 # int | Inclusive lower bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no lower bound. (optional)
    until = 56 # int | Inclusive upper bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no upper bound. (optional)
    kind = verity471.ProductKind() # ProductKind | Filter by product kind. An unknown value returns 400 (optional)
    marketplace_id = 'marketplace_id_example' # str | Filter by marketplace id (optional)
    vendor_id = 'vendor_id_example' # str | Filter by vendor id (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get products (stream)
        api_response = api_instance.get_products_stream(text_filter=text_filter, var_from=var_from, until=until, kind=kind, marketplace_id=marketplace_id, vendor_id=vendor_id, size=size, cursor=cursor)
        print("The response of MarketplacesApi->get_products_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_products_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search based on a keyword | [optional] 
 **var_from** | **int**| Inclusive lower bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no lower bound. | [optional] 
 **until** | **int**| Inclusive upper bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no upper bound. | [optional] 
 **kind** | [**ProductKind**](.md)| Filter by product kind. An unknown value returns 400 | [optional] 
 **marketplace_id** | **str**| Filter by marketplace id | [optional] 
 **vendor_id** | **str**| Filter by vendor id | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ProductsStreamingPage**](ProductsStreamingPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of products and the cursor for the next page |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_resource_id**
> IntegrationResourceResponse get_resources_resource_id(resource_id)

Get a resource by id

Get resource by resource id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.integration_resource_response import IntegrationResourceResponse
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    resource_id = 'marketplace-resource--7145bf84-eabb-5a3f-8137-2c28b537f440' # str | 

    try:
        # Get a resource by id
        api_response = api_instance.get_resources_resource_id(resource_id)
        print("The response of MarketplacesApi->get_resources_resource_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_resources_resource_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**|  | 

### Return type

[**IntegrationResourceResponse**](IntegrationResourceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_stream**
> ResourcesStreamingPage get_resources_stream(text_filter=text_filter, var_from=var_from, until=until, marketplace_id=marketplace_id, size=size, cursor=cursor)

Get resources (stream)

Returns a cursor-paginated list of resources matching the filters. Each item has the same shape as GET /resources/{resource_id}. Results are ordered by ingestion time, oldest first.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.resources_streaming_page import ResourcesStreamingPage
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search based on a keyword (optional)
    var_from = 56 # int | Inclusive lower bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no lower bound. (optional)
    until = 56 # int | Inclusive upper bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no upper bound. (optional)
    marketplace_id = 'marketplace_id_example' # str | Filter by marketplace id (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get resources (stream)
        api_response = api_instance.get_resources_stream(text_filter=text_filter, var_from=var_from, until=until, marketplace_id=marketplace_id, size=size, cursor=cursor)
        print("The response of MarketplacesApi->get_resources_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_resources_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search based on a keyword | [optional] 
 **var_from** | **int**| Inclusive lower bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no lower bound. | [optional] 
 **until** | **int**| Inclusive upper bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no upper bound. | [optional] 
 **marketplace_id** | **str**| Filter by marketplace id | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ResourcesStreamingPage**](ResourcesStreamingPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of resources and the cursor for the next page |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors_stream**
> VendorsStreamingPage get_vendors_stream(text_filter=text_filter, var_from=var_from, until=until, marketplace_id=marketplace_id, size=size, cursor=cursor)

Get vendors (stream)

Returns a cursor-paginated list of vendors matching the filters. Each item has the same shape as GET /vendors/{vendor_id}. Results are ordered by ingestion time, oldest first.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.vendors_streaming_page import VendorsStreamingPage
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search based on a keyword (optional)
    var_from = 56 # int | Inclusive lower bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no lower bound. (optional)
    until = 56 # int | Inclusive upper bound on the entity's last-seen time (`activity.last_seen_ts`), as a UNIX timestamp in milliseconds. Omit for no upper bound. (optional)
    marketplace_id = 'marketplace_id_example' # str | Filter by marketplace id (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get vendors (stream)
        api_response = api_instance.get_vendors_stream(text_filter=text_filter, var_from=var_from, until=until, marketplace_id=marketplace_id, size=size, cursor=cursor)
        print("The response of MarketplacesApi->get_vendors_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_vendors_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search based on a keyword | [optional] 
 **var_from** | **int**| Inclusive lower bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no lower bound. | [optional] 
 **until** | **int**| Inclusive upper bound on the entity&#39;s last-seen time (&#x60;activity.last_seen_ts&#x60;), as a UNIX timestamp in milliseconds. Omit for no upper bound. | [optional] 
 **marketplace_id** | **str**| Filter by marketplace id | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**VendorsStreamingPage**](VendorsStreamingPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of vendors and the cursor for the next page |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors_vendor_id**
> IntegrationVendorResponse get_vendors_vendor_id(vendor_id)

Get a vendor by id

Get vendor by vendor id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.integration_vendor_response import IntegrationVendorResponse
from verity471.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.intel471.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verity471.Configuration(
    host = "https://api.intel471.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = verity471.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with verity471.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verity471.MarketplacesApi(api_client)
    vendor_id = 'marketplace-seller--103796cd-baa5-58a3-9c72-4029ec2bd3f2' # str | 

    try:
        # Get a vendor by id
        api_response = api_instance.get_vendors_vendor_id(vendor_id)
        print("The response of MarketplacesApi->get_vendors_vendor_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplacesApi->get_vendors_vendor_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**|  | 

### Return type

[**IntegrationVendorResponse**](IntegrationVendorResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The vendor |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

