# verity471.SourcesApi

All URIs are relative to *https://api.intel471.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_leak_sites_file_listings_id**](SourcesApi.md#get_data_leak_sites_file_listings_id) | **GET** /integrations/sources/v1/data-leak-sites/file-listings/{id} | Get a data leak site file listing content
[**get_data_leak_sites_posts_stream**](SourcesApi.md#get_data_leak_sites_posts_stream) | **GET** /integrations/sources/v1/data-leak-sites/posts/stream | Get data leak sites posts (stream)
[**get_forums_posts_post_id**](SourcesApi.md#get_forums_posts_post_id) | **GET** /integrations/sources/v1/forums/posts/{post_id} | Get a forum post by id
[**get_forums_posts_stream**](SourcesApi.md#get_forums_posts_stream) | **GET** /integrations/sources/v1/forums/posts/stream | Get forums posts (stream)
[**get_forums_private_messages_private_message_id**](SourcesApi.md#get_forums_private_messages_private_message_id) | **GET** /integrations/sources/v1/forums/private-messages/{private_message_id} | Get a private message by id
[**get_forums_private_messages_stream**](SourcesApi.md#get_forums_private_messages_stream) | **GET** /integrations/sources/v1/forums/private-messages/stream | Get forums private messages (stream)
[**get_images_image_type_hash_name**](SourcesApi.md#get_images_image_type_hash_name) | **GET** /integrations/sources/v1/images/{image_type}/{hash}/{name} | Download image by type hash and name
[**get_messaging_services_messages_message_id**](SourcesApi.md#get_messaging_services_messages_message_id) | **GET** /integrations/sources/v1/messaging-services/messages/{message_id} | Get a chat message by id
[**get_messaging_services_messages_stream**](SourcesApi.md#get_messaging_services_messages_stream) | **GET** /integrations/sources/v1/messaging-services/messages/stream | Get chat messages (stream)


# **get_data_leak_sites_file_listings_id**
> bytearray get_data_leak_sites_file_listings_id(id)

Get a data leak site file listing content

Returns data leak sites file listing content

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
    api_instance = verity471.SourcesApi(api_client)
    id = 'file--082e91d6-2258-5f21-81d1-809bb96eb720' # str | 

    try:
        # Get a data leak site file listing content
        api_response = api_instance.get_data_leak_sites_file_listings_id(id)
        print("The response of SourcesApi->get_data_leak_sites_file_listings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_data_leak_sites_file_listings_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Content-Disposition -  <br>  * Content-Type -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_leak_sites_posts_stream**
> DataLeakSitePostsStreamingPage get_data_leak_sites_posts_stream(website_id=website_id, thread_id=thread_id, text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)

Get data leak sites posts (stream)

Returns data leak sites posts based on applied filters

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.data_leak_site_posts_streaming_page import DataLeakSitePostsStreamingPage
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
    api_instance = verity471.SourcesApi(api_client)
    website_id = 'website_id_example' # str | Search data leak posts in a given data leak blog (optional)
    thread_id = 'thread--b0bf6f45-a087-5006-b7b6-f19916c3a88b' # str | Search data leak posts by thread id (optional)
    text_filter = 'text_filter_example' # str | Apply text filter to search posts based on a keyword (optional)
    var_from = 56 # int | UNIX timestamp in milliseconds (optional)
    until = 56 # int | UNIX timestamp in milliseconds (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get data leak sites posts (stream)
        api_response = api_instance.get_data_leak_sites_posts_stream(website_id=website_id, thread_id=thread_id, text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of SourcesApi->get_data_leak_sites_posts_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_data_leak_sites_posts_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Search data leak posts in a given data leak blog | [optional] 
 **thread_id** | **str**| Search data leak posts by thread id | [optional] 
 **text_filter** | **str**| Apply text filter to search posts based on a keyword | [optional] 
 **var_from** | **int**| UNIX timestamp in milliseconds | [optional] 
 **until** | **int**| UNIX timestamp in milliseconds | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**DataLeakSitePostsStreamingPage**](DataLeakSitePostsStreamingPage.md)

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

# **get_forums_posts_post_id**
> PostDetails1 get_forums_posts_post_id(post_id)

Get a forum post by id

Return a single forum post by id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.post_details1 import PostDetails1
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
    api_instance = verity471.SourcesApi(api_client)
    post_id = 'post--03d22f83-14f1-5d28-a94e-5807161c92f6' # str | 

    try:
        # Get a forum post by id
        api_response = api_instance.get_forums_posts_post_id(post_id)
        print("The response of SourcesApi->get_forums_posts_post_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_forums_posts_post_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**|  | 

### Return type

[**PostDetails1**](PostDetails1.md)

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

# **get_forums_posts_stream**
> ForumsPostsStreamingPage get_forums_posts_stream(thread_id=thread_id, author=author, author_id=author_id, forum_title=forum_title, text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)

Get forums posts (stream)

Return posts in a thread

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.forums_posts_streaming_page import ForumsPostsStreamingPage
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
    api_instance = verity471.SourcesApi(api_client)
    thread_id = 'thread--d5e745de-a27a-5329-ab9c-1cd4632b2ed6' # str | Search forum posts in a given forum. (optional)
    author = 'author_example' # str | Search for posts authored by given actor user name. (optional)
    author_id = 'author_id_example' # str | Search for posts authored by given actor id. (optional)
    forum_title = 'forum_title_example' # str | Search for posts in a given forum. (optional)
    text_filter = 'text_filter_example' # str | Apply text filter to search posts based on a keyword. (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get forums posts (stream)
        api_response = api_instance.get_forums_posts_stream(thread_id=thread_id, author=author, author_id=author_id, forum_title=forum_title, text_filter=text_filter, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of SourcesApi->get_forums_posts_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_forums_posts_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Search forum posts in a given forum. | [optional] 
 **author** | **str**| Search for posts authored by given actor user name. | [optional] 
 **author_id** | **str**| Search for posts authored by given actor id. | [optional] 
 **forum_title** | **str**| Search for posts in a given forum. | [optional] 
 **text_filter** | **str**| Apply text filter to search posts based on a keyword. | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ForumsPostsStreamingPage**](ForumsPostsStreamingPage.md)

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

# **get_forums_private_messages_private_message_id**
> PrivateMessageDetails1 get_forums_private_messages_private_message_id(private_message_id)

Get a private message by id

Return a single private message by id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.private_message_details1 import PrivateMessageDetails1
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
    api_instance = verity471.SourcesApi(api_client)
    private_message_id = 'private-message--ff34a99a-08da-5313-a1ea-1ca9639a701d' # str | 

    try:
        # Get a private message by id
        api_response = api_instance.get_forums_private_messages_private_message_id(private_message_id)
        print("The response of SourcesApi->get_forums_private_messages_private_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_forums_private_messages_private_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_message_id** | **str**|  | 

### Return type

[**PrivateMessageDetails1**](PrivateMessageDetails1.md)

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

# **get_forums_private_messages_stream**
> ForumsPrivateMessagesStreamingPage get_forums_private_messages_stream(text_filter=text_filter, author=author, author_id=author_id, forum_title=forum_title, subject=subject, recipient=recipient, recipient_id=recipient_id, forum_id=forum_id, var_from=var_from, until=until, size=size, cursor=cursor)

Get forums private messages (stream)

Returns a private messages conversations based on filters

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.forums_private_messages_streaming_page import ForumsPrivateMessagesStreamingPage
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
    api_instance = verity471.SourcesApi(api_client)
    text_filter = 'text_filter_example' # str | Apply text filter to search for private messages based on a keyword. (optional)
    author = 'author_example' # str | Search for messages authored by given actor user name. (optional)
    author_id = 'author_id_example' # str | Search for messages authored by given actor id. (optional)
    forum_title = 'forum_title_example' # str | Search for messages in a given forum (optional)
    subject = 'subject_example' # str | Search text in subjects of Private Messages. (optional)
    recipient = 'recipient_example' # str | Search messages received by given actor user name. (optional)
    recipient_id = 'recipient_id_example' # str | Search messages received by given actor id. (optional)
    forum_id = 'forum--fafde818-43d5-5dbf-b5a9-83253bf13432' # str | Search for messages in a given forum by `forum_id`. `forum_id` will take precedence if used together with the `forum_title` filter (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get forums private messages (stream)
        api_response = api_instance.get_forums_private_messages_stream(text_filter=text_filter, author=author, author_id=author_id, forum_title=forum_title, subject=subject, recipient=recipient, recipient_id=recipient_id, forum_id=forum_id, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of SourcesApi->get_forums_private_messages_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_forums_private_messages_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search for private messages based on a keyword. | [optional] 
 **author** | **str**| Search for messages authored by given actor user name. | [optional] 
 **author_id** | **str**| Search for messages authored by given actor id. | [optional] 
 **forum_title** | **str**| Search for messages in a given forum | [optional] 
 **subject** | **str**| Search text in subjects of Private Messages. | [optional] 
 **recipient** | **str**| Search messages received by given actor user name. | [optional] 
 **recipient_id** | **str**| Search messages received by given actor id. | [optional] 
 **forum_id** | **str**| Search for messages in a given forum by &#x60;forum_id&#x60;. &#x60;forum_id&#x60; will take precedence if used together with the &#x60;forum_title&#x60; filter | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ForumsPrivateMessagesStreamingPage**](ForumsPrivateMessagesStreamingPage.md)

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

# **get_images_image_type_hash_name**
> bytearray get_images_image_type_hash_name(image_type, hash, name)

Download image by type hash and name

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.image_type import ImageType
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
    api_instance = verity471.SourcesApi(api_client)
    image_type = verity471.ImageType() # ImageType | 
    hash = 'd383c5db40027a3d84153c808e6c1c78b3c6c68ff436d5d8c99fb677c32eb6ee' # str | 
    name = 'jhy2Gqc.gif' # str | 

    try:
        # Download image by type hash and name
        api_response = api_instance.get_images_image_type_hash_name(image_type, hash, name)
        print("The response of SourcesApi->get_images_image_type_hash_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_images_image_type_hash_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_type** | [**ImageType**](.md)|  | 
 **hash** | **str**|  | 
 **name** | **str**|  | 

### Return type

**bytearray**

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

# **get_messaging_services_messages_message_id**
> ChatRoomMessageStream get_messaging_services_messages_message_id(message_id)

Get a chat message by id

Return a single chat message by id

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.chat_room_message_stream import ChatRoomMessageStream
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
    api_instance = verity471.SourcesApi(api_client)
    message_id = 'message--99ebfde4-0d27-5daa-bca5-6d08aa827233' # str | 

    try:
        # Get a chat message by id
        api_response = api_instance.get_messaging_services_messages_message_id(message_id)
        print("The response of SourcesApi->get_messaging_services_messages_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_messaging_services_messages_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

[**ChatRoomMessageStream**](ChatRoomMessageStream.md)

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

# **get_messaging_services_messages_stream**
> ChatMessagesStreamingPage get_messaging_services_messages_stream(text_filter=text_filter, author=author, author_id=author_id, server_type=server_type, server_id=server_id, room_id=room_id, var_from=var_from, until=until, size=size, cursor=cursor)

Get chat messages (stream)

Return messages in a chat room

### Example

* Basic Authentication (basicAuth):

```python
import verity471
from verity471.models.chat_messages_streaming_page import ChatMessagesStreamingPage
from verity471.models.chat_server_type_stream import ChatServerTypeStream
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
    api_instance = verity471.SourcesApi(api_client)
    text_filter = 'hacker' # str | Apply text filter to search messages based on a keyword (optional)
    author = 'author_example' # str | Search for messages authored by given actor user name handle. (optional)
    author_id = 'actor--d9a4cda0-8d30-5e50-b730-2ee1145d4edd' # str | Search for messages authored by given actor id handle. (optional)
    server_type = verity471.ChatServerTypeStream() # ChatServerTypeStream | Filter results based on server type (optional)
    server_id = 'server_id_example' # str | Search for chat messages by chat server id. (optional)
    room_id = 'room--92ac69ca-9d08-5cb5-a8e4-4d26c5e50311roo' # str | Search for chat messages by chat room id. (optional)
    var_from = 56 # int | UNIX timestamp(in milliseconds) (optional)
    until = 56 # int | UNIX timestamp(in milliseconds) (optional)
    size = 1000 # int | Range is: [1, 1000] (optional) (default to 1000)
    cursor = 'cursor_example' # str | Continue scrolling from cursor (optional)

    try:
        # Get chat messages (stream)
        api_response = api_instance.get_messaging_services_messages_stream(text_filter=text_filter, author=author, author_id=author_id, server_type=server_type, server_id=server_id, room_id=room_id, var_from=var_from, until=until, size=size, cursor=cursor)
        print("The response of SourcesApi->get_messaging_services_messages_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_messaging_services_messages_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_filter** | **str**| Apply text filter to search messages based on a keyword | [optional] 
 **author** | **str**| Search for messages authored by given actor user name handle. | [optional] 
 **author_id** | **str**| Search for messages authored by given actor id handle. | [optional] 
 **server_type** | [**ChatServerTypeStream**](.md)| Filter results based on server type | [optional] 
 **server_id** | **str**| Search for chat messages by chat server id. | [optional] 
 **room_id** | **str**| Search for chat messages by chat room id. | [optional] 
 **var_from** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **until** | **int**| UNIX timestamp(in milliseconds) | [optional] 
 **size** | **int**| Range is: [1, 1000] | [optional] [default to 1000]
 **cursor** | **str**| Continue scrolling from cursor | [optional] 

### Return type

[**ChatMessagesStreamingPage**](ChatMessagesStreamingPage.md)

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

