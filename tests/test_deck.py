import pytest

from blackjack.constants import DECK_SIZE
from blackjack.deck import Card, FrenchDeck


def test_deck_size_is_52():
    assert len(FrenchDeck()) == DECK_SIZE


def test_deck_has_no_repeated_cards():
    assert len(FrenchDeck()) == len(set(FrenchDeck()._cards))


@pytest.mark.parametrize(("rank", "expected"), [
    ('2', (2, None)),
    ('9', (9, None)),
    ('10', (10, None)),
    ('J', (10, None)),
    ('K', (10, None)),
    ('A', (1, 11)),
])
def test_card_values(rank, expected):
    assert Card(rank, 'spades').value == expected
