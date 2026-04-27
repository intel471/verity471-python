# verity471.ReportsApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports_breach_alert_id**](ReportsApi.md#get_reports_breach_alert_id) | **GET** /integrations/intel-report/v1/reports/breach-alert/{id} | Get a breach alert report details
[**get_reports_breach_alert_stream**](ReportsApi.md#get_reports_breach_alert_stream) | **GET** /integrations/intel-report/v1/reports/breach-alert/stream | Get all breach alert reports (stream)
[**get_reports_fintel_id**](ReportsApi.md#get_reports_fintel_id) | **GET** /integrations/intel-report/v1/reports/fintel/{id} | Get a fintel report details
[**get_reports_fintel_report_id_attachments_attachment_id**](ReportsApi.md#get_reports_fintel_report_id_attachments_attachment_id) | **GET** /integrations/intel-report/v1/reports/fintel/{report_id}/attachments/{attachment_id} | Get attachment for fintel report
[**get_reports_fintel_stream**](ReportsApi.md#get_reports_fintel_stream) | **GET** /integrations/intel-report/v1/reports/fintel/stream | Get all fintel reports (stream)
[**get_reports_geopol_id**](ReportsApi.md#get_reports_geopol_id) | **GET** /integrations/intel-report/v1/reports/geopol/{id} | Get a geopol report details
[**get_reports_geopol_report_id_attachments_attachment_id**](ReportsApi.md#get_reports_geopol_report_id_attachments_attachment_id) | **GET** /integrations/intel-report/v1/reports/geopol/{report_id}/attachments/{attachment_id} | Get attachment for geopol report
[**get_reports_geopol_stream**](ReportsApi.md#get_reports_geopol_stream) | **GET** /integrations/intel-report/v1/reports/geopol/stream | Get all geopol reports (stream)
[**get_reports_id_download_as_pdf**](ReportsApi.md#get_reports_id_download_as_pdf) | **GET** /integrations/intel-report/v1/reports/{id}/download-as-pdf | Get a report as PDF
[**get_reports_info_id**](ReportsApi.md#get_reports_info_id) | **GET** /integrations/intel-report/v1/reports/info/{id} | Get an info report details
[**get_reports_info_report_id_attachments_attachment_id**](ReportsApi.md#get_reports_info_report_id_attachments_attachment_id) | **GET** /integrations/intel-report/v1/reports/info/{report_id}/attachments/{attachment_id} | Get attachment for info report
[**get_reports_info_stream**](ReportsApi.md#get_reports_info_stream) | **GET** /integrations/intel-report/v1/reports/info/stream | Get all info reports (stream)
[**get_reports_malware_id**](ReportsApi.md#get_reports_malware_id) | **GET** /integrations/intel-report/v1/reports/malware/{id} | Get a malware report details
[**get_reports_malware_report_id_attachments_attachment_id**](ReportsApi.md#get_reports_malware_report_id_attachments_attachment_id) | **GET** /integrations/intel-report/v1/reports/malware/{report_id}/attachments/{attachment_id} | Get attachment for malware report
[**get_reports_malware_stream**](ReportsApi.md#get_reports_malware_stream) | **GET** /integrations/intel-report/v1/reports/malware/stream | Get all malware reports (stream)
[**get_reports_spot_id**](ReportsApi.md#get_reports_spot_id) | **GET** /integrations/intel-report/v1/reports/spot/{id} | Get a spot report details
[**get_reports_spot_stream**](ReportsApi.md#get_reports_spot_stream) | **GET** /integrations/intel-report/v1/reports/spot/stream | Get all spot reports (stream)
[**get_reports_stream**](ReportsApi.md#get_reports_stream) | **GET** /integrations/intel-report/v1/reports/stream | Get all reports (stream)
[**get_reports_vulnerabilities_id_download_as_pdf**](ReportsApi.md#get_reports_vulnerabilities_id_download_as_pdf) | **GET** /integrations/intel-report/v1/reports/vulnerabilities/{id}/download-as-pdf | Get a vulnerability report as PDF
[**get_reports_vulnerability_id**](ReportsApi.md#get_reports_vulnerability_id) | **GET** /integrations/intel-report/v1/reports/vulnerability/{id} | Get a vulnerability report details
[**get_reports_vulnerability_stream**](ReportsApi.md#get_reports_vulnerability_stream) | **GET** /integrations/intel-report/v1/reports/vulnerability/stream | Get all vulnerabilities reports (stream)


# **get_reports_breach_alert_id**
> BreachAlertByIdResponse get_reports_breach_alert_id(id, include_inline_images=include_inline_images)

Get a breach alert report details

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.breach_alert_by_id_response import BreachAlertByIdResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--6312bcbe-feb6-5b4d-bfec-ad2ddeabcc21' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get a breach alert report details
        api_response = api_instance.get_reports_breach_alert_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_breach_alert_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_breach_alert_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**BreachAlertByIdResponse**](BreachAlertByIdResponse.md)

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

# **get_reports_breach_alert_stream**
> BreachAlertsResponseStream get_reports_breach_alert_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)

Get all breach alert reports (stream)

Returns list of reports

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.breach_alerts_response_stream import BreachAlertsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all breach alert reports (stream)
        api_response = api_instance.get_reports_breach_alert_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_breach_alert_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_breach_alert_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**BreachAlertsResponseStream**](BreachAlertsResponseStream.md)

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

# **get_reports_fintel_id**
> FintelResponse get_reports_fintel_id(id, include_inline_images=include_inline_images)

Get a fintel report details

Returns a fintel report based on id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.fintel_response import FintelResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--2e3c8a71-5811-59e0-a7bc-4a4a31a1b22f' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get a fintel report details
        api_response = api_instance.get_reports_fintel_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_fintel_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_fintel_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**FintelResponse**](FintelResponse.md)

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

# **get_reports_fintel_report_id_attachments_attachment_id**
> bytes get_reports_fintel_report_id_attachments_attachment_id(report_id, attachment_id)

Get attachment for fintel report

Returns attachment in form of byte stream

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
    api_instance = verity471.ReportsApi(api_client)
    report_id = 'report--2e3c8a71-5811-59e0-a7bc-4a4a31a1b22f' # str | 
    attachment_id = '18a8df76cb766e9aed83c9450a30921a920c6509e44cd7e6a6cdac6a58e549e7' # str | 

    try:
        # Get attachment for fintel report
        api_response = api_instance.get_reports_fintel_report_id_attachments_attachment_id(report_id, attachment_id)
        print("The response of ReportsApi->get_reports_fintel_report_id_attachments_attachment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_fintel_report_id_attachments_attachment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Disposition -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_fintel_stream**
> FintelReportsResponseStream get_reports_fintel_stream(text_filter=text_filter, girs=girs, sub_type=sub_type, var_from=var_from, until=until, size=size, cursor=cursor)

Get all fintel reports (stream)

Returns list of reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.fintel_reports_response_stream import FintelReportsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    sub_type = ['sub_type_example'] # List[str] | If using filter `type=fintel`, you can then further filter result by subtypes (supports multiple). Allowed values: actor_profile, intelligence_bulletin, service_profile, underground_perspective, underground_pulse, whitepaper, threat_brief, breach_report, intelligence_summary, malware_campaign, fintel_blog (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all fintel reports (stream)
        api_response = api_instance.get_reports_fintel_stream(text_filter=text_filter, girs=girs, sub_type=sub_type, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_fintel_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_fintel_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **sub_type** | [**List[str]**](str.md)| If using filter &#x60;type&#x3D;fintel&#x60;, you can then further filter result by subtypes (supports multiple). Allowed values: actor_profile, intelligence_bulletin, service_profile, underground_perspective, underground_pulse, whitepaper, threat_brief, breach_report, intelligence_summary, malware_campaign, fintel_blog | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**FintelReportsResponseStream**](FintelReportsResponseStream.md)

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

# **get_reports_geopol_id**
> GeopolReportDetailsResponse get_reports_geopol_id(id, include_inline_images=include_inline_images)

Get a geopol report details

Returns a details of a geopol report

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.geopol_report_details_response import GeopolReportDetailsResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--e42e87d7-b2a4-5f56-aaa2-e64c4f08e422' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get a geopol report details
        api_response = api_instance.get_reports_geopol_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_geopol_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_geopol_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**GeopolReportDetailsResponse**](GeopolReportDetailsResponse.md)

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

# **get_reports_geopol_report_id_attachments_attachment_id**
> bytes get_reports_geopol_report_id_attachments_attachment_id(report_id, attachment_id)

Get attachment for geopol report

Returns attachment in form of byte stream

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
    api_instance = verity471.ReportsApi(api_client)
    report_id = 'report--7c404c08-ff9c-5107-99fd-bc56d21151b1' # str | 
    attachment_id = 'c681d9e851ab6663adea8b1c229c35d322dd1b19e7810f3601c6e022fc5dff99' # str | 

    try:
        # Get attachment for geopol report
        api_response = api_instance.get_reports_geopol_report_id_attachments_attachment_id(report_id, attachment_id)
        print("The response of ReportsApi->get_reports_geopol_report_id_attachments_attachment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_geopol_report_id_attachments_attachment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Disposition -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_geopol_stream**
> GeopolReportsResponseStream get_reports_geopol_stream(sub_type=sub_type, country=country, report_location_country=report_location_country, text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)

Get all geopol reports (stream)

Returns a list of geopol reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.geopol_reports_response_stream import GeopolReportsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    sub_type = ['sub_type_example'] # List[str] | Filter result by GEOPOL subtypes. Allowed values: spot_report, intelligence_bulletin, intelligence_summary, tension_point_profile, threat_brief, significant_activity_report, intelligence_estimate, adversary_profile (optional)
    country = 'country_example' # str | Filter result by country. (optional)
    report_location_country = 'report_location_country_example' # str | Filter result by report location. (optional)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 100 # int | Range is: [1, 100] (optional) (default to 100)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all geopol reports (stream)
        api_response = api_instance.get_reports_geopol_stream(sub_type=sub_type, country=country, report_location_country=report_location_country, text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_geopol_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_geopol_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_type** | [**List[str]**](str.md)| Filter result by GEOPOL subtypes. Allowed values: spot_report, intelligence_bulletin, intelligence_summary, tension_point_profile, threat_brief, significant_activity_report, intelligence_estimate, adversary_profile | [optional] 
 **country** | **str**| Filter result by country. | [optional] 
 **report_location_country** | **str**| Filter result by report location. | [optional] 
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 100] | [optional] [default to 100]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**GeopolReportsResponseStream**](GeopolReportsResponseStream.md)

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

# **get_reports_id_download_as_pdf**
> bytes get_reports_id_download_as_pdf(id)

Get a report as PDF

Download report as pdf

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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--407ec14f-23c5-5d6b-8e3d-0b8d9d7413a2' # str | 

    try:
        # Get a report as PDF
        api_response = api_instance.get_reports_id_download_as_pdf(id)
        print("The response of ReportsApi->get_reports_id_download_as_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_id_download_as_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Type -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_info_id**
> InfoReportResponse get_reports_info_id(id, include_inline_images=include_inline_images)

Get an info report details

Return info report by ID

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.info_report_response import InfoReportResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--f9a6b8f4-f931-5781-856e-f435af22074e' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get an info report details
        api_response = api_instance.get_reports_info_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_info_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_info_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**InfoReportResponse**](InfoReportResponse.md)

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

# **get_reports_info_report_id_attachments_attachment_id**
> bytes get_reports_info_report_id_attachments_attachment_id(report_id, attachment_id)

Get attachment for info report

Returns attachment in form of byte stream

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
    api_instance = verity471.ReportsApi(api_client)
    report_id = 'report--f9a6b8f4-f931-5781-856e-f435af22074e' # str | 
    attachment_id = 'a19d91df22cfd225c2942d519b2e3f05451602b6a0c51a6b6acbb548db00861b' # str | 

    try:
        # Get attachment for info report
        api_response = api_instance.get_reports_info_report_id_attachments_attachment_id(report_id, attachment_id)
        print("The response of ReportsApi->get_reports_info_report_id_attachments_attachment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_info_report_id_attachments_attachment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Disposition -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_info_stream**
> InfoReportsResponseStream get_reports_info_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)

Get all info reports (stream)

Returns list of info reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.info_reports_response_stream import InfoReportsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all info reports (stream)
        api_response = api_instance.get_reports_info_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_info_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_info_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**InfoReportsResponseStream**](InfoReportsResponseStream.md)

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

# **get_reports_malware_id**
> MalwareReportResponse get_reports_malware_id(id, include_inline_images=include_inline_images)

Get a malware report details

Returns malware report based by ID

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.malware_report_response import MalwareReportResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--407ec14f-23c5-5d6b-8e3d-0b8d9d7413a2' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get a malware report details
        api_response = api_instance.get_reports_malware_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_malware_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_malware_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**MalwareReportResponse**](MalwareReportResponse.md)

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

# **get_reports_malware_report_id_attachments_attachment_id**
> bytes get_reports_malware_report_id_attachments_attachment_id(report_id, attachment_id)

Get attachment for malware report

Returns attachment in form of byte stream

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
    api_instance = verity471.ReportsApi(api_client)
    report_id = 'report--407ec14f-23c5-5d6b-8e3d-0b8d9d7413a2' # str | 
    attachment_id = 'd2149d75c7c32facda76ca586d696a6fe968d859a525d84788f18cf5f00ade52' # str | 

    try:
        # Get attachment for malware report
        api_response = api_instance.get_reports_malware_report_id_attachments_attachment_id(report_id, attachment_id)
        print("The response of ReportsApi->get_reports_malware_report_id_attachments_attachment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_malware_report_id_attachments_attachment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Disposition -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_malware_stream**
> MalwareReportsResponseStream get_reports_malware_stream(text_filter=text_filter, girs=girs, malware_family=malware_family, threat_id=threat_id, threat_type=threat_type, var_from=var_from, until=until, size=size, cursor=cursor)

Get all malware reports (stream)

Returns list of malware reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.malware_reports_response_stream import MalwareReportsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    malware_family = 'malware_family_example' # str | Search malware reports by malware family (optional)
    threat_id = 'threat_id_example' # str | Search malware reports by threat ID (optional)
    threat_type = 'threat_type_example' # str | Search malware reports by threat type (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all malware reports (stream)
        api_response = api_instance.get_reports_malware_stream(text_filter=text_filter, girs=girs, malware_family=malware_family, threat_id=threat_id, threat_type=threat_type, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_malware_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_malware_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **malware_family** | **str**| Search malware reports by malware family | [optional] 
 **threat_id** | **str**| Search malware reports by threat ID | [optional] 
 **threat_type** | **str**| Search malware reports by threat type | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**MalwareReportsResponseStream**](MalwareReportsResponseStream.md)

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

# **get_reports_spot_id**
> SpotReportResponse get_reports_spot_id(id, include_inline_images=include_inline_images)

Get a spot report details

Returns spot report by ID

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.spot_report_response import SpotReportResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'report--32b605e5-362c-5c10-b797-38f25da8cc0d' # str | 
    include_inline_images = True # bool | Inline images (optional)

    try:
        # Get a spot report details
        api_response = api_instance.get_reports_spot_id(id, include_inline_images=include_inline_images)
        print("The response of ReportsApi->get_reports_spot_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_spot_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_inline_images** | **bool**| Inline images | [optional] 

### Return type

[**SpotReportResponse**](SpotReportResponse.md)

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

# **get_reports_spot_stream**
> SpotReportsResponseStream get_reports_spot_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)

Get all spot reports (stream)

Returns list of spot reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.spot_reports_response_stream import SpotReportsResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all spot reports (stream)
        api_response = api_instance.get_reports_spot_stream(text_filter=text_filter, girs=girs, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_spot_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_spot_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**SpotReportsResponseStream**](SpotReportsResponseStream.md)

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

# **get_reports_stream**
> ReportResponseStream get_reports_stream(text_filter=text_filter, girs=girs, type=type, sub_type=sub_type, var_from=var_from, until=until, size=size, cursor=cursor)

Get all reports (stream)

Returns list of reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.report_response_stream import ReportResponseStream
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
    api_instance = verity471.ReportsApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list (optional)
    type = ['type_example'] # List[str] | Filter result by type of report (supports multiple). Allowed values: fintel, info_report, breach_alert, spot_report, vulnerability_report, malware_report, geopol_report, situation_report, news_report (optional)
    sub_type = ['sub_type_example'] # List[str] | If using filter `report_type=fintel` or `report_type=geopol_report`, you can then further filter result by subtypes (supports multiple). Allowed values for fintel: actor_profile, intelligence_bulletin, service_profile, underground_perspective, underground_pulse, whitepaper, threat_brief, breach_report, intelligence_summary, malware_campaign, fintel_blog, for geopol: spot_report, intelligence_bulletin, intelligence_summary, tension_point_profile, threat_brief, significant_activity_report, intelligence_estimate, adversary_profile (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all reports (stream)
        api_response = api_instance.get_reports_stream(text_filter=text_filter, girs=girs, type=type, sub_type=sub_type, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), my_girs or company_pirs. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **type** | [**List[str]**](str.md)| Filter result by type of report (supports multiple). Allowed values: fintel, info_report, breach_alert, spot_report, vulnerability_report, malware_report, geopol_report, situation_report, news_report | [optional] 
 **sub_type** | [**List[str]**](str.md)| If using filter &#x60;report_type&#x3D;fintel&#x60; or &#x60;report_type&#x3D;geopol_report&#x60;, you can then further filter result by subtypes (supports multiple). Allowed values for fintel: actor_profile, intelligence_bulletin, service_profile, underground_perspective, underground_pulse, whitepaper, threat_brief, breach_report, intelligence_summary, malware_campaign, fintel_blog, for geopol: spot_report, intelligence_bulletin, intelligence_summary, tension_point_profile, threat_brief, significant_activity_report, intelligence_estimate, adversary_profile | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ReportResponseStream**](ReportResponseStream.md)

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

# **get_reports_vulnerabilities_id_download_as_pdf**
> bytes get_reports_vulnerabilities_id_download_as_pdf(id)

Get a vulnerability report as PDF

Download vulnerability report as pdf

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
    api_instance = verity471.ReportsApi(api_client)
    id = 'vulnerability--527c3004-241f-599d-9dbd-00ac1d6d52f6' # str | 

    try:
        # Get a vulnerability report as PDF
        api_response = api_instance.get_reports_vulnerabilities_id_download_as_pdf(id)
        print("The response of ReportsApi->get_reports_vulnerabilities_id_download_as_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_vulnerabilities_id_download_as_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytes**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Type -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_vulnerability_id**
> VulnerabilitiesReportDetailsResponse get_reports_vulnerability_id(id)

Get a vulnerability report details

Returns a details of a vulnerabilities report

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.vulnerabilities_report_details_response import VulnerabilitiesReportDetailsResponse
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
    api_instance = verity471.ReportsApi(api_client)
    id = 'vulnerability--cebd8c83-47e4-5d53-bec7-92be770a32d5' # str | 

    try:
        # Get a vulnerability report details
        api_response = api_instance.get_reports_vulnerability_id(id)
        print("The response of ReportsApi->get_reports_vulnerability_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_vulnerability_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VulnerabilitiesReportDetailsResponse**](VulnerabilitiesReportDetailsResponse.md)

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

# **get_reports_vulnerability_stream**
> VulnerabilitiesReportsResponseStream get_reports_vulnerability_stream(status=status, text_filter=text_filter, girs=girs, risk_level=risk_level, patch_status=patch_status, interest_level=interest_level, activity_location=activity_location, exploit_status=exploit_status, cve_type=cve_type, cve_name=cve_name, vendor_name=vendor_name, product_name=product_name, var_from=var_from, until=until, size=size, cursor=cursor)

Get all vulnerabilities reports (stream)

Returns list of vulnerabilities reports (stream)

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.activity_location import ActivityLocation
from verity471.models.exploit_status import ExploitStatus
from verity471.models.interest_level import InterestLevel
from verity471.models.patch_status import PatchStatus
from verity471.models.risk_level import RiskLevel
from verity471.models.vulnerabilities_reports_response_stream import VulnerabilitiesReportsResponseStream
from verity471.models.vulnerability_status import VulnerabilityStatus
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
    api_instance = verity471.ReportsApi(api_client)
    status = verity471.VulnerabilityStatus() # VulnerabilityStatus | Vulnerabilities status type (optional)
    text_filter = 'text_filter_example' # str | Apply text filter to search reports based on a keyword (optional)
    girs = '1.0.1,2.1.0,my_girs,company_pirs' # str | Filter result by custom GIRs (General intel requirements), `my_girs` or `company_pirs`. Using multiple value will return result based on the aggregated GIR list (optional)
    risk_level = [verity471.RiskLevel()] # List[RiskLevel] | Search reports in a given risk level (optional)
    patch_status = [verity471.PatchStatus()] # List[PatchStatus] | Search reports with given patch status. (optional)
    interest_level = [verity471.InterestLevel()] # List[InterestLevel] | Search reports with given interest level. (optional)
    activity_location = [verity471.ActivityLocation()] # List[ActivityLocation] | Search reports with given activity location. (optional)
    exploit_status = [verity471.ExploitStatus()] # List[ExploitStatus] | Search reports with given exploit status. (optional)
    cve_type = 'cve_type_example' # str | Search reports with given cve type. (optional)
    cve_name = 'cve_name_example' # str | Search reports with given cve name. (optional)
    vendor_name = 'vendor_name_example' # str | Search reports with given vendor name. (optional)
    product_name = 'product_name_example' # str | Search reports with given product name. (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get all vulnerabilities reports (stream)
        api_response = api_instance.get_reports_vulnerability_stream(status=status, text_filter=text_filter, girs=girs, risk_level=risk_level, patch_status=patch_status, interest_level=interest_level, activity_location=activity_location, exploit_status=exploit_status, cve_type=cve_type, cve_name=cve_name, vendor_name=vendor_name, product_name=product_name, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of ReportsApi->get_reports_vulnerability_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reports_vulnerability_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**VulnerabilityStatus**](.md)| Vulnerabilities status type | [optional] 
 **text_filter** | **str**| Apply text filter to search reports based on a keyword | [optional] 
 **girs** | **str**| Filter result by custom GIRs (General intel requirements), &#x60;my_girs&#x60; or &#x60;company_pirs&#x60;. Using multiple value will return result based on the aggregated GIR list | [optional] 
 **risk_level** | [**List[RiskLevel]**](RiskLevel.md)| Search reports in a given risk level | [optional] 
 **patch_status** | [**List[PatchStatus]**](PatchStatus.md)| Search reports with given patch status. | [optional] 
 **interest_level** | [**List[InterestLevel]**](InterestLevel.md)| Search reports with given interest level. | [optional] 
 **activity_location** | [**List[ActivityLocation]**](ActivityLocation.md)| Search reports with given activity location. | [optional] 
 **exploit_status** | [**List[ExploitStatus]**](ExploitStatus.md)| Search reports with given exploit status. | [optional] 
 **cve_type** | **str**| Search reports with given cve type. | [optional] 
 **cve_name** | **str**| Search reports with given cve name. | [optional] 
 **vendor_name** | **str**| Search reports with given vendor name. | [optional] 
 **product_name** | **str**| Search reports with given product name. | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**VulnerabilitiesReportsResponseStream**](VulnerabilitiesReportsResponseStream.md)

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

