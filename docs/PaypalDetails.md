# PaypalDetails

Fields of a `paypal` product; set only when `kind` is `paypal`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**PaypalBasicInfo**](PaypalBasicInfo.md) |  | [optional] 

## Example

```python
from verity471.models.paypal_details import PaypalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaypalDetails from a JSON string
paypal_details_instance = PaypalDetails.from_json(json)
# print the JSON string representation of the object
print(PaypalDetails.to_json())

# convert the object into a dict
paypal_details_dict = paypal_details_instance.to_dict()
# create an instance of PaypalDetails from a dict
paypal_details_from_dict = PaypalDetails.from_dict(paypal_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


