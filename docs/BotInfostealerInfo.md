# BotInfostealerInfo

The infected victim host the log was taken from: operating system, ISP, IP address, country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Victim country (ISO). | [optional] 
**description** | **str** | Listing description. | [optional] 
**internet_service_provider** | **str** | Victim ISP. | [optional] 
**ip_address** | **str** | Victim IP. | [optional] 
**operating_system** | **str** | Victim OS. | [optional] 

## Example

```python
from verity471.models.bot_infostealer_info import BotInfostealerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BotInfostealerInfo from a JSON string
bot_infostealer_info_instance = BotInfostealerInfo.from_json(json)
# print the JSON string representation of the object
print(BotInfostealerInfo.to_json())

# convert the object into a dict
bot_infostealer_info_dict = bot_infostealer_info_instance.to_dict()
# create an instance of BotInfostealerInfo from a dict
bot_infostealer_info_from_dict = BotInfostealerInfo.from_dict(bot_infostealer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


