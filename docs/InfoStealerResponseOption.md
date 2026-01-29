# InfoStealerResponseOption

Array of malware family objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malware_family** | **str** | Malware family name. | [optional] 
**malware_install_path** | **str** | Malware installation path. | [optional] 
**screenshot_path** | **str** | Screenshot path. | [optional] 
**infection_ts** | **str** | Date of infection. | [optional] 
**machine_id** | **str** | Id of the machine. | [optional] 
**pc_name** | **str** | Name of the machine. | [optional] 
**computer_username** | **str** | Name of the user account. | [optional] 
**ip** | **str** | IP address. | [optional] 
**os** | **str** | Operating system. | [optional] 
**antivirus_software** | **str** | Antivirus software. | [optional] 
**isp** | **str** | Internet Service Provider. | [optional] 
**version** | **str** | Version. | [optional] 

## Example

```python
from verity471.models.info_stealer_response_option import InfoStealerResponseOption

# TODO update the JSON string below
json = "{}"
# create an instance of InfoStealerResponseOption from a JSON string
info_stealer_response_option_instance = InfoStealerResponseOption.from_json(json)
# print the JSON string representation of the object
print(InfoStealerResponseOption.to_json())

# convert the object into a dict
info_stealer_response_option_dict = info_stealer_response_option_instance.to_dict()
# create an instance of InfoStealerResponseOption from a dict
info_stealer_response_option_from_dict = InfoStealerResponseOption.from_dict(info_stealer_response_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


