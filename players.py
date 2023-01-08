#Class for players

from card_deck import Cards


class Players:

    def __init__ (self, name, index):
        self.last = "null"
        self.index = index
        self.name = name
        self.score = 0
        self.hand = []
        self.split = 0
        self.ace_count = 0

    def add(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def display_hand(self):
        hand = self.name +"\'s hand: "
        i = 0
        for item in self.hand:
            if i > 0:
                hand += ", "
            hand += item
            i += 1
        print(hand)

    # TODO standalone method to evaluate aces

    def hand_sum(self):
        # TODO doesnt handle Aces correctly
        card_dict = Cards.card_builder_dict()
        sum = 0
        for item in self.hand:
            if item[0:3] == "Ace":
                sum += Cards.ace_evaluation(self.hand)
            else:
                sum += int(card_dict[item])
        return sum


        # A 8 10 3         

    def check_player_blackjack(self):
        total_val = 0
        card_dict = Cards.card_builder_dict()
        blackjack = False
        for item in self.hand:
            total_val += int(card_dict[item])
            if 21 ==  total_val:
                print('Player has blackjack! Easy money.')
                blackjack = True
            else:
                blackjack = False
        return blackjack