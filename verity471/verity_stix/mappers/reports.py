import datetime
import logging
import re
from enum import Enum
from typing import List, NamedTuple, Union, Callable

from pytz import UTC
from stix2 import Bundle, ExternalReference, Report, ThreatActor

from verity471.verity_stix.exceptions import VerityStixException
from .entities import EntitiesMapper

from .. import STIXMapperSettings, author_identity, StixObjects
from .common import BaseMapper, StixMapper
from ..constants import INTEL_471, MARKING, PLATFORM_VERITY471, REMOVE_HTML_REGEX
from ..sdo import map_organization


log = logging.getLogger(__name__)


class ReportType(Enum):
    INFOREP = "inforep"
    FINTEL = "fintel"
    BREACH_ALERT = "breach_alert"
    SPOTREP = "spotrep"
    MALWARE = "malware"
    GEOPOL = "geopol"


REPORT_SUBTYPE_ACTOR_PROFILE = "actor_profile"


class ReportSettings(NamedTuple):
    method_name: str
    portal_url_fragment: str
    # either JSON path to the field or a function that extracts value from provided source
    description_path_or_extractor: Union[str, Callable]
    entities_path_or_extractor: Union[str, Callable]
    victims_path: str
    links_path: str
    contents_paths: Union[List[str], None] = None



