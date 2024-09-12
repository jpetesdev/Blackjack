import cards
import random
from time import sleep

##Testing change
round = True
dealer_hand = True
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
    elif ((dealer1.hand[0][0] == 10 and dealer1.hand[1][0] == 11) or (dealer1.hand[0][0] == 11 and dealer1.hand[1][0] == 10)):
        print("Dealer has a Natural Blackjack!")
    else:
        print("Did not find any Naturals!")

def check_for_over_21():
    total = 0
    for subset in player1.hand:
        total += subset[0]
        if total > 21:    
            print("Player BUST! Over 21!")
            return True
        
def hit():
    next_card = input("Would you like to HIT or STAND?: ")
    if next_card.lower() == "hit":
        player1.set_hand(card_selector())
        temp_count = 0
        for card in player1.hand:
            temp_count += card[0]

def display_hands_score(player, dealer):
    player1.set_count()
    dealer1.set_count()
    print("************************************************************")
    print(f"{player.name}'s hand is: {str(player.hand)}. CURRENT SCORE: {str(player._count)}")
    print(f"{dealer.name}'s hand is: {str(dealer.hand[0])}. CURRENT SCORE: {str(dealer.hand[0][0])}")
    print("************************************************************")
    sleep(1)

# Returns an array with two elements: First is the player's final score, second is the dealers final score.
def display_final_score(player, dealer):
    print("***************************")
    print("HERE ARE THE FINAL RESULTS")
    print("***************************")
    player_final_score = player._count
    dealer_final_score = dealer._count
    print(f"{player.name}'s hand is: {str(player.hand)}. FINAL SCORE: {str(player._count)}")
    print(f"{dealer.name}'s hand is: {str(dealer.hand)}. FINAL SCORE: {str(dealer._count)}")
    if (player_final_score > dealer_final_score) and (player_final_score < 22) and (dealer_final_score < 22):
        print(f"{player.name} WINS!")
    elif player_final_score == dealer_final_score:
        print("This Hand Is A Draw!")
    else: 
        print(f"The Dealer Wins!")
    print("***************************")
    


class Player():
    hand = [card_selector(), card_selector()]

    def __init__(self, name):
        self.name = name
        self._count = 0


    def set_count(self):
        self._count = 0
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


player = input("Enter your name: ")
player1 = Player(player)
dealer1 = Dealer()

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
        dealer1.set_count()
        sleep(1)
        display_hands_score(player1, dealer1)
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
    if check_for_over_21() == True:
        player1.set_count()
        round = False
    # Checking to see if Player wants to STAND with the hand they have
    if next_card.lower() == "stand":
        round = False

# Dealer Rules
# Dealer goes after player has chosen STAND.
# If Dealer's hand is less than 17, they MUST HIT
# Once the Dealer's hand is 17 or greater, they MUST stand
# IF the dealer would get an ACE and it would put them over 17, but not over 21 they must take it and stand.

while dealer_hand:
    print()
    print(f"Dealer's hand is: {str(dealer1.hand)}. CURRENT SCORE: {str(dealer1.set_count())}")
    sleep(1)
    if (dealer1._count < 17) and (player1._count < 22):
        print("The Dealer's hand is less than 17, so they must take another card.")
        dealer1.set_hand(card_selector())
        temp_count = 0
        for card in dealer1.hand:
            temp_count += card[0]
    # Checking for Score Over 21 and if there is an Ace acting as an 11
        if temp_count > 21:
            for sublist in dealer1.hand:
                if 11 in sublist:
                    target = dealer1.hand.index(sublist)
                    dealer1.hand[target][0] = 1
        #print(dealer1.hand)
        dealer1.set_count()
        #print(dealer1._count)
        sleep(1)
        if dealer1._count > 21:
            print("Dealer has gone BUST!")
            sleep(1)
            dealer_hand = False
    if dealer1._count >= 17:
        print(f"Dealer's new hand is: {str(dealer1.hand)}. CURRENT SCORE: {str(dealer1.set_count())}")
        sleep(2)
        #print(dealer1.hand)
        dealer_hand = False
    

display_final_score(player1, dealer1)
                    

# Improvement Notes

'''
1. Make it so that the "displayed card" for Jacks, Queens, and Kings show J, Q, K instead of 10
2. Make Naturals portion more accuarte
'''
