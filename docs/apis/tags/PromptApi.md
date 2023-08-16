<a id="__pageTop"></a>
# cheshire_cat_api.apis.tags.prompt_api.PromptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_prompt_settings**](#get_default_prompt_settings) | **get** /prompt/settings/ | Get Default Prompt Settings

# **get_default_prompt_settings**
<a id="get_default_prompt_settings"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_default_prompt_settings()

Get Default Prompt Settings

### Example

```python
import cheshire_cat_api
from cheshire_cat_api.apis.tags import prompt_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cheshire_cat_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with cheshire_cat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prompt_api.PromptApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Default Prompt Settings
        api_response = api_instance.get_default_prompt_settings()
        pprint(api_response)
    except cheshire_cat_api.ApiException as e:
        print("Exception when calling PromptApi->get_default_prompt_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_default_prompt_settings.ApiResponseFor200) | Successful Response

#### get_default_prompt_settings.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

