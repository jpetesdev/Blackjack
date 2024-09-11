import cards
import random
from time import sleep

##Testing change
round = True
# Will be used any time we need to pick a random card.
def card_selector():
    selected_suit = random.choice(cards.suits)
    selected_value = random.choice(cards.card_count[selected_suit])
    cards.card_count[selected_suit].remove(selected_value)
    selected_value = cards.card_values[selected_value]
    if selected_value != 11:
        display_card = f"{str(selected_value)}{selected_suit[0].upper()}"
    else:
        display_card = f"A{selected_suit[0].upper()}"
    return [selected_value, display_card]

def check_for_naturals():
    if (player1.hand[0][0] == 10 and player1.hand[1][0] == 11) or (player1.hand[0][1] == 11 and player1.hand[1][0] == 10):
        if (dealer1.hand[0][0] == 10 and dealer1.hand[1][0] == 11) or (dealer1.hand[0][0] == 11 and dealer1.hand[1][0] == 10):
            print("Two Naturals! It is a draw!")
        round = False
    elif (player1.hand[0][0] == 10 and player1.hand[1][0] == 11) or (player1.hand[0][0] == 11 and player1.hand[1][0] == 10):
        print("Player has a Natural!")
        round = False
    else:
        print("Did not find any Naturals!")

def check_for_21():
    total = 0
    for subset in player1.hand:
        total += subset[0]
        if total > 21:    
            print("Player BUST! Over 21!")
            return False
        
def hit():
    next_card = input("Would you like to HIT or STAND?: ")
    if next_card.lower() == "hit":
        player1.set_hand(card_selector())
        temp_count = 0
        for card in player1.hand:
            temp_count += card[0]
    



class Player():
    hand = [card_selector(), card_selector()]

    def __init__(self, name):
        self.name = name
        self._count = 0


    def set_count(self):
        for card in self.hand:
            self._count = self._count + card[0]
        return self._count
    
    def set_hand(self, add_card):
        self.hand.append(add_card)
        return self.hand


class Dealer(Player):
    hand = [card_selector(), card_selector()]

    def __init__(self):
        self._count = 0
        self.name = "Dealer"

    # hit function

    # stand function

player = input("Enter your name: ")
player1 = Player(player)
dealer1 = Dealer()

print(dealer1.hand)
dealer1.set_count()
print(dealer1._count)



 

while round:
    player1._count = 0
    if len(player1.hand) == 2:
        check_for_naturals()
    if len(player1.hand) == 2 and player1.hand[0][0] == 11 and player1.hand[1][0] == 11:
        player1.hand[0][0] = 1
        player1.set_count()
        print(player1.hand)
        print(player1._count)
    else:
        player1.set_count()
        print(player1.hand)
        print(player1._count)
    # Adding functionality to check for Naturals at start of game.
    next_card = input("Would you like to HIT or STAND?: ")
    if next_card.lower() == "hit":
        player1.set_hand(card_selector())
        temp_count = 0
        for card in player1.hand:
            temp_count += card[0]
    # Checking for Score Over 21 and if there is an Ace acting as an 11
        if temp_count > 21:
            for sublist in player1.hand:
                if 11 in sublist:
                    target = player1.hand.index(sublist)
                    player1.hand[target][0] = 1
                    break
    #Checking for hand over 21 with no ACE
    if check_for_21() == False:
        round = False
    # Checking to see if Player wants to STAND with the hand they have
    if next_card.lower() == "stand":
        round = False

while dealer1._count < 17:
    print(dealer1.set_count())
    print(dealer1._count)
    print(dealer1.hand)
    dealer1.set_hand(card_selector())
    temp_count = 0
    for card in dealer1.hand:
        temp_count += card[0]
    sleep(2)


                    

        

#print(player1.hand)
#print(cards.card_count)