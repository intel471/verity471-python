# DatabaseDetails

Fields of a `database` product; set only when `kind` is `database`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**DatabaseBasicInfo**](DatabaseBasicInfo.md) |  | [optional] 
**victim** | [**VictimInfo**](VictimInfo.md) |  | [optional] 

## Example

```python
from verity471.models.database_details import DatabaseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseDetails from a JSON string
database_details_instance = DatabaseDetails.from_json(json)
# print the JSON string representation of the object
print(DatabaseDetails.to_json())

# convert the object into a dict
database_details_dict = database_details_instance.to_dict()
# create an instance of DatabaseDetails from a dict
database_details_from_dict = DatabaseDetails.from_dict(database_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


