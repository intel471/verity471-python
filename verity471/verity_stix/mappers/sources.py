"""Shared helpers for mappers of source-derived content (forum posts, chat
messages, data-leak-site posts)."""
import logging
from typing import Optional

from stix2 import File

from ..constants import REMOVE_HTML_REGEX
from ..sco import map_file

log = logging.getLogger(__name__)

PORTAL_BASE = "https://verity.intel471.com"
CSAM_CLASSIFICATION = "csam"


def strip_html(text: Optional[str]) -> Optional[str]:
    if not text:
        return text
    return REMOVE_HTML_REGEX.sub("", text)


def portal_href(links: Optional[dict]) -> Optional[str]:
    """Extract the verity_portal href from a Verity ``links`` dict, if present."""
    if not isinstance(links, dict):
        return None
    portal = links.get("verity_portal")
    if isinstance(portal, dict):
        return portal.get("href")
    return None


def map_attachment(attachment: dict) -> Optional[File]:
    """Map a Verity AttachmentData dict to a File observable.

    Returns ``None`` for CSAM-classified attachments (never ingested) and for
    attachments carrying neither a hash nor a filename.
    """
    if not isinstance(attachment, dict):
        return None
    if (attachment.get("classification") or "").lower() == CSAM_CLASSIFICATION:
        return None
    file_hash = attachment.get("file_hash")
    md5 = sha1 = sha256 = None
    if file_hash:
        length = len(file_hash)
        if length == 32:
            md5 = file_hash
        elif length == 40:
            sha1 = file_hash
        elif length == 64:
            sha256 = file_hash
    name = attachment.get("file_name")
    if not (md5 or sha1 or sha256 or name):
        return None
    return map_file(md5=md5, sha1=sha1, sha256=sha256, name=name)
