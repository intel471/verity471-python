# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from verity471.api.credentials_api import CredentialsApi
    from verity471.api.events_api import EventsApi
    from verity471.api.girs_api import GIRsApi
    from verity471.api.indicators_api import IndicatorsApi
    from verity471.api.malware_api import MalwareApi
    from verity471.api.reports_api import ReportsApi
    from verity471.api.sources_api import SourcesApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from verity471.api.credentials_api import CredentialsApi
from verity471.api.events_api import EventsApi
from verity471.api.girs_api import GIRsApi
from verity471.api.indicators_api import IndicatorsApi
from verity471.api.malware_api import MalwareApi
from verity471.api.reports_api import ReportsApi
from verity471.api.sources_api import SourcesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
