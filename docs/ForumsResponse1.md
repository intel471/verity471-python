# ForumsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**description** | **str** | Description of forum | [optional] 
**id** | **str** | Forum unique id | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | [optional] 
**title** | **str** | Forum title | 

## Example

```python
from verity471.models.forums_response1 import ForumsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsResponse1 from a JSON string
forums_response1_instance = ForumsResponse1.from_json(json)
# print the JSON string representation of the object
print(ForumsResponse1.to_json())

# convert the object into a dict
forums_response1_dict = forums_response1_instance.to_dict()
# create an instance of ForumsResponse1 from a dict
forums_response1_from_dict = ForumsResponse1.from_dict(forums_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


