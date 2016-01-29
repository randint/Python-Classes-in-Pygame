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

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def __str__(self):
        return values.get(self.value) + " of " + suits.get(self.suit)

class Deck:
    def __init__(self):
        self.deck = []
        self.dealtCards = []

        for s in range(4):
            suit, value = "", ""
            if s == 0:
                suit = "H"
            elif s == 1:
                suit = "S"
            elif s == 2:
                suit = "C"
            elif s == 3:
                suit = "D"
            for v in range(1, 14):
                if v == 1:
                    value = "A"
                elif v <= 10:
                    value = str(v)
                elif v == 11:
                    value = "J"
                elif v == 12:
                    value = "Q"
                elif v == 13:
                    value = "K"
                self.deck.append(Card(suit, value))

    def dealCard(self):
        picked = self.deck[random.randint(0, len(self.deck)) - 1]
        print(picked.value, picked.suit)
        self.dealtCards.append(picked)
        self.deck.remove(picked)
        return self.dealtCards[-1]

    def numCardsRemaining(self):
        return len(self.deck)

deck = Deck()

for card in deck.deck:
    print(card)
while deck.deck:
    print(deck.dealCard())
print(deck.deck)