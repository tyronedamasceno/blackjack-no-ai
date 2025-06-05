from blackjack.constants import (
    BLACKJACK_NUMBER_OF_CARDS,
    BLACKJACK_VALUE,
    DEFAULT_INITIAL_BALANCE,
    MAX_HAND_VALUE,
)
from blackjack.deck import Card


class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, new_card: Card):
        self._cards.append(new_card)

    def show(self, hide_first=False):  # pragma: no cover
        # TODO: improve this, and test
        start = 1 if hide_first else 0
        for card in self._cards[start:]:
            print(card)

        if not hide_first:
            print(f'Value: {self.value}')

    def clear(self):
        self._cards = []

    @property
    def value(self) -> int:
        tmp = 0
        for card in self._cards:
            tmp += card.value

        return tmp

    @property
    def is_blackjack(self) -> bool:
        return (
            len(self._cards) == BLACKJACK_NUMBER_OF_CARDS
            and self.value == BLACKJACK_VALUE
        )

    @property
    def is_busted(self) -> bool:
        return self.value > MAX_HAND_VALUE


class Player:
    def __init__(self, balance: float = DEFAULT_INITIAL_BALANCE):
        self.hand: Hand = Hand()
        self.balance = balance


class Dealer:
    def __init__(self):
        self.hand: Hand = Hand()
