# cheshire_cat_api.SettingsLargeLanguageModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_llm_settings**](SettingsLargeLanguageModelApi.md#get_llm_settings) | **GET** /settings/llm/ | Get Llm Settings
[**upsert_llm_setting**](SettingsLargeLanguageModelApi.md#upsert_llm_setting) | **PUT** /settings/llm/{languageModelName} | Upsert Llm Setting


# **get_llm_settings**
> object get_llm_settings()

Get Llm Settings

Get the list of the Large Language Models

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
    api_instance = cheshire_cat_api.SettingsLargeLanguageModelApi(api_client)

    try:
        # Get Llm Settings
        api_response = api_instance.get_llm_settings()
        print("The response of SettingsLargeLanguageModelApi->get_llm_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsLargeLanguageModelApi->get_llm_settings: %s\n" % e)
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

# **upsert_llm_setting**
> object upsert_llm_setting(language_model_name, body)

Upsert Llm Setting

Upsert the Large Language Model setting

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
    api_instance = cheshire_cat_api.SettingsLargeLanguageModelApi(api_client)
    language_model_name = 'language_model_name_example' # str | 
    body = {"openai_api_key":"your-key-here"} # object | 

    try:
        # Upsert Llm Setting
        api_response = api_instance.upsert_llm_setting(language_model_name, body)
        print("The response of SettingsLargeLanguageModelApi->upsert_llm_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsLargeLanguageModelApi->upsert_llm_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_model_name** | **str**|  | 
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

