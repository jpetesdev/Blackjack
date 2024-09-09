import main

class Player():
    hand = [card_selector(), card_selector()]
    money_left = 100

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


class Dealer():
    hand = []

    def __init__(self):
        self._count = 0

    # hit function

    # stand function