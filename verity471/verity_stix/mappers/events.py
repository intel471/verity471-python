import logging

import pycti
from stix2 import Bundle, Infrastructure, KillChainPhase, Malware
from stix2.exceptions import InvalidValueError

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper
from ..constants import MARKING, PLATFORM_VERITY471
from ..sco import map_url, map_ipv4, map_file

log = logging.getLogger(__name__)


@StixMapper.register(
    "malware_event",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("malware-event--"),
)
class EventMapper(BaseMapper):
    """Map a malware (integrations) event to a Malware + C2 Infrastructure graph."""

    def map(self, source: dict):
        container = StixObjects()
        threat_data = (source.get("threat") or {}).get("data") or {}
        data = source.get("data") or {}

        malware = None
        family = threat_data.get("malware_family") or {}
        family_name = family.get("name") or (threat_data.get("malware") or {}).get("family")
        if family_name:
            malware = self._malware(family_name, source)
            container.add(malware)

        controller = data.get("controller") or {}
        c2_urls = [c["url"] for c in (data.get("controllers") or []) if isinstance(c, dict) and c.get("url")]
        if controller.get("url"):
            c2_urls.append(controller["url"])

        for c2_url in c2_urls:
            url_obj = self._safe(map_url, c2_url)
            if not url_obj:
                continue
            infrastructure = self._infrastructure(c2_url)
            container.add(infrastructure)
            container.add(url_obj)
            container.add(self.relate(infrastructure.id, url_obj.id, "consists-of"))
            if malware:
                container.add(self.relate(malware.id, infrastructure.id, "uses"))

        if ipv4 := (controller.get("ipv4") or {}).get("ip_address"):
            ip_obj = self._safe(map_ipv4, ipv4)
            if ip_obj:
                container.add(ip_obj)
                if malware:
                    container.add(self.relate(malware.id, ip_obj.id, "related-to"))

        for key in ("file", "config_file", "recipient_file"):
            file_src = data.get(key)
            if isinstance(file_src, dict) and any(file_src.get(h) for h in ("md5", "sha1", "sha256")):
                file_obj = map_file(md5=file_src.get("md5"), sha1=file_src.get("sha1"), sha256=file_src.get("sha256"))
                container.add(file_obj)
                if malware:
                    container.add(self.relate(malware.id, file_obj.id, "related-to"))

        if exfil := data.get("exfil_location"):
            url_obj = self._safe(map_url, exfil)
            if url_obj:
                container.add(url_obj)
                if malware:
                    container.add(self.relate(malware.id, url_obj.id, "related-to"))

        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)

    def _malware(self, name: str, source: dict) -> Malware:
        labels = [PLATFORM_VERITY471]
        if event_type := source.get("type"):
            labels.append(event_type)
        try:
            labels.extend(self.get_girs_labels(source["classification"]["girs"]))
        except (KeyError, TypeError):
            pass
        kwargs = {
            "id": pycti.Malware.generate_id(name),
            "name": name,
            "is_family": True,
            "created_by_ref": author_identity,
            "labels": labels,
            "object_marking_refs": [MARKING],
        }
        if kill_chain := self._kill_chain(source):
            kwargs["kill_chain_phases"] = kill_chain
        return Malware(**kwargs)

    @staticmethod
    def _kill_chain(source: dict) -> list:
        phases = []
        for phase in source.get("kill_chain_phases") or []:
            if isinstance(phase, dict) and phase.get("kill_chain_name") and phase.get("phase_name"):
                phases.append(KillChainPhase(
                    kill_chain_name=phase["kill_chain_name"],
                    phase_name=phase["phase_name"].replace("_", "-"),
                ))
        return phases

    @staticmethod
    def _infrastructure(name: str) -> Infrastructure:
        return Infrastructure(
            id=pycti.Infrastructure.generate_id(name),
            name=name,
            infrastructure_types=["command-and-control"],
            created_by_ref=author_identity,
            labels=[PLATFORM_VERITY471],
            object_marking_refs=[MARKING],
        )

    @staticmethod
    def _safe(mapper, value):
        try:
            return mapper(value)
        except (InvalidValueError, ValueError):
            return None
