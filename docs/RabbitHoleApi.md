# cheshire_cat_api.RabbitHoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowed_mimetypes**](RabbitHoleApi.md#get_allowed_mimetypes) | **GET** /rabbithole/allowed-mimetypes/ | Get Allowed Mimetypes
[**upload_file**](RabbitHoleApi.md#upload_file) | **POST** /rabbithole/ | Upload File
[**upload_memory**](RabbitHoleApi.md#upload_memory) | **POST** /rabbithole/memory/ | Upload Memory
[**upload_url**](RabbitHoleApi.md#upload_url) | **POST** /rabbithole/web/ | Upload Url


# **get_allowed_mimetypes**
> object get_allowed_mimetypes()

Get Allowed Mimetypes

Retrieve the allowed mimetypes that can be ingested by the Rabbit Hole

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
    api_instance = cheshire_cat_api.RabbitHoleApi(api_client)

    try:
        # Get Allowed Mimetypes
        api_response = api_instance.get_allowed_mimetypes()
        print("The response of RabbitHoleApi->get_allowed_mimetypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RabbitHoleApi->get_allowed_mimetypes: %s\n" % e)
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

# **upload_file**
> object upload_file(file, chunk_size=chunk_size, chunk_overlap=chunk_overlap)

Upload File

Upload a file containing text (.txt, .md, .pdf, etc.). File content will be extracted and segmented into chunks. Chunks will be then vectorized and stored into documents memory.

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
    api_instance = cheshire_cat_api.RabbitHoleApi(api_client)
    file = None # bytearray | 
    chunk_size = 400 # int | Maximum length of each chunk after the document is split (in characters) (optional) (default to 400)
    chunk_overlap = 100 # int | Chunk overlap (in characters) (optional) (default to 100)

    try:
        # Upload File
        api_response = api_instance.upload_file(file, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        print("The response of RabbitHoleApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RabbitHoleApi->upload_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **chunk_size** | **int**| Maximum length of each chunk after the document is split (in characters) | [optional] [default to 400]
 **chunk_overlap** | **int**| Chunk overlap (in characters) | [optional] [default to 100]

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

# **upload_memory**
> object upload_memory(file)

Upload Memory

Upload a memory json file to the cat memory

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
    api_instance = cheshire_cat_api.RabbitHoleApi(api_client)
    file = None # bytearray | 

    try:
        # Upload Memory
        api_response = api_instance.upload_memory(file)
        print("The response of RabbitHoleApi->upload_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RabbitHoleApi->upload_memory: %s\n" % e)
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

# **upload_url**
> object upload_url(body_upload_url)

Upload Url

Upload a url. Website content will be extracted and segmented into chunks. Chunks will be then vectorized and stored into documents memory.

### Example

```python
import time
import os
import cheshire_cat_api
from cheshire_cat_api.models.body_upload_url import BodyUploadUrl
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
    api_instance = cheshire_cat_api.RabbitHoleApi(api_client)
    body_upload_url = cheshire_cat_api.BodyUploadUrl() # BodyUploadUrl | 

    try:
        # Upload Url
        api_response = api_instance.upload_url(body_upload_url)
        print("The response of RabbitHoleApi->upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RabbitHoleApi->upload_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_upload_url** | [**BodyUploadUrl**](BodyUploadUrl.md)|  | 

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

