import logging

from stix2 import Bundle

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper
from .entities import EntitiesMapper
from .sources import PORTAL_BASE, strip_html, portal_href, map_attachment
from ..constants import MARKING
from ..sco import map_media_content
from ..sdo import map_channel, map_individual

log = logging.getLogger(__name__)


@StixMapper.register(
    "forum_post",
    lambda x: isinstance(x, dict)
    and isinstance(x.get("post"), dict)
    and (x["post"].get("id") or "").startswith("post--")
    and "website" not in x
    and any(k in x for k in ("forum", "thread", "sub_forum")),
)
@StixMapper.register(
    "forum_private_message",
    lambda x: isinstance(x, dict) and isinstance(x.get("private_message"), dict),
)
@StixMapper.register(
    "chat_message",
    lambda x: isinstance(x, dict)
    and isinstance(x.get("message"), dict)
    and any(k in x for k in ("chat_room", "server")),
)
class PostsMapper(BaseMapper):
    """Map forum posts, forum private messages and chat/messaging-service messages.

    The post body becomes a Media-Content, published into a Channel hierarchy -
    for a forum post: forum -> sub-forum -> thread; for a chat message: server ->
    room. Levels are linked ``inner --related-to--> outer`` and the innermost
    channel ``publishes`` the Media-Content, so posts interconnect at every level
    (same thread, same sub-forum, same forum all share the corresponding
    Channel). Author/recipient handles become individual identities and
    attachments become files.
    """

    def __init__(self, settings):
        super().__init__(settings)
        self.entities_mapper = EntitiesMapper()

    def _channel_chain(self, container: StixObjects, specs: list, media_id: str):
        """Create a Channel per spec (outermost first), link inner --related-to-->
        outer, and have the innermost --publishes--> media_id.

        Each spec's ``name`` is the channel's dedup key. Callers key outer
        containers (forum / chat server) by title and inner venues (thread /
        chat room) by their stable Verity id - because thread topics and chat
        room names collide across distinct venues, whereas ids never do. The
        readable topic / room name is passed as ``description``. Specs with no
        ``name`` are skipped (no bogus shared node).
        """
        channels = []
        for spec in specs:
            name = spec.get("name")
            if not name:
                continue
            channel = map_channel(
                name,
                channel_type=spec.get("channel_type"),
                external_references=self.external_references(spec.get("links")) or None,
                description=spec.get("description"),
            )
            container.add(channel)
            channels.append(channel)
        for outer, inner in zip(channels, channels[1:]):
            container.add(self.relate(inner.id, outer.id, "related-to"))
        if channels:
            container.add(self.relate(channels[-1].id, media_id, "publishes"))
        return channels

    def map(self, source: dict):
        container = StixObjects()
        if isinstance(source.get("private_message"), dict):
            self._map_private_message(source, container)
        elif isinstance(source.get("message"), dict):
            self._map_chat_message(source, container)
        else:
            self._map_forum_post(source, container)
        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)

    # -- forum post ---------------------------------------------------------

    def _map_forum_post(self, source: dict, container: StixObjects):
        post = source.get("post") or {}
        forum = source.get("forum") or {}
        sub_forum = source.get("sub_forum") or {}
        thread = source.get("thread") or {}

        thread_portal = portal_href(thread.get("links"))
        url = f"{thread_portal}?postId={post['id']}" if thread_portal else \
            f"{PORTAL_BASE}/sources/forums/posts/{post.get('id')}"
        media = map_media_content(
            url,
            content=post.get("message") or strip_html(post.get("html")),
            title=thread.get("topic") or thread.get("topic_original"),
            media_category="forum post",
            publication_date=post.get("creation_ts"),
        )
        container.add(media)

        thread_title = thread.get("topic") or thread.get("topic_original")
        self._channel_chain(container, [
            {"name": forum.get("title") or forum.get("id"),
             "channel_type": "forum", "links": forum.get("links")},
            {"name": sub_forum.get("id") or sub_forum.get("title"),
             "channel_type": "forum-subforum", "links": sub_forum.get("links"),
             "description": sub_forum.get("title") if sub_forum.get("id") else None},
            {"name": thread.get("id") or thread_title,
             "channel_type": "forum-thread", "links": thread.get("links"),
             "description": thread_title if thread.get("id") else None},
        ], media.id)

        self._add_actor(container, post.get("author"), media.id, role="author")
        self._add_entities(container, post.get("entities"), media.id)
        self._add_attachments(container, post.get("attachments"), media.id)

    # -- forum private message ---------------------------------------------

    def _map_private_message(self, source: dict, container: StixObjects):
        pm = source.get("private_message") or {}
        forum = source.get("forum") or {}

        url = f"{PORTAL_BASE}/sources/forums/private-messages/{pm.get('id')}"
        media = map_media_content(
            url,
            content=pm.get("message"),
            title=pm.get("subject"),
            media_category="forum private message",
            publication_date=pm.get("creation_ts"),
        )
        container.add(media)

        self._channel_chain(container, [
            {"name": forum.get("title") or forum.get("id"),
             "channel_type": "forum", "links": forum.get("links")},
        ], media.id)

        self._add_actor(container, source.get("author"), media.id, role="sender")
        self._add_actor(container, source.get("recipient"), media.id, role="recipient")

    # -- chat / messaging-service message ----------------------------------

    def _map_chat_message(self, source: dict, container: StixObjects):
        message = source.get("message") or {}
        room = source.get("chat_room") or {}
        server = source.get("server") or {}
        server_type = server.get("type") or "chat"

        msg_portal = portal_href(message.get("links"))
        url = f"{msg_portal}?messageId={message['id']}" if msg_portal else \
            f"{PORTAL_BASE}/sources/messaging-services/messages/{message.get('id')}"
        media = map_media_content(
            url,
            content=message.get("text") or strip_html(message.get("html")),
            media_category="instant message",
            publication_date=message.get("creation_ts"),
        )
        container.add(media)

        self._channel_chain(container, [
            {"name": server.get("name") or server.get("id"),
             "channel_type": server_type, "links": server.get("links")},
            {"name": room.get("id") or room.get("name"),
             "channel_type": server_type, "links": room.get("links"),
             "description": room.get("name") if room.get("id") else None},
        ], media.id)

        self._add_actor(container, message.get("author"), media.id, role="author")
        self._add_attachments(container, message.get("attachments"), media.id)

    # -- shared -------------------------------------------------------------

    def _add_actor(self, container: StixObjects, actor: dict, media_id: str, role: str = None):
        """Map a handle (author / sender / recipient) to an individual Identity and
        link it to the post. ``role`` annotates the relationship so sender and
        recipient are distinguishable (both edges are otherwise ``related-to``)."""
        if not isinstance(actor, dict):
            return
        name = actor.get("user_name")
        if not name:
            return
        individual = map_individual(name, aliases=actor.get("historical_usernames") or None)
        container.add(individual)
        container.add(self.relate(individual.id, media_id, "related-to", description=role))

    def _add_entities(self, container: StixObjects, entities: list, media_id: str):
        for entity_source in entities or []:
            if not isinstance(entity_source, dict):
                continue
            observable = self.entities_mapper.map(**entity_source)
            if observable:
                container.add(observable)
                container.add(self.relate(observable.id, media_id, "related-to"))

    def _add_attachments(self, container: StixObjects, attachments: list, media_id: str):
        for attachment in attachments or []:
            file_obj = map_attachment(attachment)
            if file_obj:
                container.add(file_obj)
                container.add(self.relate(file_obj.id, media_id, "related-to"))
