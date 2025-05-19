from blackjack.deck import Card


class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, new_card: Card):
        self._cards.append(new_card)

    @property
    def hand_value(self):
        tmp = 0
        for card in self._cards:
            if isinstance(card.value, int):
                tmp += card.value
            elif isinstance(card.value, tuple):
                # TODO: think on how to handle it
                tmp += card.value[0]

        return tmp