@StixMapper.register(
    "reports",
    lambda x: isinstance(x.get("reports"), list) and "fintel_report_count" not in x,
)
@StixMapper.register(
    "report",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("report--"),
)
class ReportMapper(BaseMapper):
    REPORTS_API_CLASS = "ReportsApi"
    reports_settings = {
        ReportType.FINTEL: ReportSettings(
            method_name="get_reports_fintel_id",
            portal_url_fragment="intelligence/fintelReportView",
            # There's no summary or anything similar. Try to extract contents of the first
            # paragraph <h2>...</h2><p>get-this</p>...
            description_path_or_extractor=lambda src: re.split(r'</?p>', re.sub(r'^.*?<p>', '', src.get("body") or ""))[0],
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources",
            contents_paths=["body"]
        ),
        ReportType.INFOREP: ReportSettings(
            method_name="get_reports_info_id",
            portal_url_fragment="intelligence/infoReportView",
            description_path_or_extractor="executive_summary",
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources",
            contents_paths=["executive_summary", "researcher_comments", "body_translated", "body", "source_characterization"]
        ),
        ReportType.BREACH_ALERT: ReportSettings(
            method_name="get_reports_breach_alert_id",
            portal_url_fragment="intelligence/breachAlertReportView",
            description_path_or_extractor="body",
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources"
        ),
        ReportType.SPOTREP: ReportSettings(
            method_name="get_reports_spot_id",
            portal_url_fragment="intelligence/spotReportView",
            description_path_or_extractor="body",
            entities_path_or_extractor="entities",
            victims_path="victims",
            links_path="sources"
        ),
        ReportType.MALWARE: ReportSettings(
            method_name="get_reports_malware_id",
            portal_url_fragment="intelligence/malwareReportView",
            description_path_or_extractor=lambda src: (re.search(r'<p>(.*?)</p>', src.get("body") or "", flags=re.S) or [None, ""])[1],
            entities_path_or_extractor=lambda src: [{"type": "MalwareFamily", "value": src.get("threat", {}).get("family")}],
            victims_path="",
            links_path="",
            contents_paths=["body"]
        ),
        # No entities in geopol. Map Locations (also for other types)
        ReportType.GEOPOL: ReportSettings(
            method_name="get_reports_geopol_id",
            portal_url_fragment="geopol/geopolReportView",
            description_path_or_extractor=lambda src: (re.search(r'<p>(.*?)</p>', src.get("body") or "", flags=re.S) or [None, ""])[1],
            entities_path_or_extractor="entities",
            victims_path="",
            links_path="",
            contents_paths=["body"]
        )
    }

    def __init__(self, settings: STIXMapperSettings):
        super().__init__(settings)
        self.entities_mapper = EntitiesMapper()
        self.cache = {}

    def map(self, source: dict) -> Union[Bundle, None]:
        """
        Main entrypoint for mapping responses from /report, /breachAlerts and /spotReports endpoints
        """
        is_report_by_id = False
        if "reports" in source and isinstance(source["reports"], list):
            items = source["reports"]
        else:
            is_report_by_id = True
            items = [source]

        stix_objects = StixObjects()
        for item in items:
            report_type = self._get_type(item)
            if not is_report_by_id and self._is_full_report_required(item):
                # Search reports APIs might return a shortened version of a report:
                # - Some fields might be absent -> then `is_truncated=true` flag is present
                # - If there are images in the report, they will be present as references in text,
                #   not inline base64 representation
                # Full version with inline images is available only when getting individual
                # report by ID with `include_inline_images=true` flag
                stix_objects.extend(self._fetch_and_map_report(report_type, item["id"]).get())
            else:
                stix_objects.extend(self._map_report(item).get())
        if stix_objects:
            bundle = Bundle(*stix_objects.get(), allow_custom=True)
            return bundle

    def _map_report(self, source: dict, object_refs: StixObjects = None) -> StixObjects:
        """
        Map report in the format that is used when getting a report by ID.
        In case of FINTEL and INFOREP (/reports endpoint) there will be extra (possible big) fields.
        Breach alert and Spot report look the same in their long and short representation
        """
        if not object_refs:
            object_refs = StixObjects()
        if entities := self._get_entities(source):
            object_refs.extend(entities.get())
        if victims := self._get_victims(source):
            object_refs.extend(victims.get())
        if not object_refs:
            object_refs.extend([author_identity])

        report_type: ReportType = self._get_type(source)
        stix_objects = StixObjects([MARKING, author_identity])
        stix_objects.extend(object_refs.get())
        name = source.get("title") or None
        time_published = source.get("creation_ts") or None
        labels = self._get_malware_families_names(stix_objects)
        if source.get("is_sensitive_source"):
            labels.append(f"{INTEL_471} - sensitive source")
        labels.extend(self._get_girs_labels(source))
        labels.append(PLATFORM_VERITY471)
        description = self._get_description(source) or name
        report_types = [report_type.value]
        if sub_type := source.get("sub_type"):
            report_types.append(sub_type)
        if report_type == ReportType.FINTEL and sub_type == REPORT_SUBTYPE_ACTOR_PROFILE:
            threat_actor = self.entities_mapper.map(**{
                "type": "Handle",
                "value": name,
                "description": description
            })
            stix_objects = StixObjects([i for i in stix_objects.get()
                                        if not (isinstance(i, ThreatActor) and i.name == name)])
            stix_objects.add(threat_actor)
            name = f"Actor Profile - {name}"

        report_kwargs = {
            "id": source["id"],
            "name": name,
            "description": description,
            "report_types": report_types,
            "confidence": self.map_confidence(source.get("assessment", {}).get("admiralty_code") or
                                              source.get("confidence", {}).get("level")),
            "published": time_published,
            "labels": labels,
            "external_references": self._get_external_references(source),
            "object_refs": object_refs.get(),
            "created_by_ref": author_identity,
            "object_marking_refs": [MARKING],
            "custom_properties": {
                "x_intel471_com_uid": source["id"],
                "content": self._get_opencti_content(source)
            }
        }
        if report_type == ReportType.INFOREP:
            if source_reliability := self._map_source_reliability(source.get("assessment", {}).get("admiralty_code")):
                report_kwargs["custom_properties"]["x_opencti_reliability"] = source_reliability
        report = Report(**report_kwargs)
        stix_objects.add(report)
        return stix_objects

    def _fetch_and_map_report(self, report_type: ReportType, report_id: str,
                              object_refs: StixObjects = None) -> StixObjects:
        report_settings = self.reports_settings.get(report_type)
        if report_id not in self.cache:
            api_instance = getattr(self.settings.client,
                                   self.REPORTS_API_CLASS)(self.settings.api_client)
            api_response = getattr(api_instance, report_settings.method_name)(id=report_id, include_inline_images=True)
            self.cache[report_id] = api_response.to_dict()
        return self._map_report(self.cache[report_id], object_refs)

    def _is_full_report_required(self, source: dict) -> bool:
        def _has_inline_images(source: dict):
            pattern = r"^https://api\.intel471\.cloud/intel-report.*/attachments/[a-fA-F0-9]{64}$"
            for item in (source.get('attachments') or []):
                mime_type = item.get("mime_type", "")
                url = item.get("url", "")
                is_image = mime_type.startswith("image/")
                is_valid_url = re.match(pattern, url)
                if is_image and is_valid_url:
                    return True
            return False

        return all([self.settings.report_full_content,
                    self.settings.client,
                    self.settings.api_client,
                    (bool(source.get('is_truncated')) or _has_inline_images(source))])

    def _extract_value(self, source: dict, path_or_extractor_name: str):
        report_type = self._get_type(source)
        report_settings = self.reports_settings.get(report_type)
        path_or_extractor = getattr(report_settings, path_or_extractor_name, "")
        if isinstance(path_or_extractor, Callable):
            try:
                return path_or_extractor(source)
            except Exception as e:
                log.warning("Can't extract value from report %s/%s using path/extractor `%s`. %s",
                            report_type, source["id"], path_or_extractor_name, e)
                return None
        return self._extract_value_by_path(source, path_or_extractor) or None

    @staticmethod
    def _extract_value_by_path(source: dict, path: str):
        for i in path.split("."):
            if not source:
                break
            source = source.get(i, {})
        return source or None

    def _get_external_references(self, source: dict) -> List[ExternalReference]:
        """
        {
            "type": "external",
            "title": "BlogSpot Webpaget: Kelvin Security Team",
            "links": {
            "external": {
                    "href": "http://kelvinsecteam.blogspot.com/"
                }
            },
            "index": 8,
            "last_updated_ts": "2018-08-02T00:00:00Z",
            "source_type": "External Link"
        },

        {
            "type": "internal",
            "title": "Actor Validolik (aka Validol-hack) announces his Android web-injects development service",
            "links": {
            "verity_api": {
                "href": "https://api.intel471.cloud/integrations/intel-report/v1/reports/fintel/report--1a88a0a7-660e-5698-a694-d36bf0c6d4dd"
            },
            "verity_portal": {
                "href": "https://verity.intel471.com/intelligence/infoReportView/report--97ab9a8e-1f33-5765-af67-f2acfe669b9f"
            }
            },
            "index": 1,
            "last_updated_ts": "2017-05-19T00:00:00Z",
            "source_type": "Info Report"
        }
        """
        references = [ExternalReference(source_name="Portal URL", url=self._get_portal_url(source))]
        if value := self._extract_value(source, "links_path"):
            for link_source in value:
                source_name = f"{link_source.get('source_type', link_source.get('type'))} - {link_source['title']}".strip()
                links = [i for i in self.map_links(link_source['links']) if i.type in ("external", "verity_portal")]
                if links:
                    external_ref = ExternalReference(url=links[0].href, source_name=source_name)
                    references.append(external_ref)
        return references

    def _get_entities(self, source: dict) -> StixObjects:
        value = self._extract_value(source, "entities_path_or_extractor")
        stix_objects = StixObjects()
        for entities_source in value or []:
            if entity := self.entities_mapper.map(**entities_source):
                stix_objects.add(entity)
        return stix_objects

    def _get_victims(self, source: dict) -> StixObjects:
        stix_objects = StixObjects()
        if value := self._extract_value(source, "victims_path"):
            if isinstance(value, dict):
                value = [value]
            for victim_src in value:
                uri = None
                if links_src := victim_src.get("links"):
                    external = [i for i in self.map_links(links_src) if i.type == "external"]
                    if external:
                        uri = external[0].href
                stix_objects.add(
                    map_organization(victim_src["name"], uri))
            return stix_objects

    @staticmethod
    def _format_published(epoch_millis: int):
        """
        Formatting datetime object for use as ID contributing property in a same way as it's done
        by OpenCTI to have the same ID here and in OpenCTI.
        """
        parsed = datetime.datetime.fromtimestamp(epoch_millis / 1000, UTC)
        return parsed.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    @staticmethod
    def _get_type(source: dict) -> ReportType:
        type_ = {
            "info_report": ReportType.INFOREP,
            "fintel": ReportType.FINTEL,
            "breach_alert": ReportType.BREACH_ALERT,
            "spot_report": ReportType.SPOTREP,
            "malware_report": ReportType.MALWARE,
            "geopol_report": ReportType.GEOPOL
        }.get(source.get("type"))
        if not type_:
            raise VerityStixException("Unkown report type")
        return type_

    def _get_portal_url(self, source: dict) -> str:
        report_type = self._get_type(source)
        report_id = source["id"]
        report_settings = self.reports_settings.get(report_type)
        return f"https://verity.intel471.com/{report_settings.portal_url_fragment}/{report_id}"

    def _get_girs_labels(self, source: dict) -> List[str]:
        girs_paths = self._extract_value_by_path(source, "classification.girs") or []
        return self.get_girs_labels(girs_paths)

    def _get_description(self, source: dict) -> Union[str, None]:
        value = self._extract_value(source, "description_path_or_extractor")
        if value and isinstance(value, str):
            return re.sub(REMOVE_HTML_REGEX, "", value)

    @staticmethod
    def _get_malware_families_names(entities: StixObjects) -> List[str]:
        return [i.name for i in entities.get() if i.type == "malware"]

    def _get_opencti_content(self, source: dict):
        content_bits = []
        contents_paths = self.reports_settings.get(self._get_type(source)).contents_paths or []
        for path in contents_paths:
            value = self._extract_value_by_path(source, path)
            if value and isinstance(value, str):
                if len(contents_paths) > 1:
                    heading = " ".join([i.capitalize() for i in re.findall(
                        r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', path.split(".")[-1])])
                    content_bits.append(f"<h1>{heading}</h1>")
                content_bits.append(value)
        return "\n".join(content_bits)

    def _map_source_reliability(self, admiralty_code: Union[str, None]):
        if admiralty_code and len(admiralty_code) > 0:
            reliability_code = admiralty_code[0].upper()
            return {
                "A": "A - Completely reliable",
                "B": "B - Usually reliable",
                "C": "C - Fairly reliable",
                "D": "D - Not usually reliable",
                "E": "E - Unreliable",
                "F": "F - Reliability cannot be judged"
            }.get(reliability_code)
        return None