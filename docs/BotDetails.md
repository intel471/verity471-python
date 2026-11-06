# BotDetails

Fields of a `bot` product; set only when `kind` is `bot`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**FileInfo**](FileInfo.md) |  | [optional] 
**infostealer** | [**BotInfostealerInfo**](BotInfostealerInfo.md) |  | [optional] 
**installed_ts** | **datetime** | When the stealer infected the victim machine (install time) | [optional] 
**other** | [**BotOtherInfo**](BotOtherInfo.md) |  | [optional] 
**stealer** | **str** | Malware family that produced the log, e.g. lumma, rhadamanthys, stealc, vidar | [optional] 

## Example

```python
from verity471.models.bot_details import BotDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BotDetails from a JSON string
bot_details_instance = BotDetails.from_json(json)
# print the JSON string representation of the object
print(BotDetails.to_json())

# convert the object into a dict
bot_details_dict = bot_details_instance.to_dict()
# create an instance of BotDetails from a dict
bot_details_from_dict = BotDetails.from_dict(bot_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


