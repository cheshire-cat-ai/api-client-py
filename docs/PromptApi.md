# cheshire_cat_api.PromptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_prompt_settings**](PromptApi.md#get_default_prompt_settings) | **GET** /prompt/settings/ | Get Default Prompt Settings


# **get_default_prompt_settings**
> object get_default_prompt_settings()

Get Default Prompt Settings

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
    api_instance = cheshire_cat_api.PromptApi(api_client)

    try:
        # Get Default Prompt Settings
        api_response = api_instance.get_default_prompt_settings()
        print("The response of PromptApi->get_default_prompt_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptApi->get_default_prompt_settings: %s\n" % e)
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

