# Redirect

Redirect information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the redirect. | [optional] 
**host** | **str** | Host of the redirect. | [optional] 

## Example

```python
from verity471.models.redirect import Redirect

# TODO update the JSON string below
json = "{}"
# create an instance of Redirect from a JSON string
redirect_instance = Redirect.from_json(json)
# print the JSON string representation of the object
print(Redirect.to_json())

# convert the object into a dict
redirect_dict = redirect_instance.to_dict()
# create an instance of Redirect from a dict
redirect_from_dict = Redirect.from_dict(redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


