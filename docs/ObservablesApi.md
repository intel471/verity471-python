# verity471.ObservablesApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_observables_stream**](ObservablesApi.md#get_observables_stream) | **GET** /integrations/observables/v1/observables/stream | Retrieve a stream of observables


# **get_observables_stream**
> ObservableStreamPage get_observables_stream(observable, type=type, var_from=var_from, until=until, size=size, cursor=cursor)

Retrieve a stream of observables

Get observable stream.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.observable_stream_page import ObservableStreamPage
from verity471.models.observable_type import ObservableType
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
    api_instance = verity471.ObservablesApi(api_client)
    observable = 'example.com' # str | Search by observable value.
    type = verity471.ObservableType() # ObservableType | Search by observable type. (optional)
    var_from = 1627776000000 # int | UNIX timestamp(in milliseconds) (optional)
    until = 1627776000000 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Retrieve a stream of observables
        api_response = api_instance.get_observables_stream(observable, type=type, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ObservablesApi->get_observables_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservablesApi->get_observables_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observable** | **str**| Search by observable value. | 
 **type** | [**ObservableType**](.md)| Search by observable type. | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ObservableStreamPage**](ObservableStreamPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

