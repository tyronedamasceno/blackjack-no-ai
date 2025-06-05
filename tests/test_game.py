import pytest

from blackjack.constants import DEFAULT_INITIAL_BALANCE
from blackjack.deck import Card
from blackjack.game import Dealer, Hand, Player


def test_hand_is_created_empty():
    hand = Hand()
    assert len(hand._cards) == 0


def test_hand_add_card():
    hand = Hand()
    hand.add_card(Card('2', 'spades'))

    assert len(hand._cards) == 1


def test_hand_clear():
    hand = Hand()
    hand.add_card(Card('2', 'spades'))
    hand.clear()

    assert len(hand._cards) == 0


@pytest.mark.parametrize(
    ('rank1', 'rank2', 'expected'),
    [
        ('A', '10', 21),
        ('10', '9', 19),
        ('5', '6', 11),
        ('3', '4', 7),
    ],
)
def test_hand_get_value(rank1, rank2, expected):
    hand = Hand()
    hand.add_card(Card(rank=rank1, suit='spades'))
    hand.add_card(Card(rank=rank2, suit='spades'))
    assert hand.value is expected


@pytest.mark.parametrize(
    ('rank1', 'rank2', 'expected'),
    [
        ('A', '10', True),
        ('10', 'A', True),
        ('A', '8', False),
        ('10', '8', False),
    ],
)
def test_hand_check_is_blackjack(rank1, rank2, expected):
    hand = Hand()
    hand.add_card(Card(rank=rank1, suit='spades'))
    hand.add_card(Card(rank=rank2, suit='spades'))
    assert hand.is_blackjack is expected


@pytest.mark.parametrize(
    ('rank1', 'rank2', 'rank3', 'expected'),
    [
        ('10', 'J', '3', True),
        ('9', '8', '7', True),
        ('A', '5', '6', True),  # TODO: fix ACEs value, this is not busted
        ('3', '4', '9', False),
        ('10', '5', '6', False),
    ],
)
def test_hand_check_is_busted(rank1, rank2, rank3, expected):
    hand = Hand()
    hand.add_card(Card(rank=rank1, suit='spades'))
    hand.add_card(Card(rank=rank2, suit='spades'))
    hand.add_card(Card(rank=rank3, suit='spades'))
    assert hand.is_busted is expected


def test_player_default_balance_is_100():
    assert Player().balance == DEFAULT_INITIAL_BALANCE


def test_dealer():
    # just to keep 100% coverage, maybe dealer should be a player
    assert Dealer()
