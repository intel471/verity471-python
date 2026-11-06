# DatabaseBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Dump file name with its size (e.g. name.7z [2.63 GB]) | [optional] 
**is_valid** | **bool** | Data is valid flag | [optional] 
**records** | **int** | Record count in a DB dump. | [optional] 
**year** | **int** | Year the database dates from, as stated by the listing, four digits | [optional] 

## Example

```python
from verity471.models.database_basic_info import DatabaseBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseBasicInfo from a JSON string
database_basic_info_instance = DatabaseBasicInfo.from_json(json)
# print the JSON string representation of the object
print(DatabaseBasicInfo.to_json())

# convert the object into a dict
database_basic_info_dict = database_basic_info_instance.to_dict()
# create an instance of DatabaseBasicInfo from a dict
database_basic_info_from_dict = DatabaseBasicInfo.from_dict(database_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


