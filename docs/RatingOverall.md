# RatingOverall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** | Maximum of the rating scale (e.g. 5 or 10). | [optional] 
**value** | **float** | Overall rating value from the listing | [optional] 

## Example

```python
from verity471.models.rating_overall import RatingOverall

# TODO update the JSON string below
json = "{}"
# create an instance of RatingOverall from a JSON string
rating_overall_instance = RatingOverall.from_json(json)
# print the JSON string representation of the object
print(RatingOverall.to_json())

# convert the object into a dict
rating_overall_dict = rating_overall_instance.to_dict()
# create an instance of RatingOverall from a dict
rating_overall_from_dict = RatingOverall.from_dict(rating_overall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


