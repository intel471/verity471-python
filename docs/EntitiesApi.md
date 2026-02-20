# verity471.EntitiesApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entities_stream**](EntitiesApi.md#get_entities_stream) | **GET** /integrations/entities/v1/entities/stream | Retrieve a stream of entities


# **get_entities_stream**
> EntityStreamPage get_entities_stream(entity, type=type, var_from=var_from, until=until, size=size, cursor=cursor)

Retrieve a stream of entities

Get entity stream.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.entity_stream_page import EntityStreamPage
from verity471.models.entity_type import EntityType
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
    api_instance = verity471.EntitiesApi(api_client)
    entity = 'intel.com' # str | The entity value to search for. Supports partial match
    type = verity471.EntityType() # EntityType | Filter entity type (optional)
    var_from = 1627776000000 # int | Apply filtering by from timestamp - UNIX timestamp(in milliseconds) (optional)
    until = 1627776000000 # int | Apply filtering by until timestamp - UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Retrieve a stream of entities
        api_response = api_instance.get_entities_stream(entity, type=type, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of EntitiesApi->get_entities_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entities_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The entity value to search for. Supports partial match | 
 **type** | [**EntityType**](.md)| Filter entity type | [optional] 
 **var_from** | **int**| Apply filtering by from timestamp - UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| Apply filtering by until timestamp - UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**EntityStreamPage**](EntityStreamPage.md)

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

