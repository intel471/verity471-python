# CountryProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**country_iso_code** | **str** |  | [optional] 
**id** | **str** |  | 
**information_ts** | **str** |  | 
**is_country_of_interest** | **bool** |  | 
**security_assessment** | [**SecurityAssessment**](SecurityAssessment.md) |  | [optional] 
**threat_rating** | [**ThreatRating**](ThreatRating.md) |  | [optional] 

## Example

```python
from verity471.models.country_profile_response import CountryProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountryProfileResponse from a JSON string
country_profile_response_instance = CountryProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CountryProfileResponse.to_json())

# convert the object into a dict
country_profile_response_dict = country_profile_response_instance.to_dict()
# create an instance of CountryProfileResponse from a dict
country_profile_response_from_dict = CountryProfileResponse.from_dict(country_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


