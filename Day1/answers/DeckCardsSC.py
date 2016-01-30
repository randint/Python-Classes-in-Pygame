import random

suits = {
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs",
    "D": "Diamonds",
}

values = {
    "A": "Ace",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
}


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def __str__(self):
        return values.get(self.value) + " of " + suits.get(self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.dealtCards = []

        for suit in ['H', 'S', 'D', 'C']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))

    def deal_card(self):
        self.dealtCards.append(self.cards.pop(random.randint(0, len(self.cards)) - 1))
        return self.dealtCards[-1]


    def num_remaining(self):
        return len(self.cards)


deck = Deck()
for card in deck.cards:
    print(card)

print("")

while deck.cards:
    print(deck.deal_card())