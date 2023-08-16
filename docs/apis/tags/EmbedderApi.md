<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.embedder_api.EmbedderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_embedder_settings**](#get_embedder_settings) | **get** /embedder/settings/{languageEmbedderName} | Get Embedder Settings
[**get_embedders_settings**](#get_embedders_settings) | **get** /embedder/settings/ | Get Embedders Settings
[**upsert_embedder_setting**](#upsert_embedder_setting) | **put** /embedder/settings/{languageEmbedderName} | Upsert Embedder Setting

# **get_embedder_settings**
<a id="get_embedder_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_embedder_settings(language_embedder_name)

Get Embedder Settings

Get settings and schema of the specified Embedder

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import embedder_api
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
    api_instance = embedder_api.EmbedderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'languageEmbedderName': "languageEmbedderName_example",
    }
    try:
        # Get Embedder Settings
        api_response = api_instance.get_embedder_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling EmbedderApi->get_embedder_settings: %s\n" % e)
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
languageEmbedderName | LanguageEmbedderNameSchema | | 

# LanguageEmbedderNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_embedder_settings.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_embedder_settings.ApiResponseFor422) | Validation Error

#### get_embedder_settings.ApiResponseFor200
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

#### get_embedder_settings.ApiResponseFor422
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

# **get_embedders_settings**
<a id="get_embedders_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_embedders_settings()

Get Embedders Settings

Get the list of the Embedders

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import embedder_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embedder_api.EmbedderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Embedders Settings
        api_response = api_instance.get_embedders_settings()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling EmbedderApi->get_embedders_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_embedders_settings.ApiResponseFor200) | Successful Response

#### get_embedders_settings.ApiResponseFor200
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

# **upsert_embedder_setting**
<a id="upsert_embedder_setting"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upsert_embedder_setting(language_embedder_namebody)

Upsert Embedder Setting

Upsert the Embedder setting

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import embedder_api
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
    api_instance = embedder_api.EmbedderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'languageEmbedderName': "languageEmbedderName_example",
    }
    body = dict()
    try:
        # Upsert Embedder Setting
        api_response = api_instance.upsert_embedder_setting(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling EmbedderApi->upsert_embedder_setting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
languageEmbedderName | LanguageEmbedderNameSchema | | 

# LanguageEmbedderNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_embedder_setting.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upsert_embedder_setting.ApiResponseFor422) | Validation Error

#### upsert_embedder_setting.ApiResponseFor200
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

#### upsert_embedder_setting.ApiResponseFor422
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

