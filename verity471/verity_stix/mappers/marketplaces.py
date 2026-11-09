"""STIX mappers for Verity471 marketplaces data.

Model (consistent with the forum / data-leak-site mappers):

* marketplace -> ``Channel`` (``channel_type="marketplace"``)
* vendor      -> individual ``Identity`` (the seller handle), ``related-to`` the Channel
* product     -> ``Media-Content`` (the listing), published by the Channel and
  ``related-to`` the vendor Identity. Bot listings add the infected machine's
  IPv4 and the stealer ``Malware``; proxy listings add the proxy IPv4 / domain.
* resource    -> ``DomainName`` / ``URL`` of the site whose data is in a bot's
  stealer log, ``related-to`` that bot listing.

Products and resources carry only their parents' ids (a product has a
``marketplace_id``, a resource the ``product_id`` of its bot). When
``STIXMapperSettings.api_client`` is set, those parents are fetched (once per
run, see ``STIXMapperSettings.lookup_cache``) so products link to the real
marketplace Channel and resources carry the bot context; without a client the
links that need a parent are skipped.

Personal data sold in listings (names, emails, phones, addresses, SSNs, card
numbers, dates of birth) is never mapped; only "available" flags are noted. Full
card numbers in seller-written titles/descriptions are truncated to first-6 +
last-4 (``helpers.redaction.mask_card_numbers``).
"""
import ipaddress
import logging
import re
from typing import Callable, Optional
from urllib.parse import urlparse

from stix2 import Bundle, ExternalReference
from stix2.exceptions import InvalidValueError

from verity471.helpers.redaction import mask_card_numbers

from .. import author_identity, StixObjects
from .common import StixMapper, BaseMapper, defang, quote, quote_plain
from .sources import PORTAL_BASE, strip_html
from ..constants import MARKING
from ..sco import map_media_content, map_ipv4, map_domain, map_url
from ..sdo import map_channel, map_individual, map_malware

log = logging.getLogger(__name__)

MARKETPLACE_PREFIX = "marketplace-website--"
PRODUCT_PREFIX = "marketplace-product--"
RESOURCE_PREFIX = "marketplace-resource--"
VENDOR_PREFIX = "marketplace-seller--"

CHANNEL_TYPE = "marketplace"

# A hostname-shaped value: labels separated by dots, no spaces or slashes.
_DOMAIN_RE = re.compile(r"^(?=.{4,253}$)([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z][a-z0-9-]{1,62}$", re.IGNORECASE)

# Card "available info" flags -> human label (the data itself is never mapped).
_CARD_AVAILABLE = (
    ("cvv_available", "CVV"),
    ("holder_name_available", "holder name"),
    ("address_available", "address"),
    ("city_available", "city"),
    ("zip_available", "ZIP"),
    ("phone_available", "phone"),
    ("email_available", "email"),
    ("date_of_birth_available", "date of birth"),
    ("social_security_number_available", "SSN"),
    ("mother_maiden_name_available", "mother's maiden name"),
    ("ip_available", "IP address"),
)


def product_url(product_id: str) -> str:
    """Stable portal permalink of a product; also the listing Media-Content's id seed,
    so a resource can reference its bot listing without fetching it."""
    return f"{PORTAL_BASE}/sources/marketplaces/products/{product_id}"


def marketplace_name(marketplace: dict) -> Optional[str]:
    """Display name used for the marketplace Channel. The API already falls back to
    the alias for ``name``; the id is the last resort so nameless markets don't merge."""
    return marketplace.get("name") or marketplace.get("alias") or marketplace.get("id")


def _id_page(key: str, prefix: str) -> Callable[[dict], bool]:
    """Condition for a stream page: ``{key: [...], "count": ...}`` whose items carry ``prefix`` ids."""
    def condition(x) -> bool:
        if not (isinstance(x, dict) and isinstance(x.get(key), list) and "count" in x):
            return False
        return all(isinstance(i, dict) and (i.get("id") or "").startswith(prefix) for i in x[key])
    return condition


def _id_item(prefix: str) -> Callable[[dict], bool]:
    return lambda x: isinstance(x, dict) and (x.get("id") or "").startswith(prefix)


def _number(value) -> str:
    return f"{value:g}" if isinstance(value, (int, float)) else str(value)


# Stealer values seen on bot listings are lowercase family names; display them the
# way the families are usually written. Malware ids are case-insensitive in pycti,
# so this only affects the name shown, not merging.
_STEALER_NAMES = {
    "lumma": "Lumma", "redline": "RedLine", "rhadamanthys": "Rhadamanthys", "vidar": "Vidar",
    "stealc": "StealC", "raccoon": "Raccoon", "risepro": "RisePro", "metastealer": "MetaStealer",
    "aurora": "Aurora", "mystic": "Mystic", "acreed": "Acreed", "amadey": "Amadey",
}
_NO_STEALER = {"", "unknown", "n/a", "na", "none", "other", "-", "null"}


def _stealer_name(value: Optional[str]) -> Optional[str]:
    """Display name of a bot's stealer family, or None for placeholders like 'unknown'."""
    value = (value or "").strip()
    if value.lower() in _NO_STEALER:
        return None
    return _STEALER_NAMES.get(value.lower(), value[:1].upper() + value[1:])


def _ipv4(value: Optional[str]) -> Optional[str]:
    """The IPv4 address in *value* (an ``ip:port`` form is accepted), or None when it
    is missing, masked (``1.2.*.*`` - stix2 would accept that) or otherwise invalid."""
    if not value:
        return None
    candidate = value.strip()
    if candidate.count(":") == 1:
        candidate = candidate.split(":", 1)[0]
    try:
        return str(ipaddress.IPv4Address(candidate))
    except (ipaddress.AddressValueError, ValueError):
        return None


def _safe(builder, value, **kwargs):
    """Build an observable, or None when the value is not valid for its type
    (masked IPs like ``1.2.3.*``, URLs passed as domains, ...)."""
    if not value:
        return None
    try:
        return builder(value, **kwargs)
    except (InvalidValueError, ValueError):
        return None


class MarketplaceLookups:
    """Fetch-and-cache access to parent marketplace objects.

    Results (including misses) are stored in a plain dict - normally
    ``STIXMapperSettings.lookup_cache`` - so they are shared across mappers of one
    run. Never raises: a missing client or a failed fetch yields ``None``.
    """

    def __init__(self, api_client, cache: dict):
        self._api_client = api_client
        self._cache = cache

    def marketplace(self, marketplace_id: Optional[str]) -> Optional[dict]:
        return self._get("marketplaces:marketplace", marketplace_id, "get_marketplaces_marketplace_id")

    def product(self, product_id: Optional[str]) -> Optional[dict]:
        return self._get("marketplaces:product", product_id, "get_products_product_id")

    def _get(self, kind: str, object_id: Optional[str], method: str) -> Optional[dict]:
        if not object_id or self._api_client is None:
            return None
        key = (kind, object_id)
        if key in self._cache:
            return self._cache[key]
        result = None
        try:
            from verity471.api.marketplaces_api import MarketplacesApi
            obj = getattr(MarketplacesApi(self._api_client), method)(object_id)
            result = StixMapper._deenum(obj.to_dict())
        except Exception as exc:  # noqa: BLE001 - enrichment must never break mapping
            log.warning("Could not fetch %s %s for STIX enrichment: %s", kind, object_id, exc)
        self._cache[key] = result
        return result


@StixMapper.register("marketplaces", _id_page("marketplaces", MARKETPLACE_PREFIX))
@StixMapper.register("marketplace_products", _id_page("products", PRODUCT_PREFIX))
@StixMapper.register("marketplace_resources", _id_page("resources", RESOURCE_PREFIX))
@StixMapper.register("marketplace_vendors", _id_page("vendors", VENDOR_PREFIX))
@StixMapper.register("marketplace", _id_item(MARKETPLACE_PREFIX))
@StixMapper.register("marketplace_product", _id_item(PRODUCT_PREFIX))
@StixMapper.register("marketplace_resource", _id_item(RESOURCE_PREFIX))
@StixMapper.register("marketplace_vendor", _id_item(VENDOR_PREFIX))
class MarketplacesMapper(BaseMapper):
    """Map marketplaces, vendors, products and resources (single items or stream
    pages). A stream page maps to one deduplicated Bundle; an item that fails to
    map is logged and skipped."""

    _PAGE_KEYS = ("marketplaces", "products", "resources", "vendors")

    def __init__(self, settings):
        super().__init__(settings)
        cache = settings.lookup_cache if settings.lookup_cache is not None else {}
        self.lookups = MarketplaceLookups(settings.api_client, cache)

    def map(self, source: dict):
        container = StixObjects()
        page_key = next((k for k in self._PAGE_KEYS if isinstance(source.get(k), list)), None)
        if page_key and "count" in source:
            for item in source[page_key]:
                try:
                    self._map_item(container, item)
                except Exception as exc:  # noqa: BLE001 - one bad item must not abort the page
                    log.warning("Failed to map marketplace item %s: %s", item.get("id"), exc)
        else:
            self._map_item(container, source)
        if container:
            container.add(author_identity)
            container.add(MARKING)
            return Bundle(*container.get(), allow_custom=True)

    def _map_item(self, container: StixObjects, item: dict):
        item_id = item.get("id") or ""
        if item_id.startswith(PRODUCT_PREFIX):
            self.map_product(container, item)
        elif item_id.startswith(RESOURCE_PREFIX):
            self.map_resource(container, item)
        elif item_id.startswith(VENDOR_PREFIX):
            self.map_vendor(container, item)
        elif item_id.startswith(MARKETPLACE_PREFIX):
            self.map_marketplace(container, item)

    # -- marketplace ---------------------------------------------------------

    def map_marketplace(self, container: StixObjects, marketplace: dict):
        name = marketplace_name(marketplace)
        if not name:
            return None
        alias = marketplace.get("alias")
        parts = [f"Marketplace {quote(name)}."]
        if marketplace.get("tier") is not None:
            parts.append(f"Tier {quote_plain(marketplace['tier'])}.")
        if marketplace.get("is_active") is False:
            parts.append("The marketplace is no longer active.")
        if text := strip_html(marketplace.get("description")):
            parts.append(defang(text))  # often carries .onion / mirror links
        refs = self.external_references(marketplace.get("links"))
        if link := marketplace.get("link"):
            refs.append(ExternalReference(source_name="Marketplace", url=link))
        channel = map_channel(
            name, channel_type=CHANNEL_TYPE,
            external_references=refs or None,
            aliases=[alias] if alias and alias != name else None,
            description=" ".join(parts),
        )
        container.add(channel)
        return channel

    def _marketplace_channel(self, container: StixObjects, marketplace_id: Optional[str],
                             fallback_name: Optional[str] = None):
        """The marketplace Channel: fully described when the marketplace can be
        fetched, a bare (same-id) Channel from ``fallback_name`` otherwise."""
        marketplace = self.lookups.marketplace(marketplace_id)
        if marketplace:
            return self.map_marketplace(container, marketplace)
        if fallback_name:
            channel = map_channel(fallback_name, channel_type=CHANNEL_TYPE)
            container.add(channel)
            return channel
        return None

    # -- vendor --------------------------------------------------------------

    def map_vendor(self, container: StixObjects, vendor: dict):
        name = vendor.get("name")
        if not name:
            return None
        channel = self._marketplace_channel(container, vendor.get("marketplace_id"),
                                            vendor.get("marketplace_name"))
        identity = map_individual(name, description=self._vendor_description(vendor))
        container.add(identity)
        if channel:
            container.add(self.relate(identity.id, channel.id, "related-to", description="vendor"))
        return identity

    @staticmethod
    def _vendor_description(vendor: dict) -> str:
        parts = [f"Marketplace vendor {quote(vendor['name'])}"]
        if vendor.get("marketplace_name"):
            parts.append(f" on {quote(vendor['marketplace_name'])}")
        description = "".join(parts) + "."
        rating = vendor.get("rating") or {}
        if rating.get("value") is not None:
            scale = f"/{_number(rating['max'])}" if rating.get("max") else ""
            description += f" Rating: {quote_plain(_number(rating['value']) + scale)}."
        rates = [(label, vendor.get(key)) for label, key in (
            ("last 10 days", "valid_rate_10_days"), ("last 30 days", "valid_rate_30_days"),
            ("overall", "valid_rate_overall"))]
        rates = [f"{quote_plain(_number(value) + '%')} {label}" for label, value in rates if value is not None]
        if rates:
            description += f" Valid goods: {', '.join(rates)}."
        return description

    # -- product -------------------------------------------------------------

    def map_product(self, container: StixObjects, product: dict):
        product_id = product.get("id")
        if not product_id:
            return None
        kind = product.get("kind")
        marketplace = self.lookups.marketplace(product.get("marketplace_id"))
        channel = self.map_marketplace(container, marketplace) if marketplace else None
        # Seller-written text: full card numbers are truncated (see helpers.redaction).
        title = mask_card_numbers(strip_html(product.get("title") or product.get("name"))) or product_id

        labels = ["verity471:marketplace_product"]
        if kind:
            labels.append(f"verity471:product_kind_{kind}")
        media = map_media_content(
            product_url(product_id),
            content=mask_card_numbers(product.get("description")),
            title=title,
            publication_date=(product.get("activity") or {}).get("first_seen_ts"),
            media_category="marketplace listing",
            description=self._product_description(product, title, marketplace),
            extra_labels=labels,
        )
        container.add(media)
        if channel:
            container.add(self.relate(channel.id, media.id, "publishes"))

        if vendor_name := product.get("vendor_name"):
            vendor = map_individual(vendor_name)
            container.add(vendor)
            container.add(self.relate(vendor.id, media.id, "related-to", description="vendor"))
            if channel:
                container.add(self.relate(vendor.id, channel.id, "related-to", description="vendor"))

        if kind == "bot":
            self._map_bot(container, product.get("bot") or {}, media.id)
        elif kind == "proxy":
            self._map_proxy(container, (product.get("proxy") or {}).get("basic_info") or {}, media.id)
        return media

    def _map_bot(self, container: StixObjects, bot: dict, media_id: str):
        info = bot.get("infostealer") or {}
        if ip := _safe(map_ipv4, _ipv4(info.get("ip_address")), extra_labels=["verity471:infected_machine"]):
            container.add(ip)
            container.add(self.relate(media_id, ip.id, "related-to", description="infected machine"))
        if stealer := _stealer_name(bot.get("stealer")):
            malware = map_malware(stealer)
            container.add(malware)
            container.add(self.relate(media_id, malware.id, "related-to", description="stealer"))

    def _map_proxy(self, container: StixObjects, basic: dict, media_id: str):
        if ip := _safe(map_ipv4, _ipv4(basic.get("ip_address")), extra_labels=["verity471:proxy"]):
            container.add(ip)
            container.add(self.relate(media_id, ip.id, "related-to", description="proxy"))
        if domain := _safe(map_domain, basic.get("domain"), extra_labels=["verity471:proxy"]):
            container.add(domain)
            container.add(self.relate(media_id, domain.id, "related-to", description="proxy"))

    def _product_description(self, product: dict, title: str, marketplace: Optional[dict]) -> str:
        kind = product.get("kind")
        kind_text = f" ({kind.replace('_', ' ')})" if kind else ""
        description = f"Marketplace listing {quote(title)}{kind_text}"
        if product.get("vendor_name"):
            description += f" by vendor {quote(product['vendor_name'])}"
        if marketplace and marketplace_name(marketplace):
            description += f" on {quote(marketplace_name(marketplace))}"
        description += "."
        prices = [f"{_number(p['value'])} {p['currency']}" for p in product.get("price") or []
                  if p.get("value") is not None and p.get("currency")]
        if prices:
            description += f" Price: {quote_plain(', '.join(prices))}."
        if created := (product.get("product") or {}).get("created_ts"):
            description += f" Listed on the market: {quote_plain(created)}."
        details = self._kind_details(kind, product)
        if details:
            description += " " + " ".join(details)
        return description

    @staticmethod
    def _kind_details(kind: Optional[str], product: dict) -> list:
        """Non-personal, kind-specific facts for the listing description."""
        details = []
        if kind == "bot":
            bot = product.get("bot") or {}
            info = bot.get("infostealer") or {}
            facts = [(label, info.get(key)) for label, key in (
                ("Country", "country"), ("ISP", "internet_service_provider"),
                ("Operating system", "operating_system"))]
            facts += [("Stealer", _stealer_name(bot.get("stealer"))), ("Infected", bot.get("installed_ts"))]
            details += [f"{label}: {quote(value)}." for label, value in facts if value]
        elif kind == "card":
            card = product.get("card") or {}
            cc = card.get("cc") or {}
            facts = [(label, cc.get(key)) for label, key in (
                ("BIN", "bin"), ("Payment system", "payment_system"), ("Bank", "bank"),
                ("Level", "level"), ("Class", "class"))]
            details += [f"{label}: {quote(value)}." for label, value in facts if value]
            available = card.get("available_info") or {}
            included = [label for key, label in _CARD_AVAILABLE if available.get(key)]
            if included:
                details.append(f"Includes: {', '.join(included)}.")
        elif kind == "proxy":
            basic = (product.get("proxy") or {}).get("basic_info") or {}
            facts = [(label, basic.get(key)) for label, key in (
                ("IP", "ip_address"), ("Proxy type", "proxy_type"), ("Country", "country"),
                ("ISP", "internet_service_provider"))]
            details += [f"{label}: {quote(value)}." for label, value in facts if value]
        elif kind == "database":
            basic = (product.get("database") or {}).get("basic_info") or {}
            if basic.get("records") is not None:
                details.append(f"Records: {quote_plain(basic['records'])}.")
            if basic.get("year") is not None:
                details.append(f"Year: {quote_plain(basic['year'])}.")
        elif kind == "exploit":
            basic = (product.get("exploit") or {}).get("basic_info") or {}
            facts = [(label, basic.get(key)) for label, key in (
                ("Category", "exploit_category"), ("Platform", "platform"),
                ("Affected version", "affected_version"), ("Risk", "risk"))]
            details += [f"{label}: {quote(value)}." for label, value in facts if value]
        return details

    # -- resource ------------------------------------------------------------

    def map_resource(self, container: StixObjects, resource: dict):
        name = resource.get("name")
        link = resource.get("link")
        included = [label for label, key in (("login", "login_available"),
                                             ("password", "password_available"),
                                             ("cookies", "cookies_available")) if resource.get(key)]
        labels = ["verity471:marketplace_resource"] + [f"verity471:includes_{i}" for i in included]
        description = self._resource_description(resource, included)

        targets = []
        domain_value = next((v for v in (name, urlparse(link).hostname if link else None,
                                         link) if v and _DOMAIN_RE.match(v)), None)
        if domain := _safe(map_domain, domain_value, extra_labels=labels, description=description):
            targets.append(domain)
        if link and link.startswith(("http://", "https://")):
            if url := _safe(map_url, link, extra_labels=labels, description=description):
                targets.append(url)
        for target in targets:
            container.add(target)

        # The bot listing (infected machine, stealer) is the context a resource hit
        # needs; map it even when the site itself can't become an observable.
        bot = self.lookups.product(resource.get("product_id"))
        if bot:
            media = self.map_product(container, bot)
            if media:
                for target in targets:
                    container.add(self.relate(target.id, media.id, "related-to", description="stolen data"))
        return targets or None

    @staticmethod
    def _resource_description(resource: dict, included: list) -> str:
        site = resource.get("name") or resource.get("link") or resource.get("id")
        description = f"Data for {quote(site)} offered in a marketplace bot (stealer log) listing."
        if included:
            description += f" Includes: {', '.join(included)}."
        infostealer = resource.get("infostealer") or {}
        if infostealer.get("browser"):
            description += f" Browser: {quote(infostealer['browser'])}."
        if infostealer.get("grabbed_ts"):
            description += f" Grabbed: {quote_plain(infostealer['grabbed_ts'])}."
        stolen = resource.get("stolen_data") or {}
        if stolen.get("datasets"):
            description += f" Datasets: {quote(', '.join(map(str, stolen['datasets'])))}."
        return description
