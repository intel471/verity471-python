# File

File information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5** | **str** | MD5 hash of the file | [optional] 
**sha1** | **str** | SHA-1 hash of the file | [optional] 
**sha256** | **str** | SHA-256 hash of the file | [optional] 
**size** | **int** | Size of the file in bytes | [optional] 
**ssdeep** | **str** | SSDeep hash of the file | [optional] 
**type** | **str** | Type of the file | [optional] 

## Example

```python
from verity471.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


