# ReportsVictimResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the victim | 
**links** | [**List[Links]**](Links.md) | List of URLs associated with the victim | [optional] 
**country** | **str** | Country of the victim | [optional] 
**revenue** | **str** | Revenue information of the victim | [optional] 
**region** | **str** | Region information of the victim | [optional] 
**industries** | [**List[Industries]**](Industries.md) | List of Industries associated with the victim | [optional] 

## Example

```python
from verity471.models.reports_victim_response import ReportsVictimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsVictimResponse from a JSON string
reports_victim_response_instance = ReportsVictimResponse.from_json(json)
# print the JSON string representation of the object
print(ReportsVictimResponse.to_json())

# convert the object into a dict
reports_victim_response_dict = reports_victim_response_instance.to_dict()
# create an instance of ReportsVictimResponse from a dict
reports_victim_response_from_dict = ReportsVictimResponse.from_dict(reports_victim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


