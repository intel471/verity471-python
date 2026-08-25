import re

from pycti import CustomObservableCryptocurrencyWallet, CustomObservableMediaContent
from stix2 import URL, IPv4Address, DomainName, File, AutonomousSystem, UserAccount, IPv6Address, EmailAddress, Software
from stix2.exceptions import InvalidValueError

from verity471.verity_stix import author_identity
from verity471.verity_stix.constants import MARKING, X_OPENCTI_CREATED_BY, X_OPENCTI_LABELS, PLATFORM_VERITY471


def map_url(value: str, *args, **kwargs) -> URL:
    return URL(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_ipv4(value: str, *args, **kwargs) -> IPv4Address:
    return IPv4Address(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_ipv6(value: str, *args, **kwargs) -> IPv6Address:
    return IPv6Address(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_domain(value: str, *args, **kwargs) -> DomainName:
    if value.startswith(("http://", "https://")):
        raise InvalidValueError(DomainName, "value", f"'{value}' is not valid domain name")
    return DomainName(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_email_address(value: str, *args, belongs_to_ref: str = None, display_name: str = None, **kwargs) -> EmailAddress:
    kwargs_ = {
        "value": value,
        "object_marking_refs": [MARKING],
        "custom_properties": {
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    }
    if belongs_to_ref:
        kwargs_["belongs_to_ref"] = belongs_to_ref
    if display_name:
        kwargs_["display_name"] = display_name
    return EmailAddress(**kwargs_)


def map_autonomous_system(value: str, *args, **kwargs) -> AutonomousSystem:
    return AutonomousSystem(
        number=int(re.sub(r"[A-Z]", "", value)),
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_crypto_wallet(value: str, *args, **kwargs) -> CustomObservableCryptocurrencyWallet:
    return CustomObservableCryptocurrencyWallet(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_user_account(value: str, type: str, *args, **kwargs) -> UserAccount:
    return UserAccount(
        account_type=type,
        user_id=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_file(md5: str = None, sha1: str = None, sha256: str = None, name: str = None) -> File:
    hashes = {}
    if md5:
        hashes["MD5"] = md5
    if sha1:
        hashes["SHA-1"] = sha1
    if sha256:
        hashes["SHA-256"] = sha256

    file_kwargs = {
        "object_marking_refs": [MARKING],
        "custom_properties": {
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    }
    if hashes:
        file_kwargs["hashes"] = hashes
    if name:
        file_kwargs["name"] = name

    return File(**file_kwargs)


def map_file_hash(value: str, type: str, *args, **kwargs) -> File:
    kwargs = {type.lower(): value}
    return map_file(**kwargs)


def map_filename(value: str, *args, **kwargs) -> File:
    return map_file(name=value)


def map_software(value: str, *args, **kwargs) -> Software:
    """Map an OS/platform name (e.g. "windows") to a ``software`` observable.

    Used as a malware's ``operating_system_refs`` target. The STIX id is
    deterministic on the name, so the same OS dedups to one node.
    """
    return Software(
        name=value,
        object_marking_refs=[MARKING],
        custom_properties={
            X_OPENCTI_CREATED_BY: author_identity.id,
            X_OPENCTI_LABELS: [PLATFORM_VERITY471]
            }
    )


def map_credential_account(login: str = None, password: str = None, display_name: str = None,
                           account_type: str = None, user_id: str = None,
                           extra_labels: list = None, description: str = None,
                           *args, **kwargs) -> UserAccount:
    """Map a leaked credential to a ``user-account`` observable.

    The password (when present) is stored in the STIX ``credential`` field.
    The STIX id is derived from ``account_type``/``user_id``/``account_login``
    only, so passing a password/description does not change the identity.
    """
    custom_properties = {
        X_OPENCTI_CREATED_BY: author_identity.id,
        X_OPENCTI_LABELS: [PLATFORM_VERITY471] + list(extra_labels or [])
    }
    if description:
        custom_properties["x_opencti_description"] = description
    kwargs_ = {
        "object_marking_refs": [MARKING],
        "custom_properties": custom_properties,
    }
    if account_type:
        kwargs_["account_type"] = account_type
    if login:
        kwargs_["account_login"] = login
    if uid := (user_id or login):
        kwargs_["user_id"] = uid
    if password:
        kwargs_["credential"] = password
    if display_name:
        kwargs_["display_name"] = display_name
    return UserAccount(**kwargs_)


def map_media_content(url: str, content: str = None, title: str = None, publication_date: str = None,
                      media_category: str = None, description: str = None, created_by_ref: str = None,
                      files: list = None, extra_labels: list = None,
                      *args, **kwargs) -> CustomObservableMediaContent:
    """Map a forum post / message / article body to a ``media-content`` observable.

    The STIX id is derived from ``url`` only, so ``url`` must be a stable,
    per-item value (a permalink where available, otherwise a deterministic
    synthetic URL built from the source object id).
    """
    custom_properties = {
        X_OPENCTI_CREATED_BY: created_by_ref or author_identity.id,
        X_OPENCTI_LABELS: [PLATFORM_VERITY471] + list(extra_labels or [])
    }
    if description:
        custom_properties["x_opencti_description"] = description
    if files:
        custom_properties["x_opencti_files"] = files
    kwargs_ = {
        "url": url,
        "object_marking_refs": [MARKING],
        "custom_properties": custom_properties
    }
    if content is not None:
        kwargs_["content"] = content
    if title:
        kwargs_["title"] = title
    if publication_date:
        kwargs_["publication_date"] = publication_date
    if media_category:
        kwargs_["media_category"] = media_category
    return CustomObservableMediaContent(**kwargs_)
