# ArticleDetails

Fields of an `article` product; set only when `kind` is `article`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**ArticleBasicInfo**](ArticleBasicInfo.md) |  | [optional] 
**policy** | [**PolicyInfo**](PolicyInfo.md) |  | [optional] 
**quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**rating** | [**RatingOverall**](RatingOverall.md) |  | [optional] 
**shipping** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 
**victim** | [**VictimInfo**](VictimInfo.md) |  | [optional] 

## Example

```python
from verity471.models.article_details import ArticleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleDetails from a JSON string
article_details_instance = ArticleDetails.from_json(json)
# print the JSON string representation of the object
print(ArticleDetails.to_json())

# convert the object into a dict
article_details_dict = article_details_instance.to_dict()
# create an instance of ArticleDetails from a dict
article_details_from_dict = ArticleDetails.from_dict(article_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


