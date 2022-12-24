#Class for players

from card_deck import CardBuilder


class Players:

    def add(self, card):
        self.hand.append(card)

    def get_hand():
        player_hand = []
        return player_hand
    
    def hand_sum(self):
        card_dict = CardBuilder.card_builder_dict()
        sum = 0
        for item in self.hand:
            sum += int(card_dict[item])
        return sum

    def __init__ (self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.split = 0

    def check_player_blackjack(self):
        total_val = 0
        card_dict = CardBuilder.card_builder_dict()
        blackjack = False
        for item in self.hand:
            total_val += int(card_dict[item])
            if 21 ==  total_val:
                print('Player has blackjack! Easy money.')
                blackjack = True
            else:
                blackjack = False
        return blackjack