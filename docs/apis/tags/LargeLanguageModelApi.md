<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.large_language_model_api.LargeLanguageModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_llm_settings**](#get_llm_settings) | **get** /llm/settings/{languageModelName} | Get Llm Settings
[**get_llms_settings**](#get_llms_settings) | **get** /llm/settings/ | Get Llms Settings
[**upsert_llm_setting**](#upsert_llm_setting) | **put** /llm/settings/{languageModelName} | Upsert Llm Setting

# **get_llm_settings**
<a id="get_llm_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_llm_settings(language_model_name)

Get Llm Settings

Get settings and schema of the specified Large Language Model

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import large_language_model_api
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
    api_instance = large_language_model_api.LargeLanguageModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'languageModelName': "languageModelName_example",
    }
    try:
        # Get Llm Settings
        api_response = api_instance.get_llm_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling LargeLanguageModelApi->get_llm_settings: %s\n" % e)
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
languageModelName | LanguageModelNameSchema | | 

# LanguageModelNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_llm_settings.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_llm_settings.ApiResponseFor422) | Validation Error

#### get_llm_settings.ApiResponseFor200
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

#### get_llm_settings.ApiResponseFor422
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

# **get_llms_settings**
<a id="get_llms_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_llms_settings()

Get Llms Settings

Get the list of the Large Language Models

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import large_language_model_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = large_language_model_api.LargeLanguageModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Llms Settings
        api_response = api_instance.get_llms_settings()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling LargeLanguageModelApi->get_llms_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_llms_settings.ApiResponseFor200) | Successful Response

#### get_llms_settings.ApiResponseFor200
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

# **upsert_llm_setting**
<a id="upsert_llm_setting"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upsert_llm_setting(language_model_namebody)

Upsert Llm Setting

Upsert the Large Language Model setting

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import large_language_model_api
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
    api_instance = large_language_model_api.LargeLanguageModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'languageModelName': "languageModelName_example",
    }
    body = dict()
    try:
        # Upsert Llm Setting
        api_response = api_instance.upsert_llm_setting(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling LargeLanguageModelApi->upsert_llm_setting: %s\n" % e)
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
languageModelName | LanguageModelNameSchema | | 

# LanguageModelNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_llm_setting.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upsert_llm_setting.ApiResponseFor422) | Validation Error

#### upsert_llm_setting.ApiResponseFor200
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

#### upsert_llm_setting.ApiResponseFor422
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

