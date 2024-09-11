import random
import cards
from player_dealer import Player, Dealer

player = input("Enter your name: ")
player1 = Player(player)
dealer1 = Dealer()



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

def check_for_neutrals():
    if (player1[0][0] == 10 and player1[0][1] == 11) or (player1[0][0] == 11 and player1[0][1] == 10):
        if (dealer1[0][0] == 10 and dealer1[0][1] == 11) or (dealer1[0][0] == 11 and dealer1[0][1] == 10):
            print("Two Naturals! It is a draw!")
            
            
