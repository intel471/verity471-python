import pytest

from verity471.helpers.redaction import mask_card_numbers


@pytest.mark.parametrize("text, expected", [
    ("4111111111111111", "411111XXXXXX1111"),
    ("card 4111 1111 1111 1111 exp 12/29", "card 411111XXXXXX1111 exp 12/29"),
    ("4111-1111-1111-1111", "411111XXXXXX1111"),
    ("amex 378282246310005", "amex 378282XXXXX0005"),
    ("545212XXXXXX1234", "545212XXXXXX1234"),          # already truncated
    ("4111111111111112", "4111111111111112"),          # fails Luhn: not a card
    ("order 123456789012", "order 123456789012"),      # too short
    ("phone +1 555 0100", "phone +1 555 0100"),
    ("two: 4111111111111111 and 5555555555554444", "two: 411111XXXXXX1111 and 555555XXXXXX4444"),
    ("amex grouped 3782 822463 10005", "amex grouped 378282XXXXX0005"),
    # Digit runs inside ids must never be touched, even when they pass Luhn.
    ("incident--4c1234a5-6789-0123-4567-89f0c123b45d", "incident--4c1234a5-6789-0123-4567-89f0c123b45d"),
    ("relationship--cae12345-6789-0123-4567-89c0ef1e2d34", "relationship--cae12345-6789-0123-4567-89c0ef1e2d34"),
    ("ref ab4111111111111111", "ref ab4111111111111111"),
    ("4111-11111-1111111", "4111-11111-1111111"),      # not a card grouping
    (None, None),
    ("", ""),
])
def test_mask_card_numbers(text, expected):
    assert mask_card_numbers(text) == expected
