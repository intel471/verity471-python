import re

from stix2 import TLP_AMBER

REMOVE_HTML_REGEX = re.compile(r"<.*?>")
X_OPENCTI_CREATED_BY = "x_opencti_created_by_ref"
X_OPENCTI_LABELS = "x_opencti_labels"
X_OPENCTI_ALIASES = "x_opencti_aliases"
MARKING = TLP_AMBER
INTEL_471 = "Intel 471"
PLATFORM_VERITY471 = "platform:verity471"
# Value used for the `source` field of alert-derived Incident objects.
SOURCE_VERITY = f"{INTEL_471} Verity"
