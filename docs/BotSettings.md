# BotSettings

Bot settings information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption** | [**List[Encryption]**](Encryption.md) | Encryption information. | [optional] 
**exit_country** | **str** | Country where the malware bot is running. | [optional] 
**settings** | **List[Dict[str, str]]** | Settings information. | [optional] 

## Example

```python
from verity471.models.bot_settings import BotSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BotSettings from a JSON string
bot_settings_instance = BotSettings.from_json(json)
# print the JSON string representation of the object
print(BotSettings.to_json())

# convert the object into a dict
bot_settings_dict = bot_settings_instance.to_dict()
# create an instance of BotSettings from a dict
bot_settings_from_dict = BotSettings.from_dict(bot_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


