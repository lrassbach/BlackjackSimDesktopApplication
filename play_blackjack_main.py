import card_deck as cd
import dealer
import players
from ui import UI

def main():
    UI.welcome()
    print('------------------------------')
    name = input("Enter player name: ")
    dealer_obj = players.Players("Dealer", 1)
    card_deck_dictionary = cd.CardBuilder.card_builder_dict()
    deck_size = 6
    table_deck = dealer.Dealer.table_deck_builder(card_deck_dictionary, deck_size)
    play = True
    while play == True:
        print("New hand!")
        p1 = players.Players(name, 1)
        p1.last = ""
        dealer_obj.hand, p1.hand, table_deck= dealer.Dealer.initial_deal(table_deck, 1)
        # TODO need to refactor
        d_blackjack_check = dealer.Dealer.check_blackjack(dealer_obj.hand)
        p_blackjack_check = p1.check_player_blackjack()
        # TODO update blackjack check to evaluate 
        if d_blackjack_check:
            print("dealer has blackjack. down bad")
        elif p_blackjack_check:
            print("you have blackjack! easy money")
        else:
            table_deck, p1, dealer_obj = play_hand(table_deck, p1, dealer_obj)
            table_deck, p1, dealer_obj = eval_player_vs_dealer(table_deck, p1, dealer_obj)
        print("...")

            

def eval_player_vs_dealer(table_deck, player, dealer_obj):
    if type(player) == int:
        return table_deck, player, dealer_obj
    else:
        if player.hand_sum() > 21:
            print(player.name + " BUST")
            dealer_obj.display_hand()
        elif player.hand_sum() < 22:
            table_deck, dealer_obj = dealer_sequence(table_deck, dealer_obj)
            player, dealer_obj = dealer_comp(player, dealer_obj)
        table_deck, player.split, dealer_obj = eval_player_vs_dealer(table_deck, player.split, dealer_obj)
        return table_deck, player, dealer_obj

def dealer_sequence(table_deck, dealer_obj):
    print("dealer: Flip card -->" + dealer_obj.hand[0] + ", " + dealer_obj.hand[1])
    while dealer_obj.hand_sum() < 17:
        table_deck, dealer_obj = dealer.Dealer.deal_one(table_deck, dealer_obj)
        hand_print = ""
        hand_print += dealer_obj.hand[0]
        i = 0
        for item in dealer_obj.hand:
            if i > 0:
                hand_print += ", "
                hand_print += item
            i += 1
        print("dealer: " + hand_print)
    return table_deck, dealer_obj
    
    

def dealer_comp(player, dealer_obj):
    if dealer_obj.hand_sum() == player.hand_sum():
        print("Push")
    elif dealer_obj.hand_sum() > 21:
        print("Dealer BUST")
    elif dealer_obj.hand_sum() > player.hand_sum():
        print("Dealer WINS")
    else:
        print(player.name + " WINS")
    print('------------------------------')
    return player, dealer_obj


def play_hand(table_deck, player, dealer_obj):
    UI.hand_display(dealer_obj.hand,player)
    table_deck, player = player_play_blackjack(table_deck, player)
    return table_deck, player, dealer_obj

# returns table_deck & list of player hands
def player_play_blackjack(table_deck, player):
    if player.hand_sum() > 21:
        print("BUST")
        print("Dealer WINS")
        return table_deck, player
    if len(player.hand) == 2:    
        if player.hand[0][0:2] == player.hand[1][0:2]:
            action = UI.get_user_action(True)
            if action == "h":
                table_deck, player = dealer.Dealer.deal_one(table_deck, player)
                return player_play_blackjack(table_deck, player)
            elif action == "d":
                table_deck, player = dealer.Dealer.deal_one(table_deck, player)
                return table_deck, player
            elif action == "s":
                return table_deck, player
            else:
                #TODO need to add UI elements for readability during execution
                player.split = players.Players(str(player.index) + " hand of " + player.name, player.index + 1)
                player.split.add(player.hand.pop(1))
                print("Hand " + player.index + "...")
                table_deck, player = player_play_blackjack(table_deck, player)
                print("Hand " + player.split.index + "...")
                table_deck, player.split = player_play_blackjack(table_deck, player.split)
                return table_deck, player
        else:
            action = UI.get_user_action(False)
            if action == "h":
                table_deck, player = dealer.Dealer.deal_one(table_deck, player)
                return player_play_blackjack(table_deck, player)
            elif action == "d":
                table_deck, player = dealer.Dealer.deal_one(table_deck, player)
                return table_deck, player
            elif action == "s":
                return table_deck, player
    else:
        table_deck, player = hit_or_stand(table_deck, player)
        if player.last == "s":
            return table_deck, player
        else:
            return player_play_blackjack(table_deck, player)

def hit_or_stand(table_deck, player):
    action = UI.hit_or_stand()
    player.last = action
    if (action == "h"):
        table_deck, player = dealer.Dealer.deal_one(table_deck, player)
        return table_deck, player
    else:
        return table_deck, player

main()