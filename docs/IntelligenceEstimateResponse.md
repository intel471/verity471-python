# IntelligenceEstimateResponse

Report related intelligence estimate data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview** | **str** |  | [optional] 
**threat_rating** | [**ThreatRating**](ThreatRating.md) |  | 
**security_assessment** | [**SecurityAssessment**](SecurityAssessment.md) |  | 
**text_toc** | **str** |  | [optional] 
**report_location** | [**ReportLocation**](ReportLocation.md) |  | 
**is_country_of_interest** | **bool** |  | 

## Example

```python
from verity471.models.intelligence_estimate_response import IntelligenceEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntelligenceEstimateResponse from a JSON string
intelligence_estimate_response_instance = IntelligenceEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(IntelligenceEstimateResponse.to_json())

# convert the object into a dict
intelligence_estimate_response_dict = intelligence_estimate_response_instance.to_dict()
# create an instance of IntelligenceEstimateResponse from a dict
intelligence_estimate_response_from_dict = IntelligenceEstimateResponse.from_dict(intelligence_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


