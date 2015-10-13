# each card must have a
# suit (spade, diamond, heart, club)
# value A, J, Q, K, 2 - 10

class Card:

    def __init__(self, suit, value):
        #YOUR CODE HERE

    def getSuit(self):
        #YOUR CODE HERE

    def getValue(self):
        #YOUR CODE HERE

# each card must have a
# suit (spade, diamond, heart, club)
# value A, J, Q, K, 2 - 10

class Deck:
    deck = []
    dealtCards = []

    def __init__(self, suit, value):
        # Create deck of cards
        # Each deck will have 52 Cards
        # 13 Hearts (A, J, K, Q, 2 - 10)
        # 13 Spade (A, J, K, Q, 2 - 10)
        # 13 Club (A, J, K, Q, 2 - 10)
        # 13 Diamonds (A, J, K, Q, 2 - 10)

        #Your Code here
        self.deck.append(Card("Heart", "J"))

    def dealCard(self):
        # deal a random card
        # once dealt, a card cannot be dealt again

    def howManyCardRemain(self):
        # return count of undealt cards

