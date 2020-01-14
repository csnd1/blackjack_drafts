from game_hand import GameHand
from dealer import Dealer
from deck import Deck


class Score(object):
    def __init__(self, gamehand):
        self.values = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9),("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self.dict_deck = {}
        self.gamehand = gamehand
        self.tup = [("7", "Diamonds"), ("Jack", "Clubs")]

    def test_return_values(self):
        total = 0
        for card in self.tup:
            for suit in self.dict_deck.keys():
                if suit in card:
                    for name in self.dict_deck[suit].keys():
                        if name in card:
                            total += self.dict_deck[suit].get(name)
        return total

    def create_dict_deck(self):
        card_values = dict(self.values)
        self.dict_deck = dict((suits, card_values)for suits in self.suits)
        return self.dict_deck

    def return_values(self):
        total = 0
        for card in self.tup:
            total += self.dict_deck[card[1]][card[0]]
        return total



deck = Deck()
deck.create_deck(1)
dealer = Dealer(deck)
gamehand = GameHand(dealer)
# gamehand.start_hand()
# print(gamehand.cards_in_hand)
score = Score(gamehand)
score.create_dict_deck()
# print(score.dict_deck)
print(score.ace())
# print(score.dict_deck)
print(score.x())
