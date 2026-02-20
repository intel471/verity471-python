# verity471.WatchersApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_watcher_groups**](WatchersApi.md#get_watcher_groups) | **GET** /integrations/watchers/v1/watcher-groups | Get list of watcher groups for user
[**get_watchers**](WatchersApi.md#get_watchers) | **GET** /integrations/watchers/v1/watchers | Get list of watchers for the current user


# **get_watcher_groups**
> GetWatcherGroupResponseWrapper get_watcher_groups(watcher_group_id=watcher_group_id, watcher_group_type=watcher_group_type, name=name)

Get list of watcher groups for user

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_watcher_group_response_wrapper import GetWatcherGroupResponseWrapper
from verity471.models.watcher_group_type import WatcherGroupType
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
    api_instance = verity471.WatchersApi(api_client)
    watcher_group_id = 56 # int | Enables returning only watchers for specific group (optional)
    watcher_group_type = verity471.WatcherGroupType() # WatcherGroupType | Enables filtering by group type (optional)
    name = 'name_example' # str | Filter results based on watcher group name (optional)

    try:
        # Get list of watcher groups for user
        api_response = api_instance.get_watcher_groups(watcher_group_id=watcher_group_id, watcher_group_type=watcher_group_type, name=name)
        print("The response of WatchersApi->get_watcher_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchersApi->get_watcher_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_group_id** | **int**| Enables returning only watchers for specific group | [optional] 
 **watcher_group_type** | [**WatcherGroupType**](.md)| Enables filtering by group type | [optional] 
 **name** | **str**| Filter results based on watcher group name | [optional] 

### Return type

[**GetWatcherGroupResponseWrapper**](GetWatcherGroupResponseWrapper.md)

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

# **get_watchers**
> GetWatcherResponseWrapper get_watchers(watcher_id=watcher_id, watcher_group_id=watcher_group_id, dsl_query=dsl_query, watcher_group_type=watcher_group_type, name=name)

Get list of watchers for the current user

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_watcher_response_wrapper import GetWatcherResponseWrapper
from verity471.models.watcher_group_type import WatcherGroupType
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
    api_instance = verity471.WatchersApi(api_client)
    watcher_id = 56 # int | Enables returning only specific watcher (optional)
    watcher_group_id = 56 # int | Enables returning only watchers for specific group (optional)
    dsl_query = 'dsl_query_example' # str | Enables returning watchers with specific DSL query (optional)
    watcher_group_type = verity471.WatcherGroupType() # WatcherGroupType | Enables filtering by group type (optional)
    name = 'name_example' # str | Filter results based on watcher name (optional)

    try:
        # Get list of watchers for the current user
        api_response = api_instance.get_watchers(watcher_id=watcher_id, watcher_group_id=watcher_group_id, dsl_query=dsl_query, watcher_group_type=watcher_group_type, name=name)
        print("The response of WatchersApi->get_watchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchersApi->get_watchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_id** | **int**| Enables returning only specific watcher | [optional] 
 **watcher_group_id** | **int**| Enables returning only watchers for specific group | [optional] 
 **dsl_query** | **str**| Enables returning watchers with specific DSL query | [optional] 
 **watcher_group_type** | [**WatcherGroupType**](.md)| Enables filtering by group type | [optional] 
 **name** | **str**| Filter results based on watcher name | [optional] 

### Return type

[**GetWatcherResponseWrapper**](GetWatcherResponseWrapper.md)

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

