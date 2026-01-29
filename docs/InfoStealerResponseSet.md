# InfoStealerResponseSet

Array of malware family objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malware_family** | **List[str]** | Malware family name. | [optional] 
**malware_install_path** | **List[str]** | Malware installation path. | [optional] 
**screenshot_path** | **List[str]** | Screenshot path. | [optional] 
**infection_ts** | **List[str]** | Date of infection. | [optional] 
**machine_id** | **List[str]** | Id of the machine. | [optional] 
**pc_name** | **List[str]** | Name of the machine. | [optional] 
**computer_username** | **List[str]** | Name of the user account. | [optional] 
**ip** | **List[str]** | IP address. | [optional] 
**os** | **List[str]** | Operating system. | [optional] 
**antivirus_software** | **List[str]** | Antivirus software. | [optional] 
**isp** | **List[str]** | Internet Service Provider. | [optional] 
**version** | **List[str]** | Version. | [optional] 

## Example

```python
from verity471.models.info_stealer_response_set import InfoStealerResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of InfoStealerResponseSet from a JSON string
info_stealer_response_set_instance = InfoStealerResponseSet.from_json(json)
# print the JSON string representation of the object
print(InfoStealerResponseSet.to_json())

# convert the object into a dict
info_stealer_response_set_dict = info_stealer_response_set_instance.to_dict()
# create an instance of InfoStealerResponseSet from a dict
info_stealer_response_set_from_dict = InfoStealerResponseSet.from_dict(info_stealer_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


