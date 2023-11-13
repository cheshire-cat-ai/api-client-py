# cheshire_cat_api.MemoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collections**](MemoryApi.md#get_collections) | **GET** /memory/collections/ | Get Collections
[**get_conversation_history**](MemoryApi.md#get_conversation_history) | **GET** /memory/conversation_history/ | Get Conversation History
[**recall_memories_from_text**](MemoryApi.md#recall_memories_from_text) | **GET** /memory/recall/ | Recall Memories From Text
[**wipe_collections**](MemoryApi.md#wipe_collections) | **DELETE** /memory/collections/ | Wipe Collections
[**wipe_conversation_history**](MemoryApi.md#wipe_conversation_history) | **DELETE** /memory/conversation_history/ | Wipe Conversation History
[**wipe_memory_point**](MemoryApi.md#wipe_memory_point) | **DELETE** /memory/collections/{collection_id}/points/{memory_id}/ | Wipe Memory Point
[**wipe_memory_points_by_metadata**](MemoryApi.md#wipe_memory_points_by_metadata) | **DELETE** /memory/collections/{collection_id}/points | Wipe Memory Points By Metadata
[**wipe_single_collection**](MemoryApi.md#wipe_single_collection) | **DELETE** /memory/collections/{collection_id}/ | Wipe Single Collection


# **get_collections**
> object get_collections()

Get Collections

Get list of available collections

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)

    try:
        # Get Collections
        api_response = api_instance.get_collections()
        print("The response of MemoryApi->get_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_collections: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_history**
> object get_conversation_history()

Get Conversation History

Get the specified user's conversation history from working memory

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)

    try:
        # Get Conversation History
        api_response = api_instance.get_conversation_history()
        print("The response of MemoryApi->get_conversation_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_conversation_history: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recall_memories_from_text**
> object recall_memories_from_text(text, k=k)

Recall Memories From Text

Search k memories similar to given text.

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)
    text = 'text_example' # str | Find memories similar to this text.
    k = 100 # int | How many memories to return. (optional) (default to 100)

    try:
        # Recall Memories From Text
        api_response = api_instance.recall_memories_from_text(text, k=k)
        print("The response of MemoryApi->recall_memories_from_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->recall_memories_from_text: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Find memories similar to this text. | 
 **k** | **int**| How many memories to return. | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_collections**
> object wipe_collections()

Wipe Collections

Delete and create all collections

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)

    try:
        # Wipe Collections
        api_response = api_instance.wipe_collections()
        print("The response of MemoryApi->wipe_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->wipe_collections: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_conversation_history**
> object wipe_conversation_history()

Wipe Conversation History

Delete the specified user's conversation history from working memory

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)

    try:
        # Wipe Conversation History
        api_response = api_instance.wipe_conversation_history()
        print("The response of MemoryApi->wipe_conversation_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->wipe_conversation_history: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_memory_point**
> object wipe_memory_point(collection_id, memory_id)

Wipe Memory Point

Delete a specific point in memory

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)
    collection_id = 'collection_id_example' # str | 
    memory_id = 'memory_id_example' # str | 

    try:
        # Wipe Memory Point
        api_response = api_instance.wipe_memory_point(collection_id, memory_id)
        print("The response of MemoryApi->wipe_memory_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->wipe_memory_point: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **memory_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_memory_points_by_metadata**
> object wipe_memory_points_by_metadata(collection_id, body=body)

Wipe Memory Points By Metadata

Delete points in memory by filter

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)
    collection_id = 'collection_id_example' # str | 
    body = None # object |  (optional)

    try:
        # Wipe Memory Points By Metadata
        api_response = api_instance.wipe_memory_points_by_metadata(collection_id, body=body)
        print("The response of MemoryApi->wipe_memory_points_by_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->wipe_memory_points_by_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_single_collection**
> object wipe_single_collection(collection_id)

Wipe Single Collection

Delete and recreate a collection

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cheshire_cat_api.MemoryApi(api_client)
    collection_id = 'collection_id_example' # str | 

    try:
        # Wipe Single Collection
        api_response = api_instance.wipe_single_collection(collection_id)
        print("The response of MemoryApi->wipe_single_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->wipe_single_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

