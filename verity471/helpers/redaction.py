"""Redaction of payment card numbers in free text taken from source data.

Marketplace listings (titles, descriptions) are seller-written text and can
contain card numbers. Truncated numbers - the first six digits (BIN) and the
last four, as card shops usually show them (``545212XXXXXX1234``) - are left
alone: PCI DSS allows displaying that form, and it is what a bank needs to
recognise a compromised card. A *full* card number is rewritten to that
truncated form before the text leaves the SDK (STIX output, alert summaries).
"""
from __future__ import annotations

import re
from typing import Optional

# A card number as written: 13-19 unbroken digits, or the standard groupings
# 4-4-4-(1..7) and 4-6-5 / 4-6-4 (Amex, Diners) separated by spaces or hyphens.
# It must not touch a letter, digit or hyphen, so fragments of UUIDs, hashes or
# longer ids never match.
_CARD_CANDIDATE = re.compile(
    r"(?<![\w-])"
    r"(?:\d{13,19}|\d{4}(?:[ -]\d{4}){2}[ -]\d{1,7}|\d{4}[ -]\d{6}[ -]\d{4,5})"
    r"(?![\w-])"
)


def _luhn_valid(digits: str) -> bool:
    total = 0
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _truncate(match: re.Match) -> str:
    digits = re.sub(r"[ -]", "", match.group(0))
    if not _luhn_valid(digits):
        return match.group(0)  # an id, order or phone number - not a card
    return digits[:6] + "X" * (len(digits) - 10) + digits[-4:]


def mask_card_numbers(text: Optional[str]) -> Optional[str]:
    """Rewrite full card numbers in *text* to first-6 + ``X`` + last-4.

    Only digit runs of card length (13-19, spaces/hyphens allowed) that pass the
    Luhn check are changed; already-truncated numbers and other text pass through.
    ``None`` and empty strings are returned unchanged.
    """
    if not text:
        return text
    return _CARD_CANDIDATE.sub(_truncate, text)
