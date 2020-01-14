played_card_dict = {}
card_list = []
dict_deck = {}
dict_deck2 = {}
values = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9),("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
number_of_decks = [1]
list_deck = []


yeet = ["Deck", "Suit", "Card(tuple)"]
list()

yeet_dict = {}
for key in reversed(yeet):
    yeet_dict = {key: yeet_dict}

print(yeet_dict)
# {'Deck': {'Suit': {'Card(tuple)': {}}}}

# yeet = [number_of_decks, suits, values]
yeet_dict.update()















class Deck(object):

    def __init__(self):
        self.played_card_dict = {}
        self.default_deck = []
        self.dict_deck = {}
        self.dict_deck2 = {}
        self.values = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9),("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self.number_of_decks = []
        self.list_deck = []

    def create_default_deck(self):
        for value in self.values:
            for suit in self.suits:
                self.default_deck.append("{} of {}".format(str(value[0]), str(suit)))

    def create_default_dict_deck(self):
        card_values = dict(self.values)
        self.dict_deck = dict((suits, card_values)for suits in self.suits)
        return self.dict_deck

    def cards_based_on_number_of_decks(self, number):
        while number != 0:


#     def add_played_card(self, card):
#         self.played_card_dict.update(card)
#
#     def remove_played_card(self, card):
#         self.dict_deck.pop("Diamonds")

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


# card = Card(1,1)
deck = Deck()
# deck.create_deck()
deck.create_default_deck()
print(deck.default_deck)
# deck.cards_based_on_number_of_decks_dict(2)
# print(deck.card_list)
# print(len(deck.card_list))
# print(deck.dict_deck)
# print(deck.card_list)
# print(len(deck.dict_deck["Diamonds"]))
# print(max(deck.dict_deck["Diamonds"].values()))
# print(len(deck.dict_deck))
# deck.add_played_card({"Diamonds": {"Ace": 1}})
# deck.add_played_card({"Diamonds": {"2": 2}})
# deck.remove_played_card({"Diamonds": {"Ace": 1}})
# print(deck.played_card_dict)
# print(deck.dict_deck)
# print(len(deck.dict_deck["Diamonds"]))
# print(deck.card_list)