# SettingBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **object** |  | 
**category** | **str** |  | [optional] 

## Example

```python
from cheshire_cat_api.models.setting_body import SettingBody

# TODO update the JSON string below
json = "{}"
# create an instance of SettingBody from a JSON string
setting_body_instance = SettingBody.from_json(json)
# print the JSON string representation of the object
print SettingBody.to_json()

# convert the object into a dict
setting_body_dict = setting_body_instance.to_dict()
# create an instance of SettingBody from a dict
setting_body_form_dict = setting_body.from_dict(setting_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


