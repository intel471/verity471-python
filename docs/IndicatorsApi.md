# verity471.IndicatorsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_indicator_by_id**](IndicatorsApi.md#get_indicator_by_id) | **GET** /integrations/indicators/v1/indicators/{id} | Get indicator by id
[**get_indicators_stream**](IndicatorsApi.md#get_indicators_stream) | **GET** /integrations/indicators/v1/indicators/stream | Stream indicators using a cursor


# **get_indicator_by_id**
> IntegrationsIndicator get_indicator_by_id(id)

Get indicator by id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.integrations_indicator import IntegrationsIndicator
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
    api_instance = verity471.IndicatorsApi(api_client)
    id = 'malware-indicator--6cc708b7-4d00-5ca9-8cbe-66bd69d17feb' # str | Id of the indicator

    try:
        # Get indicator by id
        api_response = api_instance.get_indicator_by_id(id)
        print("The response of IndicatorsApi->get_indicator_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_indicator_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the indicator | 

### Return type

[**IntegrationsIndicator**](IntegrationsIndicator.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators_stream**
> IndicatorsStream get_indicators_stream(type=type, threat_type=threat_type, confidence=confidence, cursor=cursor, text_filter=text_filter, malware_id=malware_id, malware_family_id=malware_family_id, malware_family_name=malware_family_name, girs=girs, size=size, var_from=var_from, until=until)

Stream indicators using a cursor

Indicators sorted in ascending order of processed time.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.indicators_stream import IndicatorsStream
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
    api_instance = verity471.IndicatorsApi(api_client)
    type = 'type_example' # str | Search indicators by type (optional)
    threat_type = 'malware' # str | Search indicators by threat type (optional)
    confidence = 'confidence_example' # str | Search indicators by confidence (optional)
    cursor = 'NTg2ZDYwOWUtNzhmMS00MDY5LTg3M2QtYTI5MWRjNzBhNTYyOjE3MDU0NTA5MDgwMDA6ZmM5NGY1NGM2MzZlOTc2ZmFhZmVjMTAwMmY2Y2U1OWIxYWY0ZjcxZg==' # str | Continue scrolling from cursor (optional)
    text_filter = 'Georgia' # str | Free text indicator search (all fields included) (optional)
    malware_id = 'malware--61617350-6466-5fd8-8272-1266be341a1e' # str | Search indicators by malware id (optional)
    malware_family_id = 'malware-family--92eb4b5f-cfc5-5460-bd43-53fae450ac9a' # str | Search indicators by malware family id (optional)
    malware_family_name = 'dreambot' # str | Search indicators by malware family (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), `my_girs` or `company_pirs`. Using multiple value will return result based on the aggregated GIR list (optional)
    size = 1000 # int | The size of the page to be returned. Max size: `1000` (optional) (default to 1000)
    var_from = 56 # int | Long unix timestamp in milliseconds. Search data starting from given `activity.first_seen_ts` and `activity.last_seen_ts` (including). Example - `1627776000000` (optional)
    until = 56 # int | Long unix timestamp in milliseconds. Search data ending before given `activity.first_seen_ts` and `activity.last_seen_ts` (excluding). Example - `1627776000000` (optional)

    try:
        # Stream indicators using a cursor
        api_response = api_instance.get_indicators_stream(type=type, threat_type=threat_type, confidence=confidence, cursor=cursor, text_filter=text_filter, malware_id=malware_id, malware_family_id=malware_family_id, malware_family_name=malware_family_name, girs=girs, size=size, var_from=var_from, until=until)
        print("The response of IndicatorsApi->get_indicators_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_indicators_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Search indicators by type | [optional] 
 **threat_type** | **str**| Search indicators by threat type | [optional] 
 **confidence** | **str**| Search indicators by confidence | [optional] 
 **cursor** | **str**| Continue scrolling from cursor | [optional] 
 **text_filter** | **str**| Free text indicator search (all fields included) | [optional] 
 **malware_id** | **str**| Search indicators by malware id | [optional] 
 **malware_family_id** | **str**| Search indicators by malware family id | [optional] 
 **malware_family_name** | **str**| Search indicators by malware family | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), &#x60;my_girs&#x60; or &#x60;company_pirs&#x60;. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **size** | **int**| The size of the page to be returned. Max size: &#x60;1000&#x60; | [optional] [default to 1000]
 **var_from** | **int**| Long unix timestamp in milliseconds. Search data starting from given &#x60;activity.first_seen_ts&#x60; and &#x60;activity.last_seen_ts&#x60; (including). Example - &#x60;1627776000000&#x60; | [optional] 
 **until** | **int**| Long unix timestamp in milliseconds. Search data ending before given &#x60;activity.first_seen_ts&#x60; and &#x60;activity.last_seen_ts&#x60; (excluding). Example - &#x60;1627776000000&#x60; | [optional] 

### Return type

[**IndicatorsStream**](IndicatorsStream.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

