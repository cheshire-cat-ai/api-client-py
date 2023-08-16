# cheshire_cat_api.model.body_upload_url.BodyUploadUrl

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | URL of the website to which you want to save the content | 
**chunk_size** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum length of each chunk after the document is split (in characters) | [optional] if omitted the server will use the default value of 400
**chunk_overlap** | decimal.Decimal, int,  | decimal.Decimal,  | Chunk overlap (in characters) | [optional] if omitted the server will use the default value of 100
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

