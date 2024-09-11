from card_functions import card_selector

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