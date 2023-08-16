<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.rabbit_hole_api.RabbitHoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file**](#upload_file) | **post** /rabbithole/ | Upload File
[**upload_memory**](#upload_memory) | **post** /rabbithole/memory/ | Upload Memory
[**upload_url**](#upload_url) | **post** /rabbithole/web/ | Upload Url

# **upload_file**
<a id="upload_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_file()

Upload File

Upload a file containing text (.txt, .md, .pdf, etc.). File content will be extracted and segmented into chunks. Chunks will be then vectorized and stored into documents memory.

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import rabbit_hole_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from cheshire_cat_api.model.body_upload_file import BodyUploadFile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rabbit_hole_api.RabbitHoleApi(api_client)

    # example passing only optional values
    body = dict(
        file=open('/path/to/file', 'rb'),
        chunk_size=400,
        chunk_overlap=100,
    )
    try:
        # Upload File
        api_response = api_instance.upload_file(
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling RabbitHoleApi->upload_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyUploadFile**](../../models/BodyUploadFile.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_file.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upload_file.ApiResponseFor422) | Validation Error

#### upload_file.ApiResponseFor200
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

#### upload_file.ApiResponseFor422
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

# **upload_memory**
<a id="upload_memory"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_memory()

Upload Memory

Upload a memory json file to the cat memory

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import rabbit_hole_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from cheshire_cat_api.model.body_upload_memory import BodyUploadMemory
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rabbit_hole_api.RabbitHoleApi(api_client)

    # example passing only optional values
    body = dict(
        file=open('/path/to/file', 'rb'),
    )
    try:
        # Upload Memory
        api_response = api_instance.upload_memory(
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling RabbitHoleApi->upload_memory: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyUploadMemory**](../../models/BodyUploadMemory.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_memory.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upload_memory.ApiResponseFor422) | Validation Error

#### upload_memory.ApiResponseFor200
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

#### upload_memory.ApiResponseFor422
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

# **upload_url**
<a id="upload_url"></a>
> bool, date, datetime, dict, float, int, list, str, none_type upload_url(body_upload_url)

Upload Url

Upload a url. Website content will be extracted and segmented into chunks. Chunks will be then vectorized and stored into documents memory.

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import rabbit_hole_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from cheshire_cat_api.model.body_upload_url import BodyUploadUrl
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rabbit_hole_api.RabbitHoleApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyUploadUrl(
        url="url_example",
        chunk_size=400,
        chunk_overlap=100,
    )
    try:
        # Upload Url
        api_response = api_instance.upload_url(
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling RabbitHoleApi->upload_url: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyUploadUrl**](../../models/BodyUploadUrl.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_url.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upload_url.ApiResponseFor422) | Validation Error

#### upload_url.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### upload_url.ApiResponseFor422
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

