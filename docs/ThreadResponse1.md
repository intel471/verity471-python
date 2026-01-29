# ThreadResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**id** | **str** | Thread unique id | 
**links** | [**SourcesLinks**](SourcesLinks.md) |  | [optional] 
**post_count** | **int** | Number of posts within a thread | 
**topic** | **str** | Topic name | [optional] 
**topic_original** | **str** | Original topic name | [optional] 
**translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 

## Example

```python
from verity471.models.thread_response1 import ThreadResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadResponse1 from a JSON string
thread_response1_instance = ThreadResponse1.from_json(json)
# print the JSON string representation of the object
print(ThreadResponse1.to_json())

# convert the object into a dict
thread_response1_dict = thread_response1_instance.to_dict()
# create an instance of ThreadResponse1 from a dict
thread_response1_from_dict = ThreadResponse1.from_dict(thread_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


