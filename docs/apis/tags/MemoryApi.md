<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.memory_api.MemoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collections**](#get_collections) | **get** /memory/collections/ | Get Collections
[**recall_memories_from_text**](#recall_memories_from_text) | **get** /memory/recall/ | Recall Memories From Text
[**wipe_collections**](#wipe_collections) | **delete** /memory/collections/ | Wipe Collections
[**wipe_conversation_history**](#wipe_conversation_history) | **delete** /memory/conversation_history/ | Wipe Conversation History
[**wipe_memory_point**](#wipe_memory_point) | **delete** /memory/collections/{collection_id}/points/{memory_id}/ | Wipe Memory Point
[**wipe_single_collection**](#wipe_single_collection) | **delete** /memory/collections/{collection_id}/ | Wipe Single Collection

# **get_collections**
<a id="get_collections"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_collections()

Get Collections

Get list of available collections

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Collections
        api_response = api_instance.get_collections()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->get_collections: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_collections.ApiResponseFor200) | Successful Response

#### get_collections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **recall_memories_from_text**
<a id="recall_memories_from_text"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} recall_memories_from_text(text)

Recall Memories From Text

Search k memories similar to given text.

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'text': "text_example",
    }
    try:
        # Recall Memories From Text
        api_response = api_instance.recall_memories_from_text(
            query_params=query_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->recall_memories_from_text: %s\n" % e)

    # example passing only optional values
    query_params = {
        'text': "text_example",
        'k': 100,
        'user_id': "user",
    }
    try:
        # Recall Memories From Text
        api_response = api_instance.recall_memories_from_text(
            query_params=query_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->recall_memories_from_text: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
text | TextSchema | | 
k | KSchema | | optional
user_id | UserIdSchema | | optional


# TextSchema

Find memories similar to this text.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Find memories similar to this text. | 

# KSchema

How many memories to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | How many memories to return. | if omitted the server will use the default value of 100

# UserIdSchema

User id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | User id. | if omitted the server will use the default value of "user"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#recall_memories_from_text.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#recall_memories_from_text.ApiResponseFor422) | Validation Error

#### recall_memories_from_text.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### recall_memories_from_text.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wipe_collections**
<a id="wipe_collections"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} wipe_collections()

Wipe Collections

Delete and create all collections

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wipe Collections
        api_response = api_instance.wipe_collections()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->wipe_collections: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wipe_collections.ApiResponseFor200) | Successful Response

#### wipe_collections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wipe_conversation_history**
<a id="wipe_conversation_history"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} wipe_conversation_history()

Wipe Conversation History

Delete conversation history from working memory

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wipe Conversation History
        api_response = api_instance.wipe_conversation_history()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->wipe_conversation_history: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wipe_conversation_history.ApiResponseFor200) | Successful Response

#### wipe_conversation_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wipe_memory_point**
<a id="wipe_memory_point"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} wipe_memory_point(collection_idmemory_id)

Wipe Memory Point

Delete a specific point in memory

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'collection_id': "collection_id_example",
        'memory_id': "memory_id_example",
    }
    try:
        # Wipe Memory Point
        api_response = api_instance.wipe_memory_point(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->wipe_memory_point: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
collection_id | CollectionIdSchema | | 
memory_id | MemoryIdSchema | | 

# CollectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MemoryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wipe_memory_point.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#wipe_memory_point.ApiResponseFor422) | Validation Error

#### wipe_memory_point.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### wipe_memory_point.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wipe_single_collection**
<a id="wipe_single_collection"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} wipe_single_collection(collection_id)

Wipe Single Collection

Delete and recreate a collection

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import memory_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = memory_api.MemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'collection_id': "collection_id_example",
    }
    try:
        # Wipe Single Collection
        api_response = api_instance.wipe_single_collection(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling MemoryApi->wipe_single_collection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
collection_id | CollectionIdSchema | | 

# CollectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wipe_single_collection.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#wipe_single_collection.ApiResponseFor422) | Validation Error

#### wipe_single_collection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### wipe_single_collection.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

