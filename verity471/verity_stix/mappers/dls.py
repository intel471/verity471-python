import logging

from stix2 import Bundle
from stix2.exceptions import InvalidValueError

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper
from .sources import PORTAL_BASE, portal_href, map_attachment
from ..constants import MARKING
from ..sco import map_media_content, map_url
from ..sdo import map_channel

log = logging.getLogger(__name__)


@StixMapper.register(
    "data_leak_site_post",
    lambda x: isinstance(x, dict) and isinstance(x.get("post"), dict) and "website" in x,
)
class DataLeakSiteMapper(BaseMapper):
    """Map a data-leak-site post to a Channel (the site) + Media-Content (the post).

    NOTE: alerts currently resolve data-leak-site hits via the file-listings
    endpoint, which returns raw bytes rather than this structured post model, so
    this mapper is reachable today only when mapping the data-leak-sites posts
    stream directly. Wiring alerts to the structured endpoint requires an API /
    url_router change that must be verified against real alert payloads first.
    """

    def map(self, source: dict):
        container = StixObjects()
        post = source.get("post") or {}
        website = source.get("website") or {}

        # Fall back to the stable website id (never a shared "Unknown" label) so
        # title-less sites don't false-merge into one Channel node.
        site_name = website.get("title") or website.get("id")
        channel = map_channel(
            site_name,
            channel_type="data-leak-site",
            external_references=self.external_references(post.get("links")) or None,
        ) if site_name else None
        if channel:
            container.add(channel)

        url = portal_href(post.get("links")) or f"{PORTAL_BASE}/sources/data-leak-sites/posts/{post.get('id')}"
        media = map_media_content(
            url,
            content=post.get("message"),
            title=post.get("title"),
            media_category="data leak site post",
            publication_date=post.get("creation_ts"),
        )
        container.add(media)
        if channel:
            container.add(self.relate(channel.id, media.id, "publishes"))

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
