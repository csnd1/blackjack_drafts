from card import Card


class Deck(Card):

    def __init__(self, card):
        super().__init__()
        self.card = card
        self.card_list = []

    def create_deck(self):
        for card.value in range(1, 14):
            for card.suit in card.suits:
                self.card_list.append("{} of {}".format(int(card.value), str(card.suit)))


card = Card(1, 2)
deck = Deck(card)
deck.create_deck()
print(deck.card_list)
print(len(deck.card_list))