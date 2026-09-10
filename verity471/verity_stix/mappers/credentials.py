import logging

from stix2 import Bundle
from stix2.exceptions import InvalidValueError

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper, quote
from ..constants import MARKING
from ..sco import map_credential_account, map_email_address, map_domain
from ..sdo import map_malware, map_organization

log = logging.getLogger(__name__)


def _is_email(value) -> bool:
    return bool(value) and "@" in value


@StixMapper.register(
    "credential",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("cred--"),
)
@StixMapper.register(
    "credential_occurrence",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("cred-occurrence--"),
)
class CredentialMapper(BaseMapper):
    """Map a leaked credential (or credential occurrence) to a UserAccount graph.

    The password (when present) goes in the UserAccount ``credential`` field; an
    email login is also emitted as an EmailAddress with ``belongs_to_ref`` back
    to the account. Affected domains and the harvesting malware family are
    attached via ``related-to`` relationships.
    """

    def map(self, source: dict):
        container = StixObjects()
        data = source.get("data") or {}
        # A credential occurrence nests the credential under data.credential.
        cred = data.get("credential") if isinstance(data.get("credential"), dict) else data
        labels = self._gir_labels(source)

        type_labels = ["verity471:credential"]
        if credential_type := data.get("credential_type"):
            type_labels.append(f"verity471:credential_{credential_type}")

        login = cred.get("credential_login")
        password = (cred.get("password") or {}).get("password_plain")
        account = None
        if login or password:
            account = map_credential_account(
                login=login, password=password, extra_labels=labels + type_labels,
                description=self._describe(cred, data),
            )
            container.add(account)
            if _is_email(login):
                container.add(map_email_address(login, belongs_to_ref=account.id))

        for domain in filter(None, {cred.get("credential_domain"), cred.get("detection_domain"),
                                    cred.get("accessed_domain"), data.get("accessed_domain")}):
            observable = self._safe_domain(domain)
            if observable:
                container.add(observable)
                if account:
                    container.add(self.relate(account.id, observable.id, "related-to"))

        for family in self._malware_families(data.get("info_stealer")):
            malware = map_malware(family)
            container.add(malware)
            if account:
                container.add(self.relate(account.id, malware.id, "related-to"))

        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)

    def _gir_labels(self, source: dict) -> list:
        try:
            return self.get_girs_labels(source["classification"]["girs"])
        except (KeyError, TypeError):
            return []

    @staticmethod
    def _describe(cred: dict, data: dict) -> str:
        login = cred.get("credential_login") or "unknown account"
        parts = [f"Credential for {quote(login)}"]
        if domain := cred.get("credential_domain"):
            parts.append(f" on {quote(domain)}")
        # credential set name lives under data.credential_sets[] (cred) or data.credential_set (occurrence)
        cred_set = None
        if isinstance(data.get("credential_set"), dict):
            cred_set = data["credential_set"].get("name")
        elif cred.get("credential_sets"):
            cred_set = (cred["credential_sets"][0] or {}).get("name")
        if cred_set:
            parts.append(f", from credential set {quote(cred_set)}")
        description = "".join(parts) + "."
        # Password strength lives in the description, not x_opencti_score (see note):
        # x_opencti_score is OpenCTI's threat score, a different axis from password strength.
        strength = (cred.get("password") or {}).get("strength")
        if strength and strength != "not_provided":
            description += f" Password strength: {quote(strength)}."
        return description

    @staticmethod
    def _malware_families(info_stealer) -> list:
        if not isinstance(info_stealer, dict):
            return []
        family = info_stealer.get("malware_family")
        if isinstance(family, list):
            return [f for f in family if f]
        if isinstance(family, str) and family:
            return [family]
        return []

    @staticmethod
    def _safe_domain(value):
        try:
            return map_domain(value)
        except (InvalidValueError, ValueError):
            return None


@StixMapper.register(
    "credential_set",
    lambda x: isinstance(x, dict) and (x.get("id") or "").startswith("cred-set--"),
)
class CredentialSetMapper(BaseMapper):
    """Map a credential set's victim organizations.

    The breach-dataset metadata (name, record count, breach date) is carried by
    the wrapping Incident that the alerts orchestrator builds
    (``incident_type="data-breach"``); this mapper contributes the victim
    Identities that the Incident references.
    """

    def map(self, source: dict):
        container = StixObjects()
        data = source.get("data") or {}
        for victim in data.get("victims") or []:
            if not isinstance(victim, dict) or not victim.get("name"):
                continue
            url = None
            external = [link for link in self.map_links(victim.get("links")) if link.name.lower() == "external"]
            if external:
                url = external[0].url
            container.add(map_organization(victim["name"], url))
        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)
