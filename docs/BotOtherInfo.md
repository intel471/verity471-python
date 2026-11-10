# BotOtherInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Listing URL. | [optional] 
**name** | **str** | Bot id/name/hash on the market. | [optional] 

## Example

```python
from verity471.models.bot_other_info import BotOtherInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BotOtherInfo from a JSON string
bot_other_info_instance = BotOtherInfo.from_json(json)
# print the JSON string representation of the object
print(BotOtherInfo.to_json())

# convert the object into a dict
bot_other_info_dict = bot_other_info_instance.to_dict()
# create an instance of BotOtherInfo from a dict
bot_other_info_from_dict = BotOtherInfo.from_dict(bot_other_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


