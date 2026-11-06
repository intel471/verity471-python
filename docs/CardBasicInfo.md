# CardBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the card base (the batch the card is sold from) | [optional] 
**valid_rate** | **float** | Valid rate the vendor claims for the card base, as a percentage (0–100) | [optional] 

## Example

```python
from verity471.models.card_basic_info import CardBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CardBasicInfo from a JSON string
card_basic_info_instance = CardBasicInfo.from_json(json)
# print the JSON string representation of the object
print(CardBasicInfo.to_json())

# convert the object into a dict
card_basic_info_dict = card_basic_info_instance.to_dict()
# create an instance of CardBasicInfo from a dict
card_basic_info_from_dict = CardBasicInfo.from_dict(card_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


