import card_deck as cd
import dealer
import players
import hand_evaluation
from ui import UI

def main():
    UI.welcome()
    print('------------------------------')
    name = input("Enter player name: ")
    p1 = players.Players(name)
    dealer_obj = players.Players("Dealer")
    card_deck_dictionary = cd.CardBuilder.card_builder_dict()
        
    deck_size = 6
    table_deck = dealer.Dealer.table_deck_builder(card_deck_dictionary, deck_size)
    play = True
    quit = False
    while play == True:
        table_deck, p1, dealer_obj = play_hand(table_deck, p1, dealer_obj)
        if p1.hand_sum() > 21:
            print("BUST")
            print("Dealer WINS")
        else:
            print("dealer: " + dealer_obj.hand[0] + ", " + dealer_obj.hand[1])
            while dealer_obj.hand_sum() < 17:
                table_deck, dealer_obj = dealer.Dealer.deal_one(table_deck, dealer_obj)
                print("...")
                hand_print = ""
                hand_print += dealer_obj.hand[0]
                i = 0
                for item in dealer_obj.hand:
                    hand_print += ", "
                    if i > 0:
                        hand_print += item
                    i += 1
                print("dealer: " + hand_print)
            if dealer_obj.hand_sum() > 21:
                print("Dealer BUST!")
            elif dealer_obj.hand_sum() == p1.hand_sum():
                print("Push")
            elif dealer_obj.hand_sum() < p1.hand_sum():
                print(p1.name + " WINS")
            else:
                print("Dealer WINS")

def play_hand(table_deck, player, dealer_obj):
    dealer_obj.hand, player.hand, table_deck= dealer.Dealer.initial_deal(table_deck, 1)
    UI.hand_display(dealer_obj.hand,player.hand)
    d_blackjack_check = dealer.Dealer.check_blackjack(dealer_obj.hand)
    p_blackjack_check = player.check_player_blackjack()
    if d_blackjack_check:
        print("dealer has blackjack. down bad")
        return table_deck, player, dealer_obj
    elif p_blackjack_check:
        print("you have blackjack! easy money")
        return table_deck, player, dealer_obj
    else:
        # play blackjack for player
        table_deck, player = player_play_blackjack_first_action(table_deck, player)
        return table_deck, player, dealer_obj
        # play blackjack for dealer

# returns table_deck & list of player hands
def player_play_blackjack_first_action(table_deck, player):
    # doesnt handle Aces correctly
    if player.hand[0][0:2] == player.hand[1][0:2]:
        action = UI.get_user_action(True)
        if action == "h":
            table_deck, player = dealer.Dealer.deal_one(table_deck, player)
            print("card dealt: " + player.hand[2])
            #begin recursive function here
        elif action == "d":
            table_deck, player = dealer.Dealer.deal_one(table_deck, player)
            return table_deck, player
        elif action == "s":
            return table_deck, player
        else:
            # this may need to be reworked
            second_hand = players.Players()
            second_hand.add(player.hand.pop(1))
            print("hand one...")
            table_deck, player = hit_or_stand(table_deck, player)
            table_deck, player = player_play_blackjack_first_action(table_deck, player)
            print("hand two...")
            table_deck, second_hand = hit_or_stand(table_deck, second_hand)
            table_deck, second_hand = player_play_blackjack_first_action(table_deck, second_hand)
    else:
        action = UI.get_user_action(False)
        if action == "h":
            table_deck, player = dealer.Dealer.deal_one(table_deck, player)
            print("card dealt: " + player.hand[2])
            return hit_or_stand(table_deck, player)
        elif action == "d":
            table_deck, player = dealer.Dealer.deal_one(table_deck, player)
            return table_deck, player
        elif action == "s":
            return table_deck, player
        else:
            second_hand = players.Players()
            second_hand.add(player.hand.pop(1))
            print(player.name + "hand one...")
            table_deck, player = hit_or_stand(table_deck, player)
            if (player.hand.length() > 1):
                table_deck, player = player_play_blackjack_first_action(table_deck, player)
            print(player.name + "hand two...")
            table_deck, second_hand = hit_or_stand(table_deck, second_hand)
            if (second_hand.hand.length() > 1):
                table_deck, player = player_play_blackjack_first_action(table_deck, player)


def hit_or_stand(table_deck, player):
    if (player.hand_sum() > 21):
        return table_deck, player
    action = UI.hit_or_stand()

    if (action == "h"):
        table_deck, player = dealer.Dealer.deal_one(table_deck, player)
        return hit_or_stand(table_deck, player)
    else:
        return table_deck, player

main()