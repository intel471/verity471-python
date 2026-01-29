# verity471.GIRsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_of_girs_in_a_hierarchical_structure**](GIRsApi.md#get_list_of_girs_in_a_hierarchical_structure) | **GET** /integrations/girs/v1/girs/tree | 


# **get_list_of_girs_in_a_hierarchical_structure**
> GirsTreeResponse get_list_of_girs_in_a_hierarchical_structure()

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.girs_tree_response import GirsTreeResponse
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
    api_instance = verity471.GIRsApi(api_client)

    try:
        api_response = api_instance.get_list_of_girs_in_a_hierarchical_structure()
        print("The response of GIRsApi->get_list_of_girs_in_a_hierarchical_structure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GIRsApi->get_list_of_girs_in_a_hierarchical_structure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GirsTreeResponse**](GirsTreeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

