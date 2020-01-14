from card import Card
import  random


class Deck(object):

    def __init__(self):
        self.default_deck_tuple = []
        self.played_card_dict = {}
        self.played_cards = []
        self.default_deck = []
        self.cards = []
        self.dict_deck = {}
        self.values = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9),("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

    # not implemented, used in background
    def create_default_deck(self):
        for value in self.values:
            for suit in self.suits:
                self.default_deck.append("{} of {}".format(str(value[0]), str(suit)))

    def create_default_dict_deck(self):
        card_values = dict(self.values)
        self.dict_deck = dict((suits, card_values)for suits in self.suits)
        return self.dict_deck

    def create_deck(self, number_of_decks):
        self.create_default_deck()
        self.cards = self.default_deck * number_of_decks


#     def add_played_card(self, card):
#         self.played_card_dict.update(card)
#
    def remove_played_card(self, dealt_card):
        if dealt_card in self.cards:
            self.cards.remove(dealt_card)
        else:
            print("oops")

    def add_played_card(self, dealt_card):
        if dealt_card in self.cards:
            self.played_cards.append(dealt_card)
        else:
            print("oops")

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_default_deck_tuple(self):
        for value in self.values:
            for suit in self.suits:
                self.default_deck_tuple.append((str(value[0]), str(suit)))

    # def cards_based_on_number_of_decks_dict(self, number):
    #     card_values = dict(self.values)
    #     while number != 0:
    #         self.number_of_decks.append("deck {}".format(number))
    #         number -= 1
#         # print(self.number_of_decks)
#         self.list_deck = tuple(((number, suits))for number in self.number_of_decks for suits in self.suits)
#         # print(self.list_deck)
#         # self.dict_deck.update((((self.list_deck))for suits in self.suits))
#         self.dict_deck2 = dict(((self.list_deck, card_values)for number in self.number_of_decks))
#         # print(self.dict_deck2)
#         # self.list_deck.update(dict(self.dict_deck))
#         x = dict(zip(self.number_of_decks, self.suits))
#         print(x)

deck = Deck()
# deck.create_default_deck()
deck.create_default_deck_tuple()
# print(deck.default_deck)
print(deck.default_deck_tuple)
# deck.shuffle_deck()
# print(deck.cards)
