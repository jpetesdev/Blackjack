import cards
import random

##Testing change

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

round = True
 

while round:
    player1._count = 0
    if len(player1.hand) == 2 and player1.hand[0][0] == 11 and player1.hand[1][0] == 11:
        player1.hand[0][0] = 1
        player1.set_count()
        print(player1.hand)
        print(player1._count)
    else:
        player1.set_count()
        print(player1.hand)
        print(player1._count)
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
    #if temp_count > 21:
        #round = False

                    

        

#print(player1.hand)
#print(cards.card_count)