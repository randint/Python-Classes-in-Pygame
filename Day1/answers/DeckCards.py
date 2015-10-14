import random

# each card must have a
# suit (spade, diamond, heart, club)
# value A, J, Q, K, 2 - 10

class Card:
    suit = ""
    value = ""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

# each card must have a
# suit (spade, diamond, heart, club)
# value A, J, Q, K, 2 - 10

class Deck:
    deck = []
    dealtCards = []

    def __init__(self):
        # Create deck of cards
        # Each deck will have 52 Cards
        # 13 Hearts (A, J, K, Q, 2 - 10)
        # 13 Spade (A, J, K, Q, 2 - 10)
        # 13 Club (A, J, K, Q, 2 - 10)
        # 13 Diamonds (A, J, K, Q, 2 - 10)

        # Loop over all suits
        for suit in ['Heart', 'Spade', 'Diamond', 'Club']:
            # For all suits, loop over all values
            for value in ['A', 'J', 'K', 'Q', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                self.deck.append(Card(suit, value))

    def dealCard(self):
        # deal a random card
        # once dealt, a card cannot be dealt again

        # Make a random number using randint between 0 and the number of the cards in the deck
        # The 'pop' method removes this card and returns it.

        # We could add a check to see if we still have more cards!
        return self.deck.pop(random.randint(0, len(self.deck)-1))

    def howManyCardsRemain(self):
        # return count of undealt cards
        return len(self.deck)

