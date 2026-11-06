# PersonalInfoDetails

Fields of a `personal_info` product; set only when `kind` is `personal_info`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**PersonalInfoBasicInfo**](PersonalInfoBasicInfo.md) |  | [optional] 
**policy** | [**PolicyInfo**](PolicyInfo.md) |  | [optional] 
**shipping** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 
**victim** | [**VictimInfo**](VictimInfo.md) |  | [optional] 

## Example

```python
from verity471.models.personal_info_details import PersonalInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalInfoDetails from a JSON string
personal_info_details_instance = PersonalInfoDetails.from_json(json)
# print the JSON string representation of the object
print(PersonalInfoDetails.to_json())

# convert the object into a dict
personal_info_details_dict = personal_info_details_instance.to_dict()
# create an instance of PersonalInfoDetails from a dict
personal_info_details_from_dict = PersonalInfoDetails.from_dict(personal_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


