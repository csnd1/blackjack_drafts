import random
from deck import Deck


class Dealer(object):
    def __init__(self, deck):
        self.deck = deck

    def deal_card(self):
        dealt_card = random.choice(self.deck.cards)
        return dealt_card

