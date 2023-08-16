# BodyUploadUrl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the website to which you want to save the content | 
**chunk_size** | **int** | Maximum length of each chunk after the document is split (in characters) | [optional] [default to 400]
**chunk_overlap** | **int** | Chunk overlap (in characters) | [optional] [default to 100]

## Example

```python
from cheshire_cat_api.models.body_upload_url import BodyUploadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of BodyUploadUrl from a JSON string
body_upload_url_instance = BodyUploadUrl.from_json(json)
# print the JSON string representation of the object
print BodyUploadUrl.to_json()

# convert the object into a dict
body_upload_url_dict = body_upload_url_instance.to_dict()
# create an instance of BodyUploadUrl from a dict
body_upload_url_form_dict = body_upload_url.from_dict(body_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


