import pytest

from blackjack.constants import DECK_SIZE
from blackjack.deck import Card, FrenchDeck, Shoe


def test_deck_size_is_52():
    assert len(FrenchDeck()) == DECK_SIZE


def test_deck_has_no_repeated_cards():
    assert len(FrenchDeck()) == len(set(FrenchDeck()._cards))


def test_card_equality_checks_rank_and_suit():
    assert Card('2', 'spades') == Card('2', 'spades')
    assert Card('2', 'spades') != Card('2', 'hearts')
    assert Card('2', 'spades') != Card('3', 'spades')


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


def test_default_shoe_has_6_decks():
    assert len(Shoe()) == 6 * DECK_SIZE


def test_create_shoe_with_non_default_size():
    assert len(Shoe(shoesize=3)) == 3 * DECK_SIZE


def test_drawing_a_card_remove_it_from_shoe():
    shoe = Shoe()
    shoe.draw()
    assert len(shoe) == (6 * DECK_SIZE) - 1


def test_shoe_is_shuffled_by_default():
    assert Shoe()._cards != Shoe()._cards
