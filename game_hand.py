from hand import Hand
from dealer import Dealer
from deck import Deck


class GameHand(Hand):
    def __init__(self, dealer):
        self.dealer = dealer
        self.cards_in_hand = []
        super().__init__(deck=Deck, number_of_cards=2)

    def start_hand(self):
        while self.number_of_cards != 0:
            self.cards_in_hand.append(self.dealer.deal_card())
            self.number_of_cards -= 1

    def hit_me(self):
        self.cards_in_hand.append(self.dealer.deal_card())

