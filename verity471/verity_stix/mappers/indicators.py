import logging
import pycti
from stix2.exceptions import InvalidValueError
from stix2 import Indicator, Bundle, Relationship, KillChainPhase


from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper, MappingConfig
from ..constants import MARKING
from ..sco import map_domain, map_url, map_ipv4, map_file, map_email_address
from ..sdo import map_malware


log = logging.getLogger(__name__)


@StixMapper.register(
    "indicators", lambda x: "indicators" in x and isinstance(x["indicators"], list)
)
@StixMapper.register(
    "indicator",
    lambda x: isinstance(x, dict)
    and (x.get("id") or "").startswith("malware-indicator--"),
)
class IndicatorsMapper(BaseMapper):

    mapping_configs = {
        "url": MappingConfig(
            entities_mapper=map_url,
            kwargs_extractor=lambda i: {"value": i["data"]["url"]},
            name_extractor=lambda i: i["data"]["url"],
            opencti_type="Url"
        ),
        "ipv4": MappingConfig(
            entities_mapper=map_ipv4,
            kwargs_extractor=lambda i: {
                "value": i["data"]["ipv4"]["ip_address"]
            },
            name_extractor=lambda i: i["data"]["ipv4"]["ip_address"],
            opencti_type="IPv4-Addr"
        ),
        "file": MappingConfig(
            entities_mapper=map_file,
            kwargs_extractor=lambda i: {
                "md5": i["data"]["file"]["md5"],
                "sha1": i["data"]["file"]["sha1"],
                "sha256": i["data"]["file"]["sha256"],
            },
            name_extractor=lambda i: i["data"]["file"]["sha256"],
            opencti_type="StixFile"
        ),
        "domain": MappingConfig(
            entities_mapper=map_domain,
            kwargs_extractor=lambda i: {
                "value": i["data"]["domain"]
            },
            name_extractor=lambda i: i["data"]["domain"],
            opencti_type="Domain-Name"
        ),
        "email": MappingConfig(
            entities_mapper=map_email_address,
            kwargs_extractor=lambda i: {
                "value": i["data"]["email"]
            },
            name_extractor=lambda i: i["data"]["email"],
            opencti_type="Email-Addr"
        ),
       "yara": MappingConfig(
            entities_mapper=lambda value=None: None,
            kwargs_extractor=lambda i: {"value": None},
            name_extractor=lambda i: None,
            opencti_type=None
        )
    }

    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        items = (
            source.get("indicators") or []
            if "count" in source
            else [source]
        )
        for item in items:
            mapping_config = self.mapping_configs.get(item["type"])
            if not mapping_config:
                continue
            malware_family_name = item["threat"]["data"]["malware_family"]["name"]
            malware = map_malware(malware_family_name)
            labels = [malware_family_name]
            try:
                labels.extend(self.get_girs_labels(item["classification"]["girs"]))
            except KeyError:
                pass
            custom_properties = {"x_opencti_main_observable_type": mapping_config.opencti_type}
            try:
                pattern = item["pattern"]
            except KeyError:
                log.warning("Can't get pattern for indicator %s", item.get("id"))
                continue
            if self.settings.ioc_opencti_score:
                custom_properties["x_opencti_score"] = self.settings.ioc_opencti_score
            
            indicator_kwargs = {
                "pattern_type": item["pattern_type"],
                "id": pycti.Indicator.generate_id(pattern),
                "pattern": pattern,
                "pattern_version": item["pattern_version"],
                "indicator_types": ["malicious-activity"],
                "valid_from": item["activity"]["first_seen_ts"],
                "valid_until": item.get("expiration_ts"),
                "created_by_ref": author_identity,
                "object_marking_refs": [MARKING],
                "name": mapping_config.name_extractor(item),
                "description": item.get("description"),
                "labels": labels,
                "confidence": item["confidence"],
                "custom_properties": custom_properties
            }
            if kill_chain_phases := item.get("kill_chain_phases"):
                indicator_kwargs["kill_chain_phases"] = [
                    KillChainPhase(**{**kw, 'phase_name': kw['phase_name'].replace('_', '-')})
                    for kw in kill_chain_phases
                ]
            try:
                indicator = Indicator(**indicator_kwargs)
            except InvalidValueError as e:
                log.warning("Can't map indicator `%s`: %s", item.get("id"), e)
                continue
            r1 = Relationship(
                id=pycti.StixCoreRelationship.generate_id(
                    relationship_type="indicates",
                    source_ref=indicator.id,
                    target_ref=malware.id),
                source_ref=indicator,
                relationship_type="indicates",
                target_ref=malware,
                created_by_ref=author_identity,
                object_marking_refs=[MARKING]
            )

            for stix_object in [
                malware,
                indicator,
                r1,
                author_identity,
                MARKING,
            ]:
                container.add(stix_object)

            try:
                observable = mapping_config.entities_mapper(**mapping_config.kwargs_extractor(item))
            except InvalidValueError as e:
                log.warning("Can't map observable `%s`: %s", item.get('id'), e)
            else:
                if observable:
                    r2 = Relationship(
                        id=pycti.StixCoreRelationship.generate_id(
                            relationship_type="based-on",
                            source_ref=indicator.id,
                            target_ref=observable.id),
                        source_ref=indicator,
                        relationship_type="based-on",
                        target_ref=observable,
                        created_by_ref=author_identity,
                        object_marking_refs=[MARKING]
                    )
                    container.add(observable)
                    container.add(r2)

        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle
