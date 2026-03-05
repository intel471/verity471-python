# VulnerabilitiesReportDetailsResponse

Minimal schema for a vulnerability report response with keys, types, and descriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**Activity**](Activity.md) |  | 
**activity_location** | [**List[ActivityLocation]**](ActivityLocation.md) | List of locations where activity related to the vulnerability has been observed | [optional] 
**aliases** | **List[str]** | List of alternative names or identifiers for the vulnerability | [optional] 
**body** | **str** | HTML formatted summary of the vulnerability | [optional] 
**classification** | [**Classification**](Classification.md) |  | 
**counter_measure_links** | [**List[LinksSource]**](LinksSource.md) | List of titled URLs to Counter Measures related to the vulnerability | [optional] 
**counter_measures_html** | **str** | HTML formatted summary of countermeasures for the vulnerability | [optional] 
**creation_ts** | **str** | Timestamp when the report was published first time | 
**cve_type** | **str** | Type of CVE, for example: Buffer overflow, Privilege escalation, Memory corruption, etc | 
**cvss** | [**List[Cvss]**](Cvss.md) | List of CVSS scores associated with the vulnerability | [optional] 
**exploit_status** | [**List[ExploitStatus]**](ExploitStatus.md) | List of exploitation status details for the vulnerability | [optional] 
**id** | **str** | Unique identifier of the report | 
**interest_level** | [**List[InterestLevel]**](InterestLevel.md) | List of levels of interest related to the vulnerability | [optional] 
**last_updated_ts** | **str** | Timestamp of last report update | 
**links** | [**SourceLinks**](SourceLinks.md) |  | 
**name** | **str** | Name of the vulnerability | 
**patch_links** | [**List[LinksSource]**](LinksSource.md) | List of titled URLs to Patches related to the vulnerability | [optional] 
**patch_status** | [**PatchStatus**](PatchStatus.md) |  | [optional] 
**poc** | [**Poc**](Poc.md) |  | [optional] 
**poc_links** | [**List[LinksSource]**](LinksSource.md) | List of titled URLs to Proofs of Concept related to the vulnerability | [optional] 
**product_name** | **str** | Name of the product of the affected software | 
**released_ts** | **str** | Timestamp when the report was published last time | 
**risk_level** | [**RiskLevel**](RiskLevel.md) |  | 
**sort_priority** | **int** | Priority used for sorting vulnerability reports | [optional] 
**sources** | [**List[SourcesResponse]**](SourcesResponse.md) | List of sources referenced in the report | [optional] 
**status** | [**VulnerabilityStatus**](VulnerabilityStatus.md) |  | 
**type** | **str** | Type of the report | 
**underground_activity_summary_html** | **str** | HTML formatted summary of underground activity related to the vulnerability | [optional] 
**vendor_name** | **str** | Name of the vendor of the affected software | 

## Example

```python
from verity471.models.vulnerabilities_report_details_response import VulnerabilitiesReportDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerabilitiesReportDetailsResponse from a JSON string
vulnerabilities_report_details_response_instance = VulnerabilitiesReportDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(VulnerabilitiesReportDetailsResponse.to_json())

# convert the object into a dict
vulnerabilities_report_details_response_dict = vulnerabilities_report_details_response_instance.to_dict()
# create an instance of VulnerabilitiesReportDetailsResponse from a dict
vulnerabilities_report_details_response_from_dict = VulnerabilitiesReportDetailsResponse.from_dict(vulnerabilities_report_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


