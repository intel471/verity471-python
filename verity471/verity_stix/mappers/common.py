import abc
from dataclasses import dataclass
import datetime
import logging
import re
from abc import ABC
from collections.abc import Callable
from typing import Union, List, Optional, Any
from enum import Enum

from stix2 import Bundle

from .. import INTEL_471, STIXMapperSettings
from ..exceptions import EmptyBundle, StixMapperNotFound

log = logging.getLogger(__name__)


@dataclass
class MappingConfig:
    entities_mapper: Callable
    kwargs_extractor: Callable
    name_extractor: Callable
    opencti_type: str


@dataclass
class Link:
    name: str
    url: str


class StixMapper:
    def __init__(self, settings: STIXMapperSettings = None):
        self.settings = settings if settings else STIXMapperSettings()

    mappers = {}

    @classmethod
    def register(cls, name: str, condition) -> Callable:
        """
        Decorator used for registering mapper classes. Decorate any class derived from BaseMapper like this:

        @StixMapper.register("actors", lambda x: "actorTotalCount" in x)
        class ActorsMapper(BaseMapper):
            def map(self, source: dict) -> Bundle:
                ... my implementation ...

        @param name: unique name under which the mapper will be registered
        @param condition: callable that will be called against the source dict
                          to determine if given mapper should be used or not

        """

        def inner_wrapper(wrapped_class: Callable) -> Callable:
            if name in cls.mappers:
                log.info("Mapper for %s already exists. Will replace it", name)
            cls.mappers[name] = (condition, wrapped_class)
            return wrapped_class

        return inner_wrapper

    def map(self, source: dict, stix_version: str = "2.1") -> Bundle:
        log.info("Initializing converter. STIX version %s.", stix_version)
        for name, (condition, mapper_class) in self.mappers.items():
            if condition(source):
                log.info("Mapping Verity471 payload for %s.", name)
                mapper = mapper_class(self.settings)
                bundle = mapper.map(self._deenum(source))
                if bundle:
                    return bundle
                else:
                    raise EmptyBundle("STIX Mapper produced an empty bundle.")
        raise StixMapperNotFound(
            f"STIX Mapper for this payload is not available (keys: {', '.join(source.keys())})."
        )

    @classmethod
    def _deenum(cls, obj: Any) -> Any:
        # Enum -> unwrap to the underlying value
        if isinstance(obj, Enum):
            return obj.value

        # dict -> recurse on values
        if isinstance(obj, dict):
            return {k: cls._deenum(v) for k, v in obj.items()}

        # list/tuple/set -> recurse
        if isinstance(obj, list):
            return [cls._deenum(v) for v in obj]
        if isinstance(obj, tuple):
            return tuple(cls._deenum(v) for v in obj)
        if isinstance(obj, set):
            return {cls._deenum(v) for v in obj}

        # anything else -> keep
        return obj


class BaseMapper(ABC):
    def __init__(self, settings: STIXMapperSettings):
        self.now = datetime.datetime.now(datetime.timezone.utc)
        self.settings = settings

    @abc.abstractmethod
    def map(self, source: dict) -> Bundle:
        raise NotImplementedError

    def map_confidence(self, confidence: Union[str, None]):
        # There are two confidence scales used in Verity471: https://en.wikipedia.org/wiki/Admiralty_code and low/medium/high
        # This function handles both according to
        # [STIX confidence scales](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_1v6elyto0uqg)

        # If it's Admiralty_code we're interested in the second part only (Credibility), which is a number between 1 and 6.
        value = re.sub(r"^[A-F]([1-6])$", "\\1", confidence or "", flags=re.IGNORECASE)

        # If there's no match, we expect a word from low/medium/high scale.
        # If for any reason it's not the case either, we set confidence as not specified (`None`)
        return {
            "6": 0, "5": 10, "4": 30, "3": 50, "2": 70, "1": 90,
            "low": 15, "medium": 50, "high": 85
        }.get(value, 0)

    def map_links(self, links_sources: Union[dict, list[dict]]) -> list[Link]:
        links = []
        if not links_sources:
            return links

        # Normalize input to list
        if isinstance(links_sources, dict):
            links_sources = [links_sources]

        for entry in links_sources:
            # Simple style: {"verity_api": {"href": ...}}, {"verity_portal": {"href": ...}}
            if isinstance(entry, dict) and "links" not in entry:
                for key, value in entry.items():
                    if isinstance(value, dict) and "href" in value:
                        if key == "verity_portal":
                            links.append(Link(name="Verity471 Portal", url=value.get("href")))
                        elif key == "verity_api":
                            links.append(Link(name="Verity471 API", url=value.get("href")))
                        elif key == "external":
                            links.append(Link(name="External", url=value.get("href")))
            # Complex style: {"links": {"external": {"href": ...}, ...}, "title": "...", ...}
            elif isinstance(entry, dict) and "links" in entry:
                type_ = entry.get("type")
                title = entry.get("title")
                source_type = entry.get("source_type")
                links_dict = entry["links"]
                if type_ == "external" and "external" in links_dict:
                    ext_link = links_dict.get("external")
                    if isinstance(ext_link, dict) and "href" in ext_link:
                        ext_title = f"{source_type}/{title}" if source_type else title
                        links.append(Link(name=ext_title, url=ext_link.get("href")))
                elif type_ == "internal":
                    if "verity_portal" in links_dict:
                        vp_link = links_dict.get("verity_portal")
                        if isinstance(vp_link, dict) and "href" in vp_link:
                            parts = ["Verity471 Portal"]
                            if source_type:
                                parts.append(source_type)
                            vp_name = f"[{'/'.join(parts)}] {title}"
                            links.append(Link(name=vp_name, url=vp_link.get("href")))
                    if "verity_api" in links_dict:
                        va_link = links_dict.get("verity_api")
                        if isinstance(va_link, dict) and "href" in va_link:
                            parts = ["Verity471 API"]
                            if source_type:
                                parts.append(source_type)
                            va_name = f"[{'/'.join(parts)}] {title}"
                            links.append(Link(name=va_name, url=va_link.get("href")))
        return links

    def get_girs_labels(self, gir_paths: List[dict]):
        return [f'{INTEL_471} - GIR {i["path"]} - {i["name"]}' for i in gir_paths]
