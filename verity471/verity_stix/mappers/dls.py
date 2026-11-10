import logging

from stix2 import Bundle
from stix2.exceptions import InvalidValueError

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper, quote
from .sources import PORTAL_BASE, portal_href, external_href, map_attachment
from ..constants import MARKING
from ..sco import map_file, map_media_content, map_url
from ..sdo import map_channel
from verity471.helpers.alerts import dls_thread_portal_url

log = logging.getLogger(__name__)


def _site_channel(website: dict, external_references=None):
    """Channel for a data-leak site. Falls back to the stable website id (never a
    shared "Unknown" label) so title-less sites don't false-merge into one node."""
    site_name = website.get("title") or website.get("id")
    if not site_name:
        return None, None
    return map_channel(
        site_name,
        channel_type="data-leak-site",
        external_references=external_references,
    ), site_name


def _post_description(title, site_name) -> str:
    title_part = f" {quote(title)}" if title else ""
    return f"Data leak site post{title_part} on {quote(site_name or 'unknown site')}."


@StixMapper.register(
    "data_leak_site_file_listing",
    lambda x: isinstance(x, dict) and "chunk_number" in x and isinstance(x.get("post"), dict),
)
class DataLeakSiteFileListingMapper(BaseMapper):
    """Map a data-leak-site file listing (``/file-listings/{id}/details``, the
    target of data-leak-site alerts) to the same graph as its post: a Channel
    (the site) + Media-Content (the post), plus the listed file and the site's
    external URL.

    The Media-Content id is the post's thread portal URL, the same one
    :class:`DataLeakSiteMapper` uses, so a listing and its post merge into one
    node. The listing carries neither the post body nor its creation time.
    """

    def map(self, source: dict):
        container = StixObjects()
        post = source.get("post") or {}
        thread = source.get("thread") or {}
        website = source.get("website") or {}

        channel, site_name = _site_channel(website)
        if channel:
            container.add(channel)

        if website.get("id") and thread.get("id"):
            url = dls_thread_portal_url(website["id"], thread["id"])
        else:
            url = f"{PORTAL_BASE}/sources/data-leak-sites/posts/{post.get('id')}"
        title = post.get("title") or thread.get("name")
        media = map_media_content(
            url,
            title=title,
            media_category="data leak site post",
            description=_post_description(title, site_name),
            extra_labels=["verity471:data_leak_site_post"],
        )
        container.add(media)
        if channel:
            container.add(self.relate(channel.id, media.id, "publishes"))

        if file_name := (source.get("file") or {}).get("name"):
            file_obj = map_file(name=file_name)
            container.add(file_obj)
            container.add(self.relate(media.id, file_obj.id, "related-to"))

        if source_href := external_href(source.get("links")):
            try:
                src_obj = map_url(source_href)
            except (InvalidValueError, ValueError):
                src_obj = None
            if src_obj:
                container.add(src_obj)
                container.add(self.relate(src_obj.id, media.id, "related-to", description="source"))

        container.add(author_identity)
        container.add(MARKING)
        return Bundle(*container.get(), allow_custom=True)


@StixMapper.register(
    "data_leak_site_post",
    lambda x: (isinstance(x, dict) and isinstance(x.get("post"), dict) and "website" in x
               and "chunk_number" not in x),
)
class DataLeakSiteMapper(BaseMapper):
    """Map a data-leak-site post to a Channel (the site) + Media-Content (the post).

    Alerts on data leak sites target file listings, which
    :class:`DataLeakSiteFileListingMapper` maps onto the same nodes.
    """

    def map(self, source: dict):
        container = StixObjects()
        post = source.get("post") or {}
        website = source.get("website") or {}

        channel, site_name = _site_channel(
            website, self.external_references(post.get("links")) or None)
        if channel:
            container.add(channel)

        url = portal_href(post.get("links")) or f"{PORTAL_BASE}/sources/data-leak-sites/posts/{post.get('id')}"
        title = post.get("title")
        description = _post_description(title, site_name)
        media = map_media_content(
            url,
            content=post.get("message"),
            title=title,
            media_category="data leak site post",
            publication_date=post.get("creation_ts"),
            description=description,
            extra_labels=["verity471:data_leak_site_post"],
        )
        container.add(media)
        if channel:
            container.add(self.relate(channel.id, media.id, "publishes"))

        # source (external) URL of the post -> first-class URL observable
        if source_href := external_href(post.get("links"), website.get("links")):
            try:
                src_obj = map_url(source_href)
            except (InvalidValueError, ValueError):
                src_obj = None
            if src_obj:
                container.add(src_obj)
                container.add(self.relate(src_obj.id, media.id, "related-to", description="source"))

        download_url = (post.get("file_listing") or {}).get("download_url")
        if download_url:
            try:
                url_obj = map_url(download_url)
            except (InvalidValueError, ValueError):
                url_obj = None
            if url_obj:
                container.add(url_obj)
                container.add(self.relate(media.id, url_obj.id, "related-to"))

        for attachment in post.get("attachments") or []:
            file_obj = map_attachment(attachment)
            if file_obj:
                container.add(file_obj)
                container.add(self.relate(media.id, file_obj.id, "related-to"))

        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)
