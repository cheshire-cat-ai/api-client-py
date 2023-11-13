# cheshire_cat_api.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_plugin**](PluginsApi.md#delete_plugin) | **DELETE** /plugins/{plugin_id} | Delete Plugin
[**get_available_plugins**](PluginsApi.md#get_available_plugins) | **GET** /plugins/ | Get Available Plugins
[**get_plugin_details**](PluginsApi.md#get_plugin_details) | **GET** /plugins/{plugin_id} | Get Plugin Details
[**get_plugin_settings**](PluginsApi.md#get_plugin_settings) | **GET** /plugins/settings/{plugin_id} | Get Plugin Settings
[**get_plugins_settings**](PluginsApi.md#get_plugins_settings) | **GET** /plugins/settings/ | Get Plugins Settings
[**install_plugin**](PluginsApi.md#install_plugin) | **POST** /plugins/upload/ | Install Plugin
[**install_plugin_from_registry**](PluginsApi.md#install_plugin_from_registry) | **POST** /plugins/upload/registry | Install Plugin From Registry
[**toggle_plugin**](PluginsApi.md#toggle_plugin) | **PUT** /plugins/toggle/{plugin_id} | Toggle Plugin
[**upsert_plugin_settings**](PluginsApi.md#upsert_plugin_settings) | **PUT** /plugins/settings/{plugin_id} | Upsert Plugin Settings


# **delete_plugin**
> object delete_plugin(plugin_id)

Delete Plugin

Physically remove plugin.

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 

    try:
        # Delete Plugin
        api_response = api_instance.delete_plugin(plugin_id)
        print("The response of PluginsApi->delete_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

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

# **get_available_plugins**
> object get_available_plugins(query=query)

Get Available Plugins

List available plugins

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        # Get Available Plugins
        api_response = api_instance.get_available_plugins(query=query)
        print("The response of PluginsApi->get_available_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_available_plugins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

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

# **get_plugin_details**
> object get_plugin_details(plugin_id)

Get Plugin Details

Returns information on a single plugin

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 

    try:
        # Get Plugin Details
        api_response = api_instance.get_plugin_details(plugin_id)
        print("The response of PluginsApi->get_plugin_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

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

# **get_plugin_settings**
> object get_plugin_settings(plugin_id)

Get Plugin Settings

Returns the settings of a specific plugin

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 

    try:
        # Get Plugin Settings
        api_response = api_instance.get_plugin_settings(plugin_id)
        print("The response of PluginsApi->get_plugin_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

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

# **get_plugins_settings**
> object get_plugins_settings()

Get Plugins Settings

Returns the settings of all the plugins

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)

    try:
        # Get Plugins Settings
        api_response = api_instance.get_plugins_settings()
        print("The response of PluginsApi->get_plugins_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugins_settings: %s\n" % e)
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

# **install_plugin**
> object install_plugin(file)

Install Plugin

Install a new plugin from a zip file

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    file = None # bytearray | 

    try:
        # Install Plugin
        api_response = api_instance.install_plugin(file)
        print("The response of PluginsApi->install_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->install_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_plugin_from_registry**
> object install_plugin_from_registry(body)

Install Plugin From Registry

Install a new plugin from registry

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    body = None # object | 

    try:
        # Install Plugin From Registry
        api_response = api_instance.install_plugin_from_registry(body)
        print("The response of PluginsApi->install_plugin_from_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->install_plugin_from_registry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **toggle_plugin**
> object toggle_plugin(plugin_id)

Toggle Plugin

Enable or disable a single plugin

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 

    try:
        # Toggle Plugin
        api_response = api_instance.toggle_plugin(plugin_id)
        print("The response of PluginsApi->toggle_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->toggle_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

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

# **upsert_plugin_settings**
> object upsert_plugin_settings(plugin_id, body)

Upsert Plugin Settings

Updates the settings of a specific plugin

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
    api_instance = cheshire_cat_api.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    body = None # object | 

    try:
        # Upsert Plugin Settings
        api_response = api_instance.upsert_plugin_settings(plugin_id, body)
        print("The response of PluginsApi->upsert_plugin_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upsert_plugin_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **body** | **object**|  | 

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

