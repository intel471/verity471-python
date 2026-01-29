# IndicatorsStream

Stream of indicators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of indicators matching the query | [optional] 
**cursor_next** | **str** | Cursor for retrieving the next page of results | [optional] 
**indicators** | [**List[IntegrationsIndicator]**](IntegrationsIndicator.md) | List of indicators | [optional] 

## Example

```python
from verity471.models.indicators_stream import IndicatorsStream

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorsStream from a JSON string
indicators_stream_instance = IndicatorsStream.from_json(json)
# print the JSON string representation of the object
print(IndicatorsStream.to_json())

# convert the object into a dict
indicators_stream_dict = indicators_stream_instance.to_dict()
# create an instance of IndicatorsStream from a dict
indicators_stream_from_dict = IndicatorsStream.from_dict(indicators_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


