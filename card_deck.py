####Card Deck
####Builds a Card Deck based on the parameters you choose

class CardBuilder:

    def card_builder_dict():
        #input number of suits & determine length
        num_suits = 4
        deck_length = (52 / 4) * num_suits
        deck_length = int(deck_length)
        #takes inputs and determines number of suits
        suit_list = ["Hearts","Clubs","Spades","Diamonds"]
        suits_reqd = []
        x = 0
        for item in suit_list:
            suits_reqd.insert(x,suit_list[x])
            x += 1
            if x == num_suits:
                break
        #uses length and number of suits to create a dictionary
        card_deck = {
            }
        x = 1
        y = 0
        face = ["Jack","Queen","King","Ace"]
        def card_build(x,y):    
            for item in range(deck_length):
                if x <= 9:
                    card = str(x+1) + " of " + str(suits_reqd[y])
                    card_deck[card] = x + 1
                    x = x + 1
                elif 9 < x <= 12:
                    card = str(face[x-10]) + " of " + str(suits_reqd[y])
                    card_deck[card] = 10
                    x = x + 1
                elif x == 13:
                    card = str(face[x-10]) + " of " + str(suits_reqd[y])
                    card_deck[card] = 11
                    x = x + 1
        for item in suits_reqd:
            card_build(x,y)
            y = y + 1
        card_deck_dict = card_deck
        return card_deck_dict
    
    
    def card_builder_list():
        #this function creates a list of keys to resemble a card deck to your specifications
        #input number of suits & determine length
        num_suits = 4
        deck_length = (52 / 4) * num_suits
        deck_length = int(deck_length)
        #takes inputs and determines number of suits
        suit_list = ["Hearts","Clubs","Spades","Diamonds"]
        suits_reqd = []
        x = 0
        for item in suit_list:
            suits_reqd.insert(x,suit_list[x])
            x += 1
            if x == num_suits:
                break
        #uses length and number of suits to create a list of keys 
        card_deck = []
        x = 1
        y = 0
        face = ["Jack","Queen","King","Ace"]
        def card_build(x,y):    
            for item in range(deck_length):
                if x <= 9:
                    card = str(x+1) + " of " + str(suits_reqd[y])
                    card_deck.append(card)
                    x = x + 1
                elif 9 < x <= 12:
                    card = str(face[x-10]) + " of " + str(suits_reqd[y])
                    card_deck.append(card)
                    x = x + 1
                elif x == 13:
                    card = str(face[x-10]) + " of " + str(suits_reqd[y])
                    card_deck.append(card)
                    x = x + 1
        for item in suits_reqd:
            card_build(x,y)
            y = y + 1
        card_deck_list = card_deck
        return card_deck_list
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # SOFT CARD DECK BUILDER -> Still in Development       
    # def soft_card_builder():
    #     #input number of suits & determine length
    #     num_suits = 4
    #     num_suits = int(num_suits)
    #     deck_length = (52 / 4) * num_suits
    #     deck_length = int(deck_length)
    #     #takes inputs and determines number of suits
    #     suit_list = ["Hearts","Clubs","Spades","Diamonds"]
    #     suits_reqd = []
    #     x = 0
    #     for item in suit_list:
    #         suits_reqd.insert(x,suit_list[x])
    #         x += 1
    #         if x == num_suits:
    #             break
    #     #uses length and number of suits to create a dictionary
    #     card_deck = {
    #         }
    #     x = 1
    #     y = 0
    #     face = ["Jack","Queen","King","Ace"]
    #     def dict_card_build(x,y):    
    #         for item in range(deck_length):
    #             if x <= 9:
    #                 card = str(x+1) + " of " + str(suits_reqd[y])
    #                 card_deck[card] = x + 1
    #                 x = x + 1
    #             elif 9 < x <= 12:
    #                 card = str(face[x-10]) + " of " + str(suits_reqd[y])
    #                 card_deck[card] = 10
    #                 x = x + 1
    #             elif x == 13:
    #                 card = str(face[x-10]) + " of " + str(suits_reqd[y])
    #                 card_deck[card] = 1
    #                 x = x + 1
    #     for item in suits_reqd:
    #         dict_card_build(x,y)
    #         y = y + 1
    #     soft_card_deck = card_deck
    #     return soft_card_deck