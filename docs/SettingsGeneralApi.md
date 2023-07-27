# cheshire_cat_api.SettingsGeneralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_setting**](SettingsGeneralApi.md#create_setting) | **POST** /settings/ | Create Setting
[**delete_setting**](SettingsGeneralApi.md#delete_setting) | **DELETE** /settings/{settingId} | Delete Setting
[**get_setting**](SettingsGeneralApi.md#get_setting) | **GET** /settings/{settingId} | Get Setting
[**get_settings**](SettingsGeneralApi.md#get_settings) | **GET** /settings/ | Get Settings
[**update_setting**](SettingsGeneralApi.md#update_setting) | **PUT** /settings/{settingId} | Update Setting


# **create_setting**
> object create_setting(setting_body)

Create Setting

Create a new setting in the database

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.models.setting_body import SettingBody
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
    api_instance = cheshire_cat_api.SettingsGeneralApi(api_client)
    setting_body = cheshire_cat_api.SettingBody() # SettingBody | 

    try:
        # Create Setting
        api_response = api_instance.create_setting(setting_body)
        print("The response of SettingsGeneralApi->create_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsGeneralApi->create_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_body** | [**SettingBody**](SettingBody.md)|  | 

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

# **delete_setting**
> object delete_setting(setting_id)

Delete Setting

Delete a specific setting in the database

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
    api_instance = cheshire_cat_api.SettingsGeneralApi(api_client)
    setting_id = 'setting_id_example' # str | 

    try:
        # Delete Setting
        api_response = api_instance.delete_setting(setting_id)
        print("The response of SettingsGeneralApi->delete_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsGeneralApi->delete_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id** | **str**|  | 

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

# **get_setting**
> object get_setting(setting_id)

Get Setting

Get the a specific setting from the database

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
    api_instance = cheshire_cat_api.SettingsGeneralApi(api_client)
    setting_id = 'setting_id_example' # str | 

    try:
        # Get Setting
        api_response = api_instance.get_setting(setting_id)
        print("The response of SettingsGeneralApi->get_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsGeneralApi->get_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id** | **str**|  | 

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

# **get_settings**
> object get_settings(search=search)

Get Settings

Get the entire list of settings available in the database

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
    api_instance = cheshire_cat_api.SettingsGeneralApi(api_client)
    search = '' # str |  (optional) (default to '')

    try:
        # Get Settings
        api_response = api_instance.get_settings(search=search)
        print("The response of SettingsGeneralApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsGeneralApi->get_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] [default to &#39;&#39;]

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

# **update_setting**
> object update_setting(setting_id, setting_body)

Update Setting

Update a specific setting in the database if it exists

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.models.setting_body import SettingBody
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
    api_instance = cheshire_cat_api.SettingsGeneralApi(api_client)
    setting_id = 'setting_id_example' # str | 
    setting_body = cheshire_cat_api.SettingBody() # SettingBody | 

    try:
        # Update Setting
        api_response = api_instance.update_setting(setting_id, setting_body)
        print("The response of SettingsGeneralApi->update_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsGeneralApi->update_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id** | **str**|  | 
 **setting_body** | [**SettingBody**](SettingBody.md)|  | 

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

