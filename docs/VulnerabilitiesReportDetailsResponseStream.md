# VulnerabilitiesReportDetailsResponseStream

Minimal schema for a vulnerability report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report | 
**type** | **str** | Type of the report | 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**released_ts** | **str** | Timestamp when the report was published last time | 
**last_updated_ts** | **str** | Timestamp of last report update | 
**name** | **str** | Name of the vulnerability | 
**aliases** | **List[str]** | List of alternative names or identifiers for the vulnerability | [optional] 
**status** | [**VulnerabilityStatus**](VulnerabilityStatus.md) |  | 
**cve_type** | **str** | Type of CVE, for example: Buffer overflow, Privilege escalation, Memory corruption, etc | 
**risk_level** | [**RiskLevel**](RiskLevel.md) |  | 
**cvss** | [**List[Cvss]**](Cvss.md) | List of CVSS scores associated with the vulnerability | [optional] 
**poc** | [**Poc**](Poc.md) |  | [optional] 
**patch_status** | [**PatchStatus**](PatchStatus.md) |  | [optional] 
**body** | **str** | HTML formatted summary of the vulnerability | [optional] 
**underground_activity_summary_html** | **str** | HTML formatted summary of underground activity related to the vulnerability | [optional] 
**counter_measures_html** | **str** | HTML formatted summary of countermeasures for the vulnerability | [optional] 
**interest_level** | [**List[InterestLevel]**](InterestLevel.md) | List of levels of interest related to the vulnerability | [optional] 
**activity_location** | [**List[ActivityLocation]**](ActivityLocation.md) | List of locations where activity related to the vulnerability has been observed | [optional] 
**exploit_status** | [**List[ExploitStatus]**](ExploitStatus.md) | List of exploitation status details for the vulnerability | [optional] 
**sort_priority** | **int** | Priority used for sorting vulnerability reports | [optional] 
**vendor_name** | **str** | Name of the vendor of the affected software | 
**product_name** | **str** | Name of the product of the affected software | 
**sources** | [**List[CveSource]**](CveSource.md) | List of sources referenced in the report | [optional] 
**poc_links** | [**List[Link1]**](Link1.md) | List of titled URLs to Proofs of Concept related to the vulnerability | [optional] 
**patch_links** | [**List[Link1]**](Link1.md) | List of titled URLs to Patches related to the vulnerability | [optional] 
**counter_measure_links** | [**List[Link1]**](Link1.md) | List of titled URLs to Counter Measures related to the vulnerability | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**activity** | [**Activity**](Activity.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from verity471.models.vulnerabilities_report_details_response_stream import VulnerabilitiesReportDetailsResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerabilitiesReportDetailsResponseStream from a JSON string
vulnerabilities_report_details_response_stream_instance = VulnerabilitiesReportDetailsResponseStream.from_json(json)
# print the JSON string representation of the object
print(VulnerabilitiesReportDetailsResponseStream.to_json())

# convert the object into a dict
vulnerabilities_report_details_response_stream_dict = vulnerabilities_report_details_response_stream_instance.to_dict()
# create an instance of VulnerabilitiesReportDetailsResponseStream from a dict
vulnerabilities_report_details_response_stream_from_dict = VulnerabilitiesReportDetailsResponseStream.from_dict(vulnerabilities_report_details_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


