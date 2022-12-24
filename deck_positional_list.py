
def deck_positional_list(num_suits):
    #input number of suits & determine length
    num_suits = 4
    num_suits = int(num_suits)
    deck_length = (52 / 4) * num_suits
    deck_length = int(deck_length)
    #print(num_suits,"suits;",deck_length,"cards")
    #takes inputs and determines number of suits
    suit_list = ["Hearts","Clubs","Spades","Diamonds"]
    suits_reqd = []
    x = 0
    for item in suit_list:
        suits_reqd.insert(x,suit_list[x])
        x = x + 1
        if x == num_suits:
            break
    #uses length and number of suits to create a list of cards in a deck
    positional_list_card_deck = []
    x = 1
    y = 0
    face = ["Jack","Queen","King","Ace"]
    def dict_card_build(x,y):    
        for item in range(deck_length):
            if x <= 9:
                card = str(x+1) + " of " + str(suits_reqd[y])
                positional_list_card_deck.append(card)
                x = x + 1
            elif 9 < x <= 12:
                card = str(face[x-10]) + " of " + str(suits_reqd[y])
                positional_list_card_deck.append(card)
                x = x + 1
            elif x == 13:
                card = str(face[x-10]) + " of " + str(suits_reqd[y])
                positional_list_card_deck.append(card)
                x = x + 1
    for item in suits_reqd:
        dict_card_build(x,y)
        y = y + 1
    return positional_list_card_deck

