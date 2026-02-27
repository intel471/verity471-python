# verity471.CredentialsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credential_sets_accessed_urls_stream**](CredentialsApi.md#get_credential_sets_accessed_urls_stream) | **GET** /integrations/creds/v1/credential-sets/accessed-urls/stream | Credential set accessed url stream
[**get_credential_sets_id**](CredentialsApi.md#get_credential_sets_id) | **GET** /integrations/creds/v1/credential-sets/{id} | Get credential set by ID
[**get_credential_sets_stream**](CredentialsApi.md#get_credential_sets_stream) | **GET** /integrations/creds/v1/credential-sets/stream | Credential set stream
[**get_credentials_id**](CredentialsApi.md#get_credentials_id) | **GET** /integrations/creds/v1/credentials/{id} | Get credential by ID
[**get_credentials_occurrences_id**](CredentialsApi.md#get_credentials_occurrences_id) | **GET** /integrations/creds/v1/credentials/occurrences/{id} | Get credential occurrence by ID
[**get_credentials_occurrences_stream**](CredentialsApi.md#get_credentials_occurrences_stream) | **GET** /integrations/creds/v1/credentials/occurrences/stream | Credential occurrence stream
[**get_credentials_stream**](CredentialsApi.md#get_credentials_stream) | **GET** /integrations/creds/v1/credentials/stream | Credential stream


# **get_credential_sets_accessed_urls_stream**
> GetCredSetAccessedUrlResponseStream get_credential_sets_accessed_urls_stream(credential_set_id=credential_set_id, credential_set_name=credential_set_name, accessed_url=accessed_url, girs=girs, victim=victim, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)

Credential set accessed url stream

Returns list of Credential sets accessed urls matching filter criteria. The response contains “cursor_next” field, which should be provided to the next subsequent call to fetch potential next page of the results. Results are sorted by ascending order of the last_updated_ts field.
Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_set_accessed_url_response_stream import GetCredSetAccessedUrlResponseStream
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
    api_instance = verity471.CredentialsApi(api_client)
    credential_set_id = 'credential_set_id_example' # str | Search by credential set id. (optional)
    credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
    accessed_url = 'accessed_url_example' # str |  (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list (optional)
    victim = 'victim_example' # str |  (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    last_updated_from = 'last_updated_from_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    last_updated_until = 'last_updated_until_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Credential set accessed url stream
        api_response = api_instance.get_credential_sets_accessed_urls_stream(credential_set_id=credential_set_id, credential_set_name=credential_set_name, accessed_url=accessed_url, girs=girs, victim=victim, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)
        print("The response of CredentialsApi->get_credential_sets_accessed_urls_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential_sets_accessed_urls_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_set_id** | **str**| Search by credential set id. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **accessed_url** | **str**|  | [optional] 
 **girs** | **str**| Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list | [optional] 
 **victim** | **str**|  | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **last_updated_from** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **last_updated_until** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**GetCredSetAccessedUrlResponseStream**](GetCredSetAccessedUrlResponseStream.md)

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

# **get_credential_sets_id**
> GetCredSetResponse get_credential_sets_id(id)

Get credential set by ID

Returns a single Credential set matching requested ID.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_set_response import GetCredSetResponse
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
    api_instance = verity471.CredentialsApi(api_client)
    id = 'cred-set--8372c01c-3822-573a-a443-e580fca26b5b' # str | ID of the credential set

    try:
        # Get credential set by ID
        api_response = api_instance.get_credential_sets_id(id)
        print("The response of CredentialsApi->get_credential_sets_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the credential set | 

### Return type

[**GetCredSetResponse**](GetCredSetResponse.md)

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

# **get_credential_sets_stream**
> GetCredSetResponseStream get_credential_sets_stream(credential_set_name=credential_set_name, girs=girs, victim=victim, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)

Credential set stream

Returns list of Credential sets matching filter criteria. The response contains “cursor_next” field, which should be provided to the next subsequent call to fetch potential next page of the results. Results are sorted by ascending order of the last_updated_ts field.
Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_set_response_stream import GetCredSetResponseStream
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
    api_instance = verity471.CredentialsApi(api_client)
    credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list (optional)
    victim = 'victim_example' # str |  (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    last_updated_from = 'last_updated_from_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    last_updated_until = 'last_updated_until_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Credential set stream
        api_response = api_instance.get_credential_sets_stream(credential_set_name=credential_set_name, girs=girs, victim=victim, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)
        print("The response of CredentialsApi->get_credential_sets_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential_sets_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **girs** | **str**| Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list | [optional] 
 **victim** | **str**|  | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **last_updated_from** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **last_updated_until** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**GetCredSetResponseStream**](GetCredSetResponseStream.md)

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

# **get_credentials_id**
> GetCredResponse get_credentials_id(id)

Get credential by ID

Returns a single Credential matching requested ID.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_response import GetCredResponse
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
    api_instance = verity471.CredentialsApi(api_client)
    id = 'cred--5fe9b010-e063-5aca-a9f0-eacb1998d60a' # str | ID of the credential

    try:
        # Get credential by ID
        api_response = api_instance.get_credentials_id(id)
        print("The response of CredentialsApi->get_credentials_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credentials_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the credential | 

### Return type

[**GetCredResponse**](GetCredResponse.md)

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

# **get_credentials_occurrences_id**
> GetCredOccurrenceResponse get_credentials_occurrences_id(id)

Get credential occurrence by ID

Returns a single Credential occurrence matching requested ID.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_occurrence_response import GetCredOccurrenceResponse
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
    api_instance = verity471.CredentialsApi(api_client)
    id = 'cred-occurrence--8fc815ac-7516-588e-b1ba-a468a739cc03' # str | ID of the credential occurrence

    try:
        # Get credential occurrence by ID
        api_response = api_instance.get_credentials_occurrences_id(id)
        print("The response of CredentialsApi->get_credentials_occurrences_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credentials_occurrences_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the credential occurrence | 

### Return type

[**GetCredOccurrenceResponse**](GetCredOccurrenceResponse.md)

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

# **get_credentials_occurrences_stream**
> GetCredOccurrenceResponseStream get_credentials_occurrences_stream(credential_id=credential_id, credential_set_name=credential_set_name, credential_set_id=credential_set_id, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, girs=girs, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)

Credential occurrence stream

Returns list of Credential occurrences matching filter criteria. Stream pagination is based on a cursor. The response is the same as for the /credentials/occurrences endpoint but with the additional “cursorNext” field. Results are sorted by ascending order of the lastUpdated field.
Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_occurrence_response_stream import GetCredOccurrenceResponseStream
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
    api_instance = verity471.CredentialsApi(api_client)
    credential_id = 'credential_id_example' # str | Search by credential id. (optional)
    credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
    credential_set_id = 'credential_set_id_example' # str | Search by credential set id. (optional)
    domain = 'domain_example' # str | Search by credential domain(detection domain). (optional)
    affiliation_group = 'affiliation_group_example' # str | Possible values: my_employees, my_customers, third_parties, vip_emails (optional)
    password_strength = 'password_strength_example' # str | Possible values: excellent, strong, medium, weak, poor, not_provided (optional)
    password_length_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_lowercase_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_uppercase_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_numbers_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_punctuation_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_symbols_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_separators_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_other_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_entropy_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_plain = 'password_plain_example' # str | Must be URL encoded (optional)
    credential_login = 'credential_login_example' # str | Search by credential login. (optional)
    detected_malware = 'detected_malware_example' # str | Search by credential detected malware. For example: agent_tesla, Lumma, VIDAR (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    last_updated_from = 'last_updated_from_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    last_updated_until = 'last_updated_until_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Credential occurrence stream
        api_response = api_instance.get_credentials_occurrences_stream(credential_id=credential_id, credential_set_name=credential_set_name, credential_set_id=credential_set_id, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, girs=girs, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)
        print("The response of CredentialsApi->get_credentials_occurrences_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credentials_occurrences_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| Search by credential id. | [optional] 
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_id** | **str**| Search by credential set id. | [optional] 
 **domain** | **str**| Search by credential domain(detection domain). | [optional] 
 **affiliation_group** | **str**| Possible values: my_employees, my_customers, third_parties, vip_emails | [optional] 
 **password_strength** | **str**| Possible values: excellent, strong, medium, weak, poor, not_provided | [optional] 
 **password_length_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_lowercase_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_uppercase_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_numbers_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_punctuation_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_symbols_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_separators_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_other_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_entropy_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_plain** | **str**| Must be URL encoded | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. For example: agent_tesla, Lumma, VIDAR | [optional] 
 **girs** | **str**| Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **last_updated_from** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **last_updated_until** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**GetCredOccurrenceResponseStream**](GetCredOccurrenceResponseStream.md)

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

# **get_credentials_stream**
> GetCredResponseStream get_credentials_stream(credential_set_name=credential_set_name, credential_set_id=credential_set_id, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, girs=girs, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)

Credential stream

Returns list of Credentials matching filter criteria. The response contains “cursor_next” field, which should be provided to the next subsequent call to fetch potential next page of the results. Results are sorted by ascending order of the last_updated_ts field.
Two indications of the end of the stream are possible: the result list is empty or its size is less than the requested items count.

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.get_cred_response_stream import GetCredResponseStream
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
    api_instance = verity471.CredentialsApi(api_client)
    credential_set_name = 'credential_set_name_example' # str | Search by credential set name. (optional)
    credential_set_id = 'credential_set_id_example' # str | Search by credential set id. (optional)
    domain = 'domain_example' # str | Search by credential domain(detection domain). (optional)
    affiliation_group = 'affiliation_group_example' # str | Possible values: my_employees, my_customers, third_parties, vip_emails (optional)
    password_strength = 'password_strength_example' # str | Possible values: excellent, strong, medium, weak, poor, not_provided (optional)
    password_length_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_lowercase_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_uppercase_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_numbers_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_punctuation_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_symbols_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_separators_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_other_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_entropy_gte = 56 # int | Must be greater than or equal to 0 (optional)
    password_plain = 'password_plain_example' # str | Must be URL encoded (optional)
    credential_login = 'credential_login_example' # str | Search by credential login. (optional)
    detected_malware = 'detected_malware_example' # str | Search by credential detected malware. For example: agent_tesla, Lumma, VIDAR (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    last_updated_from = 'last_updated_from_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    last_updated_until = 'last_updated_until_example' # str | UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Credential stream
        api_response = api_instance.get_credentials_stream(credential_set_name=credential_set_name, credential_set_id=credential_set_id, domain=domain, affiliation_group=affiliation_group, password_strength=password_strength, password_length_gte=password_length_gte, password_lowercase_gte=password_lowercase_gte, password_uppercase_gte=password_uppercase_gte, password_numbers_gte=password_numbers_gte, password_punctuation_gte=password_punctuation_gte, password_symbols_gte=password_symbols_gte, password_separators_gte=password_separators_gte, password_other_gte=password_other_gte, password_entropy_gte=password_entropy_gte, password_plain=password_plain, credential_login=credential_login, detected_malware=detected_malware, girs=girs, var_from=var_from, until=until, last_updated_from=last_updated_from, last_updated_until=last_updated_until, size=size, cursor=cursor)
        print("The response of CredentialsApi->get_credentials_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credentials_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_set_name** | **str**| Search by credential set name. | [optional] 
 **credential_set_id** | **str**| Search by credential set id. | [optional] 
 **domain** | **str**| Search by credential domain(detection domain). | [optional] 
 **affiliation_group** | **str**| Possible values: my_employees, my_customers, third_parties, vip_emails | [optional] 
 **password_strength** | **str**| Possible values: excellent, strong, medium, weak, poor, not_provided | [optional] 
 **password_length_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_lowercase_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_uppercase_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_numbers_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_punctuation_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_symbols_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_separators_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_other_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_entropy_gte** | **int**| Must be greater than or equal to 0 | [optional] 
 **password_plain** | **str**| Must be URL encoded | [optional] 
 **credential_login** | **str**| Search by credential login. | [optional] 
 **detected_malware** | **str**| Search by credential detected malware. For example: agent_tesla, Lumma, VIDAR | [optional] 
 **girs** | **str**| Filter results by custom GIRs (General Intelligence Requirements), my_girs or company_pirs. Using multiple values will return results based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **last_updated_from** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **last_updated_until** | **str**| UNIX timestamp(in milliseconds) or period e.g. 24hours or 7days | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**GetCredResponseStream**](GetCredResponseStream.md)

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

