from deck import Deck


class Hand(object):
    def __init__(self, deck=None, number_of_cards=None):
        self.deck = deck
        self.number_of_cards = number_of_cards
        if not self.number_of_cards:
            raise ValueError("You must provide a number of cards")
        if not self.deck:
            raise ValueError("You must provide a deck")
        super().__init__()

        # for _ in range(number_of_cards):
        #     self.append(random_card)...


# deck = Deck()
# x = Hand(deck, number_of_cards=1)
