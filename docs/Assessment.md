# Assessment

Report assessment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admiralty_code** | [**AdmiraltyCode**](AdmiraltyCode.md) |  | [optional] 
**confidence** | [**Confidence**](Confidence.md) |  | [optional] 

## Example

```python
from verity471.models.assessment import Assessment

# TODO update the JSON string below
json = "{}"
# create an instance of Assessment from a JSON string
assessment_instance = Assessment.from_json(json)
# print the JSON string representation of the object
print(Assessment.to_json())

# convert the object into a dict
assessment_dict = assessment_instance.to_dict()
# create an instance of Assessment from a dict
assessment_from_dict = Assessment.from_dict(assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


