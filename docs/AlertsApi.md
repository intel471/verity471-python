# verity471.AlertsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alerts_stream**](AlertsApi.md#get_alerts_stream) | **GET** /integrations/watchers/v1/alerts/stream | Get alerts for the current user in a stream way
[**put_alerts_id_status**](AlertsApi.md#put_alerts_id_status) | **PUT** /integrations/watchers/v1/alerts/{id}/{status} | Change status of an alert


# **get_alerts_stream**
> StreamingAlertsResponse get_alerts_stream(cursor=cursor, size=size, var_from=var_from, until=until, watcher_group_ids=watcher_group_ids, watcher_ids=watcher_ids, statuses=statuses, is_trashed_included=is_trashed_included)

Get alerts for the current user in a stream way

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.streaming_alerts_response import StreamingAlertsResponse
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
    api_instance = verity471.AlertsApi(api_client)
    cursor = 'cursor_example' # str | Cursor to be used to fetch next batch from stream (optional)
    size = 1000 # int | Size of the batch to return. Defaults to 1000. Max value 1000 (if size is bigger than this onlyfirst 1000 alerts will be returned) (optional) (default to 1000)
    var_from = 56 # int | Long unix time. Example - 1627776000000 (By timestamp) (optional)
    until = 56 # int | Long unix time. Example - 1627776000000 (By timestamp) (optional)
    watcher_group_ids = '121,3553,5334' # str | Comma separated watcher group ids to filter alerts. (optional)
    watcher_ids = '121,3553,5334' # str | Comma separated watcher ids to filter alerts. (optional)
    statuses = 'generated,needs_action,completed' # str | Comma separated statuses to filter alerts. Allowed values are generated, needs_action, in_progress, completed and false_positive. (optional)
    is_trashed_included = False # bool | Include trashed alerts in the response. Defaults to false. (optional) (default to False)

    try:
        # Get alerts for the current user in a stream way
        api_response = api_instance.get_alerts_stream(cursor=cursor, size=size, var_from=var_from, until=until, watcher_group_ids=watcher_group_ids, watcher_ids=watcher_ids, statuses=statuses, is_trashed_included=is_trashed_included)
        print("The response of AlertsApi->get_alerts_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Cursor to be used to fetch next batch from stream | [optional] 
 **size** | **int**| Size of the batch to return. Defaults to 1000. Max value 1000 (if size is bigger than this onlyfirst 1000 alerts will be returned) | [optional] [default to 1000]
 **var_from** | **int**| Long unix time. Example - 1627776000000 (By timestamp) | [optional] 
 **until** | **int**| Long unix time. Example - 1627776000000 (By timestamp) | [optional] 
 **watcher_group_ids** | **str**| Comma separated watcher group ids to filter alerts. | [optional] 
 **watcher_ids** | **str**| Comma separated watcher ids to filter alerts. | [optional] 
 **statuses** | **str**| Comma separated statuses to filter alerts. Allowed values are generated, needs_action, in_progress, completed and false_positive. | [optional] 
 **is_trashed_included** | **bool**| Include trashed alerts in the response. Defaults to false. | [optional] [default to False]

### Return type

[**StreamingAlertsResponse**](StreamingAlertsResponse.md)

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

# **put_alerts_id_status**
> put_alerts_id_status(id, status)

Change status of an alert

### Example

* Basic Authentication (basicAuth):

```python
import verity471
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
    api_instance = verity471.AlertsApi(api_client)
    id = 56 # int | 
    status = 'status_example' # str | 

    try:
        # Change status of an alert
        api_instance.put_alerts_id_status(id, status)
    except Exception as e:
        print("Exception when calling AlertsApi->put_alerts_id_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **status** | **str**|  | 

### Return type

void (empty response body)

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

