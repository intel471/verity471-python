# Cvss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**score** | **float** |  | 

## Example

```python
from verity471.models.cvss import Cvss

# TODO update the JSON string below
json = "{}"
# create an instance of Cvss from a JSON string
cvss_instance = Cvss.from_json(json)
# print the JSON string representation of the object
print(Cvss.to_json())

# convert the object into a dict
cvss_dict = cvss_instance.to_dict()
# create an instance of Cvss from a dict
cvss_from_dict = Cvss.from_dict(cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


