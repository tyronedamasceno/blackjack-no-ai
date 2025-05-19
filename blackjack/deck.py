# Card and FrenchDeck are (strongly) based on https://www.fluentpython.com/

from functools import reduce
from random import shuffle


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit})"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False

        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash(f'{self.rank}.{self.suit}')

    @property
    def value(self):
        if self.rank.isdigit():
            return int(self.rank), None

        if self.rank in 'JQK':
            return 10, None

        return 1, 11


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)


class Shoe:
    def __init__(self, shoesize: int = 6):
        self._cards = reduce(
            lambda _c, deck: _c + deck._cards,
            (FrenchDeck() for _ in range(shoesize)),
            []
        )
        shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def draw(self) -> Card:
        return self._cards.pop(0)
