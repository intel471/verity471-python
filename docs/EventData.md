# EventData

Malware event data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **List[str]** | Arguments. | [optional] 
**attack_targets** | **List[Dict[str, str]]** | Attack targets. | [optional] 
**attack_type** | **str** | Attack type. | [optional] 
**bot_settings** | [**BotSettings**](BotSettings.md) | An object containing varying data types showing malware bot settings data. Contains any of but not limited the following fields: &#x60;exit_country&#x60;, &#x60;encryption&#x60;. | [optional] 
**command** | **str** | Command. | [optional] 
**component_type** | **str** | Type of component i.e. &#x60;CORE&#x60;. | [optional] 
**config_file** | [**File**](File.md) | Config file. | [optional] 
**controller** | [**EventController**](EventController.md) | Object containing the &#x60;url&#x60; and &#x60;ipv4&#x60; of a &#x60;controller&#x60;. | [optional] 
**controllers** | [**List[ControllerUrl]**](ControllerUrl.md) | An array of objects, each containing an individual controller&#39;s url. | [optional] 
**encryption** | [**List[Encryption]**](Encryption.md) | An array of &#x60;encryption&#x60; meta data. | [optional] 
**exfil_location** | **str** | Contains the url location of the exfiltration event. | [optional] 
**file** | [**File**](File.md) | Object containing fields of the &#x60;file&#x60;&#39;s hashes (&#x60;md5&#x60;, &#x60;sha1&#x60;, &#x60;sha256&#x60;) and file &#x60;type&#x60; and &#x60;size&#x60;. | [optional] 
**function** | **str** | Function name. | [optional] 
**inject_type** | **str** | Inject type. | [optional] 
**location** | [**Location**](Location.md) | The &#x60;url&#x60; object of the location of the event. | [optional] 
**parameters** | **List[Dict[str, str]]** | Parameters. | [optional] 
**plugin_name** | **str** | Plugin&#39;s name. | [optional] 
**plugin_type** | **str** | Type of plugin. i.e. &#x60;REMOTE_ACCESS&#x60;, &#x60;CREDENTIAL_STEALER&#x60;, &#x60;OTHER&#x60;. | [optional] 
**recipient_domains** | [**List[RecipientDomain]**](RecipientDomain.md) | Recipient domains. | [optional] 
**recipient_file** | [**File**](File.md) | Recipient file. | [optional] 
**redirects** | [**List[Redirect]**](Redirect.md) | An array of redirects. | [optional] 
**senders** | **List[str]** | Senders. | [optional] 
**service_type** | **str** | Type of service. | [optional] 
**settings** | [**Settings**](Settings.md) | An array of event related &#x60;settings&#x60; objects containing any of but not limited the following fields: &#x60;plugin_location&#x60;, &#x60;bot_version&#x60;, &#x60;compaign_id&#x60;, etc. | [optional] 
**target_type** | **str** | Type of target. | [optional] 
**template** | [**Template**](Template.md) | Template information. | [optional] 
**triggers** | [**List[Trigger]**](Trigger.md) | An array of objects, each containing the field &#x60;trigger&#x60;. | [optional] 

## Example

```python
from verity471.models.event_data import EventData

# TODO update the JSON string below
json = "{}"
# create an instance of EventData from a JSON string
event_data_instance = EventData.from_json(json)
# print the JSON string representation of the object
print(EventData.to_json())

# convert the object into a dict
event_data_dict = event_data_instance.to_dict()
# create an instance of EventData from a dict
event_data_from_dict = EventData.from_dict(event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


