from cards import *
from math import pow

print(pow(2, 4))

deck = Deck()

print(deck.deal(1))
print(len(deck.dealt))
'''
for card in deck.cards:
    print(card)

print("")

while deck.cards:
    print(deck.deal_card())
'''