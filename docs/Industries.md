# Industries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry** | **str** | Name of the industry | 
**sector** | **str** | Sector of the industry | 

## Example

```python
from verity471.models.industries import Industries

# TODO update the JSON string below
json = "{}"
# create an instance of Industries from a JSON string
industries_instance = Industries.from_json(json)
# print the JSON string representation of the object
print(Industries.to_json())

# convert the object into a dict
industries_dict = industries_instance.to_dict()
# create an instance of Industries from a dict
industries_from_dict = Industries.from_dict(industries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


