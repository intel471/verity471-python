from stix2 import Malware, ThreatActor, Identity, Vulnerability, Infrastructure
import pycti
from pycti import Channel, CustomObjectChannel
from . import author_identity
from .constants import MARKING, PLATFORM_VERITY471, X_OPENCTI_ALIASES



def map_malware(value: str, *args, **kwargs) -> Malware:
    return Malware(
        id=pycti.Malware.generate_id(value),
        name=value,
        is_family=True,
        created_by_ref=author_identity,
        labels=[PLATFORM_VERITY471],
        object_marking_refs=[MARKING],  
    )

def map_threat_actor(value: str, description: str = None, *args, **kwargs) -> ThreatActor:
    return ThreatActor(
        id=pycti.ThreatActorIndividual.generate_id(value),
        name = value,
        description = description,
        resource_level="individual",
        created_by_ref=author_identity,
        labels=[PLATFORM_VERITY471],
        object_marking_refs=[MARKING],
)


def map_vulnerability(value: str, *args, **kwargs) -> Vulnerability:
    return Vulnerability(
        id=pycti.Vulnerability.generate_id(value),
        name=value,
        created_by_ref=author_identity,
        labels=[PLATFORM_VERITY471],
        object_marking_refs=[MARKING],
    )


def map_infrastructure(value: str, *args, **kwargs) -> Infrastructure:
    return Infrastructure(
        id=pycti.Infrastructure.generate_id(value),
        name=value,
        infrastructure_types=["hosting-malware"],
        created_by_ref=author_identity,
        labels=[PLATFORM_VERITY471],
        object_marking_refs=[MARKING],
    )


def map_organization(value: str, url=None, *args, **kwargs) -> Identity:
    return Identity(
        id=pycti.Identity.generate_id(value, identity_class="organization"),
        name = value,
        contact_information=url,
        identity_class="organization",
        created_by_ref=author_identity,
        labels=[PLATFORM_VERITY471],
        object_marking_refs=[MARKING],
)


def map_individual(value: str, aliases: list = None, description: str = None, *args, **kwargs) -> Identity:
    """Map an online handle (forum/chat author or recipient) to an individual Identity.

    Follows the OpenCTI community convention for underground handles: an
    ``identity_class="individual"`` Identity with the raw handle(s) preserved in
    the ``x_opencti_aliases`` custom property. Not a Persona observable.
    """
    kwargs_ = {
        "id": pycti.Identity.generate_id(value, identity_class="individual"),
        "name": value,
        "identity_class": "individual",
        "created_by_ref": author_identity,
        "labels": [PLATFORM_VERITY471],
        "object_marking_refs": [MARKING],
    }
    if description:
        kwargs_["description"] = description
    if aliases:
        kwargs_["custom_properties"] = {X_OPENCTI_ALIASES: aliases}
    return Identity(**kwargs_)


def map_channel(name: str, channel_type: str = None, external_references: list = None,
                aliases: list = None, description: str = None, *args, **kwargs) -> CustomObjectChannel:
    """Map a forum / chat room / data-leak site / marketplace to a Channel SDO.

    Name follows the community ``"[<type>] - <name>"`` convention; the source
    portal / site link goes into ``external_references``.
    """
    formatted_name = f"[{channel_type}] - {name}" if channel_type else name
    kwargs_ = {
        "id": Channel.generate_id(formatted_name),
        "name": formatted_name,
        "created_by_ref": author_identity,
        "labels": [PLATFORM_VERITY471],
        "object_marking_refs": [MARKING],
    }
    if channel_type:
        kwargs_["channel_types"] = [channel_type]
    if aliases:
        kwargs_["aliases"] = aliases
    if description:
        kwargs_["description"] = description
    if external_references:
        kwargs_["external_references"] = external_references
    return CustomObjectChannel(**kwargs_)
