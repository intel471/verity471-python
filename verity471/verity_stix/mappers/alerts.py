import logging

import pycti
from stix2 import Bundle, ExternalReference, Incident

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper
from ..constants import INTEL_471, MARKING, PLATFORM_VERITY471, SOURCE_VERITY
from ..exceptions import EmptyBundle, StixMapperNotFound

from verity471.helpers.alerts import fetch_alert_targets
from verity471.models.streaming_alerts_response import StreamingAlertsResponse
from verity471.models.get_cred_response import GetCredResponse
from verity471.models.get_cred_occurrence_response import GetCredOccurrenceResponse
from verity471.models.get_cred_set_response import GetCredSetResponse

log = logging.getLogger(__name__)

# Target types whose alert Incident is a data breach rather than a generic alert.
_DATA_BREACH_TARGETS = (GetCredResponse, GetCredOccurrenceResponse, GetCredSetResponse)

# Object types that are never linked to the alert Incident as content.
_NON_CONTENT_TYPES = ("marking-definition", "relationship")


@StixMapper.register(
    "alerts",
    lambda x: isinstance(x, dict) and isinstance(x.get("alerts"), list),
)
class AlertsMapper(BaseMapper):
    """Map a page of Verity watcher alerts.

    Each alert's target is resolved (via ``fetch_alert_targets``) and mapped
    through the registry to its content graph. By default each unique target is
    wrapped in an Incident (``incident_type`` ``"alert"``, or ``"data-breach"``
    for credential targets) carrying the watcher labels and portal reference,
    linked ``related-to`` its content. When
    ``STIXMapperSettings.alerts_create_incident`` is False, no Incident is
    created and the watcher context is attached to the content objects instead.

    Alerts firing multiple watchers on the same target are collapsed into one
    Incident with the union of watcher labels.
    """

    def map(self, source: dict):
        api_client = self.settings.api_client
        if api_client is None:
            raise StixMapperNotFound(
                "Alerts mapping requires STIXMapperSettings.api_client to resolve targets."
            )
        response = StreamingAlertsResponse.from_dict(source)
        targets = fetch_alert_targets(response, api_client, skip_missing_targets=True)
        if not targets:
            return None

        groups: dict = {}
        order: list = []
        for alert_target in targets:
            key = alert_target.alert.source_id or id(alert_target)
            if key not in groups:
                groups[key] = []
                order.append(key)
            groups[key].append(alert_target)

        container = StixObjects()
        for key in order:
            self._map_group(container, groups[key])
        if container:
            return Bundle(*container.get(), allow_custom=True)

    def _map_group(self, container: StixObjects, alert_targets: list):
        primary = alert_targets[0]
        content_objects = self._map_target(primary.target)

        watcher_labels = set()
        for alert_target in alert_targets:
            if alert_target.watcher and getattr(alert_target.watcher, "name", None):
                watcher_labels.add(f"watcher:{alert_target.watcher.name}")
            if alert_target.watcher_group and getattr(alert_target.watcher_group, "name", None):
                watcher_labels.add(f"watcher_group:{alert_target.watcher_group.name}")
        watcher_labels = sorted(watcher_labels)
        external_references = self._external_references(primary.alert)

        primary_objects = [
            o for o in content_objects
            if o.type not in _NON_CONTENT_TYPES and o.id != author_identity.id
        ]
        # Surface the target's GIR labels on the alert Incident too (they otherwise
        # live only on the nested content objects, e.g. the Malware).
        gir_labels = self._collect_gir_labels(content_objects)

        if self.settings.alerts_create_incident:
            incident = self._build_incident(
                primary, watcher_labels + gir_labels + [PLATFORM_VERITY471], external_references)
            container.add(incident)
            container.add(author_identity)
            container.add(MARKING)
            for obj in content_objects:
                container.add(obj)
            for obj in primary_objects:
                container.add(self.relate(incident.id, obj.id, "related-to"))
        else:
            primary_ids = {o.id for o in primary_objects}
            for obj in content_objects:
                if obj.id in primary_ids:
                    container.add(self._augment(obj, watcher_labels, external_references))
                else:
                    container.add(obj)

    def _map_target(self, target) -> list:
        if target is None:
            return []
        try:
            bundle = StixMapper(self.settings).map(target.to_dict())
        except (StixMapperNotFound, EmptyBundle):
            return []
        except Exception as exc:  # noqa: BLE001 - one bad target must not abort the batch
            log.warning("Failed to map alert target %s: %s", getattr(target, "id", None), exc)
            return []
        return list(bundle.objects)

    def _build_incident(self, primary, labels: list, external_references: list) -> Incident:
        summary = primary.target_summary or f"Verity alert {primary.alert.source_id}"
        # A datetime is passed straight through: stix2 accepts datetime objects
        # but rejects isoformat strings with a "+00:00" offset.
        created = primary.alert.creation_ts
        incident_type = "data-breach" if isinstance(primary.target, _DATA_BREACH_TARGETS) else "alert"
        kwargs = {
            "id": pycti.Incident.generate_id(summary, created),
            "name": summary,
            "description": summary,
            "incident_type": incident_type,
            "source": SOURCE_VERITY,
            "created_by_ref": author_identity,
            "labels": labels,
            "object_marking_refs": [MARKING],
            "allow_custom": True,
        }
        if created:
            kwargs["created"] = created
            kwargs["first_seen"] = created
            kwargs["last_seen"] = created
        if external_references:
            kwargs["external_references"] = external_references
        return Incident(**kwargs)

    @staticmethod
    def _collect_gir_labels(content_objects: list) -> list:
        """Gather GIR labels from content objects (SDO ``labels`` and SCO
        ``x_opencti_labels``) so they can also be shown on the alert Incident."""
        prefix = f"{INTEL_471} - GIR "
        girs = []
        for obj in content_objects:
            for label in (obj.get("labels") or []) + (obj.get("x_opencti_labels") or []):
                if label.startswith(prefix) and label not in girs:
                    girs.append(label)
        return girs

    @staticmethod
    def _external_references(alert) -> list:
        href = None
        links = getattr(alert, "links", None)
        if links:
            if links.verity_portal and links.verity_portal.href:
                href = links.verity_portal.href
            elif links.verity_api and links.verity_api.href:
                href = links.verity_api.href
        return [ExternalReference(source_name="Verity471 Portal", url=href)] if href else []

    @staticmethod
    def _augment(obj, labels: list, external_references: list):
        """Label-only mode: fold watcher context into an SDO's labels / refs."""
        if not labels and not external_references:
            return obj
        try:
            if "labels" in obj:  # SDOs carry a labels list; SCOs do not
                existing = list(obj.get("labels") or [])
                merged = existing + [label for label in labels if label not in existing]
                changes = {"labels": merged}
                if external_references:
                    changes["external_references"] = list(obj.get("external_references") or []) + external_references
                return obj.new_version(**changes)
        except Exception as exc:  # noqa: BLE001
            log.debug("Could not augment %s with watcher context: %s", getattr(obj, "id", None), exc)
        return obj
