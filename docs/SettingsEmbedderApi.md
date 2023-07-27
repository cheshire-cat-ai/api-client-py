# cheshire_cat_api.SettingsEmbedderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_embedder_settings**](SettingsEmbedderApi.md#get_embedder_settings) | **GET** /settings/embedder/ | Get Embedder Settings
[**upsert_embedder_setting**](SettingsEmbedderApi.md#upsert_embedder_setting) | **PUT** /settings/embedder/{languageEmbedderName} | Upsert Embedder Setting


# **get_embedder_settings**
> object get_embedder_settings()

Get Embedder Settings

Get the list of the Embedders

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
    api_instance = cheshire_cat_api.SettingsEmbedderApi(api_client)

    try:
        # Get Embedder Settings
        api_response = api_instance.get_embedder_settings()
        print("The response of SettingsEmbedderApi->get_embedder_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsEmbedderApi->get_embedder_settings: %s\n" % e)
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

# **upsert_embedder_setting**
> object upsert_embedder_setting(language_embedder_name, body)

Upsert Embedder Setting

Upsert the Embedder setting

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
    api_instance = cheshire_cat_api.SettingsEmbedderApi(api_client)
    language_embedder_name = 'language_embedder_name_example' # str | 
    body = {"openai_api_key":"your-key-here"} # object | 

    try:
        # Upsert Embedder Setting
        api_response = api_instance.upsert_embedder_setting(language_embedder_name, body)
        print("The response of SettingsEmbedderApi->upsert_embedder_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsEmbedderApi->upsert_embedder_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_embedder_name** | **str**|  | 
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

