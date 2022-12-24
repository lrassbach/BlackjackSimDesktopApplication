import card_deck as cd
import dealer
import players
import hand_evaluation
from ui import UI

class SimulatorMain:
    
    def main():
        
        #this is going to be a while loop
        
        UI.welcome()
        print('------------------------------')
        name = input("Enter player name: ")
        p1 = players.Players(name)
        #somewhere near here there will be a check with the database to validate player name
        card_deck_dictionary = cd.CardBuilder.card_builder_dict()
        
        deck_size = 6
        table_deck = dealer.Dealer.table_deck_builder(card_deck_dictionary, deck_size)
        play = True
        quit = False
        while play == True:
            comparison = True
            dealer_hand, p1.hand, table_deck= dealer.Dealer.deal_card(table_deck, 1)
            UI.hand_display(dealer_hand,p1.hand)
            d_blackjack_check = dealer.Dealer.check_blackjack(dealer_hand)
            p_blackjack_check = p1.check_player_blackjack()
            #players.Players.check_player_blackjack(p1.hand) trying check player blackjack method called by p1 object
            if d_blackjack_check == True or p_blackjack_check == True:
                comparison = False
            if comparison == True:
                action = hand_evaluation.HandEvaluation.evaluation(p1.hand, dealer_hand)
                choice = UI.get_user_action()
                check, quit, p1.score = UI.action_check(choice, action, p1.score)
            if quit == True:
                play = False
            print('------------------------------')
            print('------------------------------')
        print("Player score: ")
        print(p1.score)
        print('Thanks for playing!')
            
SimulatorMain.main()