# verity471.ActorsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actors_stream**](ActorsApi.md#get_actors_stream) | **GET** /integrations/actors/v1/actors/stream | Retrieve a stream of actors


# **get_actors_stream**
> ActorStreamPage get_actors_stream(actor, forum=forum, var_from=var_from, until=until, service_type=service_type, size=size, cursor=cursor)

Retrieve a stream of actors

Get actor stream.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.actor_stream_page import ActorStreamPage
from verity471.models.chat_server_type import ChatServerType
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
    api_instance = verity471.ActorsApi(api_client)
    actor = 'example_actor' # str | Search by actor handle.
    forum = 'forum_example' # str | Apply filtering by forum display name. (optional)
    var_from = 1627776000000 # int | Apply filtering by from timestamp - UNIX timestamp(in milliseconds) (optional)
    until = 1627776000000 # int | Apply filtering by until timestamp - UNIX timestamp(in milliseconds) (optional)
    service_type = verity471.ChatServerType() # ChatServerType | Search by specific service for messages. Example: Telegram (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Retrieve a stream of actors
        api_response = api_instance.get_actors_stream(actor, forum=forum, var_from=var_from, until=until, service_type=service_type, size=size, cursor=cursor)
        print("The response of ActorsApi->get_actors_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->get_actors_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor** | **str**| Search by actor handle. | 
 **forum** | **str**| Apply filtering by forum display name. | [optional] 
 **var_from** | **int**| Apply filtering by from timestamp - UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| Apply filtering by until timestamp - UNIX timestamp(in milliseconds) | [optional] 
 **service_type** | [**ChatServerType**](.md)| Search by specific service for messages. Example: Telegram | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ActorStreamPage**](ActorStreamPage.md)

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

