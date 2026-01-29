# CredentialSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the source | [optional] 
**links** | [**Links**](Links.md) |  | 
**type** | **str** | Type of the source | 

## Example

```python
from verity471.models.credential_source import CredentialSource

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSource from a JSON string
credential_source_instance = CredentialSource.from_json(json)
# print the JSON string representation of the object
print(CredentialSource.to_json())

# convert the object into a dict
credential_source_dict = credential_source_instance.to_dict()
# create an instance of CredentialSource from a dict
credential_source_from_dict = CredentialSource.from_dict(credential_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


