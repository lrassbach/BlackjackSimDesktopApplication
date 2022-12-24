dictionary_test_1 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}
dictionary_test_2 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}
dictionary_test_3 = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}

list_test = [dictionary_test_1, dictionary_test_2, dictionary_test_3] 

import card_deck

table_deck = card_deck.CardBuilder.card_builder_list()

#print(table_deck)


def deal_card(table_deck, num_players):
            import players as players
            hand = players.Players.get_hand()
            dealer_hand = []
            x = 1
            for item in range(4):
                if x % 2 != 0:
                    card = table_deck.pop(0)
                    hand.append(card)
                    x += 1
                elif x % 2 == 0:
                    card = table_deck.pop(0)
                    #its popping out the item and removing the list item. throwing off the index
                    dealer_hand.append(card)
                    x += 1
            return dealer_hand, hand, table_deck

dealer_hand, hand, table_deck = deal_card(table_deck, 1)
print(dealer_hand)
print(hand)
