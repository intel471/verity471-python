import yaml
import pycti
from stix2 import Bundle, Vulnerability, ExternalReference, Software, Relationship

from .common import BaseMapper, StixMapper
from .. import author_identity, StixObjects
from ..constants import MARKING, PLATFORM_VERITY471, X_OPENCTI_CREATED_BY, X_OPENCTI_LABELS


@StixMapper.register(
    "vuln_reports",
    lambda x: isinstance(x.get("reports"), list)
    and (x["reports"][0].get("id") or "").startswith("vulnerability--")
    and "fintel_report_count" not in x,
)
@StixMapper.register(
    "vuln_report",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("vulnerability--"),
)
class CveMapper(BaseMapper):
    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        items = (
            source.get("reports") or []
            if "count" in source
            else [source]
        )
        for item in items:
            id_ = item["id"]
            name = item["name"]
            summary = item["body"]
            underground_activity_summary = item["underground_activity_summary_html"]
            counter_measures = item["counter_measures_html"]
            extras = yaml.dump(
                {
                    k: v
                    for k, v in item.items()
                    if k
                    in (
                        "patch_status",
                        "interest_level",
                        "activity_location",
                        "exploit_status",
                    )
                }
            )
            description = f"{summary}\n\n{underground_activity_summary}\n\n{counter_measures}\n\n### Properties\n\n```yaml\n{extras}```"

            external_references = []
            for key, key_name in (
                ("links", None),
                ("sources", None),
                ("poc_links", "PoC"),
                ("patch_links", "Patch"),
                ("counter_measure_links", "Counter measure")
            ):
                links = self.map_links(item.get(key))
                for link in links:
                    source_name = f"[{key_name}] {link.name}" if key_name else link.name
                    external_references.append(ExternalReference(source_name=source_name, url=link.url))

            custom_properties = {"x_intel471_com_uid": id_}
            cvss_item = next((i for i in item.get("cvss") if i.get('version') == '3.1'), None)
            cvss3_score = cvss_item.get('score') if cvss_item and cvss_item.get('score', 0) > 0 else None
            if cvss3_score:
                custom_properties["x_opencti_base_score"] = cvss3_score
            labels = self.get_girs_labels((item.get("classification") or {}).get("girs") or [])
            labels.append(PLATFORM_VERITY471)
            vulnerability = Vulnerability(
                id=pycti.Vulnerability.generate_id(name),
                name=name,
                description=description,
                created_by_ref=author_identity,
                external_references=external_references,
                object_marking_refs=[MARKING],
                custom_properties=custom_properties,
                labels=labels
            )
            software = Software(
                name=item["product_name"],
                vendor=item["vendor_name"],
                custom_properties={
                    X_OPENCTI_CREATED_BY: author_identity.id,
                    X_OPENCTI_LABELS: [PLATFORM_VERITY471]
                    })
            rel = Relationship(
                id=pycti.StixCoreRelationship.generate_id(
                    relationship_type="has",
                    source_ref=software.id,
                    target_ref=vulnerability.id),
                source_ref=software,
                relationship_type= "has",
                target_ref=vulnerability,
                object_marking_refs=[MARKING],
                labels=[PLATFORM_VERITY471],
                created_by_ref=author_identity)
            container.extend([vulnerability, software, rel, author_identity, MARKING])
        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle
