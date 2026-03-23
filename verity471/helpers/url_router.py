from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

from verity471.api_client import ApiClient
from verity471.api.credentials_api import CredentialsApi


class UnresolvableURL(Exception):
    """Raised when a URL cannot be mapped to a known SDK route."""
from verity471.api.events_api import EventsApi
from verity471.api.indicators_api import IndicatorsApi
from verity471.api.malware_api import MalwareApi
from verity471.api.reports_api import ReportsApi
from verity471.api.sources_api import SourcesApi

# Ordered list of (path_template, ApiClass, method_name).
# More-specific paths must come before shorter prefix matches
# (e.g. /credentials/occurrences/{id} before /credentials/{id}).
_RAW_ROUTES: list[tuple[str, type, str]] = [
    # Sources
    ("/integrations/sources/v1/forums/posts/{post_id}", SourcesApi, "get_forums_posts_post_id"),
    ("/integrations/sources/v1/forums/private-messages/{private_message_id}", SourcesApi, "get_forums_private_messages_private_message_id"),
    ("/integrations/sources/v1/data-leak-sites/file-listings/{id}", SourcesApi, "get_data_leak_sites_file_listings_id"),
    ("/integrations/sources/v1/messaging-services/messages/{message_id}", SourcesApi, "get_messaging_services_messages_message_id"),
    # Reports
    ("/integrations/intel-report/v1/reports/breach-alert/{id}", ReportsApi, "get_reports_breach_alert_id"),
    ("/integrations/intel-report/v1/reports/fintel/{id}", ReportsApi, "get_reports_fintel_id"),
    ("/integrations/intel-report/v1/reports/geopol/{id}", ReportsApi, "get_reports_geopol_id"),
    ("/integrations/intel-report/v1/reports/info/{id}", ReportsApi, "get_reports_info_id"),
    ("/integrations/intel-report/v1/reports/malware/{id}", ReportsApi, "get_reports_malware_id"),
    ("/integrations/intel-report/v1/reports/spot/{id}", ReportsApi, "get_reports_spot_id"),
    ("/integrations/intel-report/v1/reports/vulnerability/{id}", ReportsApi, "get_reports_vulnerability_id"),
    # Credentials
    ("/integrations/creds/v1/credentials/occurrences/{id}", CredentialsApi, "get_credentials_occurrences_id"),
    ("/integrations/creds/v1/credentials/{id}", CredentialsApi, "get_credentials_id"),
    ("/integrations/creds/v1/credential-sets/{id}", CredentialsApi, "get_credential_sets_id"),
    # Indicators
    ("/integrations/indicators/v1/indicators/{id}", IndicatorsApi, "get_indicator_by_id"),
    # Events and Malware
    ("/integrations/malware-intel/v1/events/{id}", EventsApi, "get_event_by_id"),
    ("/integrations/malware-intel/v1/malware/{id}", MalwareApi, "get_malware_family_by_id"),
]


def _template_to_regex(template: str) -> re.Pattern[str]:
    parts = re.split(r'\{(\w+)\}', template)
    segments = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            segments.append(re.escape(part))
        else:
            segments.append(f'(?P<{part}>[^/]+)')
    return re.compile(''.join(segments) + '$')


_COMPILED_ROUTES: list[tuple[re.Pattern[str], type, str]] = [
    (_template_to_regex(template), api_class, method_name)
    for template, api_class, method_name in _RAW_ROUTES
]


def resolve_url(url: str) -> tuple[type, str, dict[str, str]] | None:
    """Parse a Verity API URL and return (ApiClass, method_name, path_params).

    Returns None if no route matches.

    Example::

        api_class, method, params = resolve_url(
            "https://api.intel471.cloud/integrations/sources/v1/forums/posts/post--abc"
        )
        # -> (SourcesApi, 'get_forums_posts_post_id', {'post_id': 'post--abc'})
    """
    path = urlparse(url).path
    for pattern, api_class, method_name in _COMPILED_ROUTES:
        m = pattern.match(path)
        if m:
            return api_class, method_name, m.groupdict()
    return None


def call_url(api_client: ApiClient, url: str) -> Any:
    """Resolve a Verity API URL and call the corresponding API method.

    Raises ValueError if the URL does not match any known route.

    Example::

        obj = call_url(api_client,
            "https://api.intel471.cloud/integrations/sources/v1/forums/posts/post--abc"
        )
        # -> ForumsPost object
    """
    resolved = resolve_url(url)
    if resolved is None:
        raise UnresolvableURL(f"No API route found for URL: {url}")
    api_class, method_name, path_params = resolved
    instance = api_class(api_client)
    return getattr(instance, method_name)(**path_params)
