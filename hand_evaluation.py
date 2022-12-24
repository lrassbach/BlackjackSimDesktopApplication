###Hand Evaluation Class

import card_deck

class HandEvaluation:
    #this method will determine the makeup of the dealer hand
    def dealer_upcard(dealer_hand):
        card_deck_dict = card_deck.CardBuilder.card_builder_dict()
        dealer_show = dealer_hand[1]
        dealer_up_value = card_deck_dict[dealer_show]
        return dealer_up_value
    
    def hand_value_sum(hand):
        hand_value = 0
        card_deck_dict = card_deck.CardBuilder.card_builder_dict()
        for item in hand:
            hand_value += card_deck_dict[item]
        return hand_value
    
        #this method is hard coded to evaluate hard totals and determine the correct action for the best odds of winning 
    def hard_total_eval(hand_value, dealer_up_value):
        action = ''
        if hand_value <= 8:
            action = 'h'
        elif hand_value >= 17:
            action = 's'
        elif hand_value == 11:
            action = 'd'
        elif hand_value >= 13 and hand_value <= 16 and dealer_up_value < 7:
            action = 's'
            #TODO check this line below 
        elif hand_value == 12 and dealer_up_value < 4:
            action = 'h'
        elif hand_value == 12 and dealer_up_value > 3 and dealer_up_value < 7:
            action = 's'
        elif hand_value > 11 and hand_value < 17 and dealer_up_value > 6:
            action = 'h'
        elif hand_value == 10 and dealer_up_value < 10:
            action = 'h'
        elif hand_value == 10 and dealer_up_value > 9:
            action = 'd'
        elif hand_value == 9 and ((dealer_up_value < 3 or dealer_up_value > 6) == True):
            action = 'h'
        elif hand_value == 9 and dealer_up_value > 2 and dealer_up_value < 7:
            action = 'd'
        else:
            action = 'error: not hard total'
        return action
    
    def soft_total_eval(hand_value, dealer_up_value):
        action = ''
        non_ace = hand_value - 11
        if non_ace == 8 or non_ace == 9:
            action = 's'
        elif non_ace in [2,3] and dealer_up_value in [5,6]:
            action = 'd'
        elif non_ace in [2,3] and dealer_up_value not in [5,6]:
            action = 'h'
        elif non_ace in [4,5] and dealer_up_value in [4,5,6]:
            action = 'd'
        elif non_ace in [4,5] and dealer_up_value not in [4,5,6]:
            action = 'h'
        elif non_ace == 6 and dealer_up_value in [3,4,5,6]:
            action = 'd'
        elif non_ace == 6 and dealer_up_value == 7:
            action = 's'
        elif non_ace == 6 and dealer_up_value in [2,8,9,10,11]:
            action = 'h'
        elif non_ace == 7 and dealer_up_value in [2,7,8]:
            action = 's'
        elif non_ace == 7 and dealer_up_value in [3,4,5,6]:
            action = 'd'
        elif non_ace ==7 and dealer_up_value > 8:
            action = 'h'
        else:
            action = 'error: not soft hand'
        return action
    # Someday refactor into enum
    #TODO unit test szn
    def split_total_eval(hand_value, dealer_up_value):
        action = ''
        card_value = int(hand_value / 2)
        _2_hit = [2,8,9,10,11]
        _3_split = [4,5,6,7]
        _5_hit = [10,11]
        _6_split = [2,3,4,5,6]
        _7_hit = [8,9,10,11]        
        _9_stand = [7,10,11]

        if card_value == 2 and ((dealer_up_value in _2_hit) == True):
            action = 'h'
        elif card_value == 2 and dealer_up_value not in _2_hit:
            action = 'sp'
        elif card_value == 3 and dealer_up_value in _3_split:
            action = 'sp'
        elif card_value == 3 and dealer_up_value not in _3_split:
            action = 'h'
        elif card_value == 4:
            action = 'h'
        elif card_value == 5 and dealer_up_value in _5_hit:
            action = 'h'
        elif card_value == 5 and dealer_up_value not in _5_hit:
            action = 'd'
        elif card_value == 6 and dealer_up_value in _6_split:
            action = 'sp'
        elif card_value == 6 and dealer_up_value not in _6_split:
            action = 'h'
        elif card_value == 7 and dealer_up_value in _7_hit:
            action = 'h'
        elif card_value == 7 and dealer_up_value not in _7_hit:
            action = 'sp'
        elif card_value == 8:
            action = 'sp'
        elif card_value == 9 and dealer_up_value in _9_stand:
            action = 's'
        elif card_value == 9 and dealer_up_value not in _9_stand:
            action = 'sp'
        elif card_value == 10:
            action = 's'
        elif card_value == 11:
            action = 'sp'
        else:
            action ='error: not a split hand'
        return action
    
    def soft_check(hand):
        soft_tag = False
        #determine if an ace has been dealt to this hand 
        ace_spot = []
        for item in hand:
            a = item[0:3]
            if a == 'Ace':
                ace_spot.append(a)
        if len(ace_spot) == 1:
            soft_tag = True
        else:
            soft_tag = False
        return soft_tag
    
    def split_check(hand):
        values = 0
        card_dict = card_deck.CardBuilder.card_builder_dict()
        for item in hand:
            values += card_dict[item]
        split_value = values / 2
        if split_value == card_dict[hand[0]] and split_value == card_dict[hand[1]]:
            split_tag = True
        else:
            split_tag = False
        return split_tag

    def evaluation(hand, dealer_hand):
        #TODO SOLID principles
        hand_value = HandEvaluation.hand_value_sum(hand)
        dealer_up_value = HandEvaluation.dealer_upcard(dealer_hand)
        soft_tag = HandEvaluation.soft_check(hand)
        split_tag = HandEvaluation.split_check(hand)
        if soft_tag is True:
            action = HandEvaluation.soft_total_eval(hand_value, dealer_up_value)
        elif split_tag is True:
            action = HandEvaluation.split_total_eval(hand_value, dealer_up_value)
        else:
            action = HandEvaluation.hard_total_eval(hand_value, dealer_up_value)
        return action




