<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.plugins_api.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_plugin**](#delete_plugin) | **delete** /plugins/{plugin_id} | Delete Plugin
[**get_available_plugins**](#get_available_plugins) | **get** /plugins/ | Get Available Plugins
[**get_plugin_details**](#get_plugin_details) | **get** /plugins/{plugin_id} | Get Plugin Details
[**get_plugin_settings**](#get_plugin_settings) | **get** /plugins/settings/{plugin_id} | Get Plugin Settings
[**get_plugins_settings**](#get_plugins_settings) | **get** /plugins/settings/ | Get Plugins Settings
[**install_plugin**](#install_plugin) | **post** /plugins/upload/ | Install Plugin
[**install_plugin_from_registry**](#install_plugin_from_registry) | **post** /plugins/upload/registry | Install Plugin From Registry
[**toggle_plugin**](#toggle_plugin) | **put** /plugins/toggle/{plugin_id} | Toggle Plugin
[**upsert_plugin_settings**](#upsert_plugin_settings) | **put** /plugins/settings/{plugin_id} | Upsert Plugin Settings

# **delete_plugin**
<a id="delete_plugin"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_plugin(plugin_id)

Delete Plugin

Physically remove plugin.

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'plugin_id': "plugin_id_example",
    }
    try:
        # Delete Plugin
        api_response = api_instance.delete_plugin(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
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
plugin_id | PluginIdSchema | | 

# PluginIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_plugin.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_plugin.ApiResponseFor422) | Validation Error

#### delete_plugin.ApiResponseFor200
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

#### delete_plugin.ApiResponseFor422
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

# **get_available_plugins**
<a id="get_available_plugins"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_available_plugins()

Get Available Plugins

List available plugins

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plugins_api.PluginsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Available Plugins
        api_response = api_instance.get_available_plugins()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->get_available_plugins: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_available_plugins.ApiResponseFor200) | Successful Response

#### get_available_plugins.ApiResponseFor200
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

# **get_plugin_details**
<a id="get_plugin_details"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_plugin_details(plugin_id)

Get Plugin Details

Returns information on a single plugin

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'plugin_id': "plugin_id_example",
    }
    try:
        # Get Plugin Details
        api_response = api_instance.get_plugin_details(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_details: %s\n" % e)
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
plugin_id | PluginIdSchema | | 

# PluginIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_plugin_details.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_plugin_details.ApiResponseFor422) | Validation Error

#### get_plugin_details.ApiResponseFor200
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

#### get_plugin_details.ApiResponseFor422
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

# **get_plugin_settings**
<a id="get_plugin_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_plugin_settings(plugin_id)

Get Plugin Settings

Returns the settings of a specific plugin

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'plugin_id': "plugin_id_example",
    }
    try:
        # Get Plugin Settings
        api_response = api_instance.get_plugin_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_settings: %s\n" % e)
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
plugin_id | PluginIdSchema | | 

# PluginIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_plugin_settings.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_plugin_settings.ApiResponseFor422) | Validation Error

#### get_plugin_settings.ApiResponseFor200
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

#### get_plugin_settings.ApiResponseFor422
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

# **get_plugins_settings**
<a id="get_plugins_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_plugins_settings()

Get Plugins Settings

Returns the settings of all the plugins

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plugins_api.PluginsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Plugins Settings
        api_response = api_instance.get_plugins_settings()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->get_plugins_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_plugins_settings.ApiResponseFor200) | Successful Response

#### get_plugins_settings.ApiResponseFor200
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

# **install_plugin**
<a id="install_plugin"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} install_plugin()

Install Plugin

Install a new plugin from a zip file

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
from cheshire_cat_api.model.http_validation_error import HTTPValidationError
from cheshire_cat_api.model.body_install_plugin import BodyInstallPlugin
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only optional values
    body = dict(
        file=open('/path/to/file', 'rb'),
    )
    try:
        # Install Plugin
        api_response = api_instance.install_plugin(
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->install_plugin: %s\n" % e)
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
[**BodyInstallPlugin**](../../models/BodyInstallPlugin.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#install_plugin.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#install_plugin.ApiResponseFor422) | Validation Error

#### install_plugin.ApiResponseFor200
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

#### install_plugin.ApiResponseFor422
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

# **install_plugin_from_registry**
<a id="install_plugin_from_registry"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} install_plugin_from_registry(body)

Install Plugin From Registry

Install a new plugin from external repository

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict()
    try:
        # Install Plugin From Registry
        api_response = api_instance.install_plugin_from_registry(
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->install_plugin_from_registry: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#install_plugin_from_registry.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#install_plugin_from_registry.ApiResponseFor422) | Validation Error

#### install_plugin_from_registry.ApiResponseFor200
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

#### install_plugin_from_registry.ApiResponseFor422
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

# **toggle_plugin**
<a id="toggle_plugin"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} toggle_plugin(plugin_id)

Toggle Plugin

Enable or disable a single plugin

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'plugin_id': "plugin_id_example",
    }
    try:
        # Toggle Plugin
        api_response = api_instance.toggle_plugin(
            path_params=path_params,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->toggle_plugin: %s\n" % e)
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
plugin_id | PluginIdSchema | | 

# PluginIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#toggle_plugin.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#toggle_plugin.ApiResponseFor422) | Validation Error

#### toggle_plugin.ApiResponseFor200
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

#### toggle_plugin.ApiResponseFor422
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

# **upsert_plugin_settings**
<a id="upsert_plugin_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upsert_plugin_settings(plugin_idbody)

Upsert Plugin Settings

Updates the settings of a specific plugin

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import plugins_api
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
    api_instance = plugins_api.PluginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'plugin_id': "plugin_id_example",
    }
    body = dict()
    try:
        # Upsert Plugin Settings
        api_response = api_instance.upsert_plugin_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PluginsApi->upsert_plugin_settings: %s\n" % e)
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
plugin_id | PluginIdSchema | | 

# PluginIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_plugin_settings.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#upsert_plugin_settings.ApiResponseFor422) | Validation Error

#### upsert_plugin_settings.ApiResponseFor200
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

#### upsert_plugin_settings.ApiResponseFor422
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

