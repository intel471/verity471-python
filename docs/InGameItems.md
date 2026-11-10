# InGameItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents_amount** | **str** | Number of agents, as a range (e.g. 0-4 Agents) | [optional] 
**arena** | **str** | Arena reached (e.g. Electro Valley) | [optional] 
**cars_amount** | **str** | Number of cars, as a range or label (e.g. All Cars) | [optional] 
**cash_amount** | **str** | In-game cash, as a range (e.g. 1 Billion- 7.99 Billion) | [optional] 
**free_name_change** | **str** | Whether a free name change is available (e.g. Unavailable) | [optional] 
**maxed_weapons** | **str** |  | [optional] 
**operators** | **List[str]** | Unlocked operators (e.g. Rainbow Six Siege operators) | [optional] 
**skins** | **List[str]** | Skin names on the account | [optional] 
**skins_amount** | **str** | Number of skins, as a range (e.g. 10-50 Skins) | [optional] 
**trophies** | **str** | Trophy count, as a range (e.g. 0-6000 Trophies) | [optional] 

## Example

```python
from verity471.models.in_game_items import InGameItems

# TODO update the JSON string below
json = "{}"
# create an instance of InGameItems from a JSON string
in_game_items_instance = InGameItems.from_json(json)
# print the JSON string representation of the object
print(InGameItems.to_json())

# convert the object into a dict
in_game_items_dict = in_game_items_instance.to_dict()
# create an instance of InGameItems from a dict
in_game_items_from_dict = InGameItems.from_dict(in_game_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


