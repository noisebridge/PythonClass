""" 
                        Rules:
Two players per game with a Standard Deck of playing cards
each player is initially dealt five cards
the rest of the cards are in the fishing_pot
the player to go first is chosen at random
the current player asks the other player for a rank
the other player must give the current asking player ALL of the cards of that rank to the asking player
if the answering player has none of that rank 
the asking player must "go fish" and draw a card from the fishing_pot
when a player has four cards of one rank in their hand they must 
file those four cards from their hand into a book placed in front of them 
when the fishing_pot is empty then the players continue 
to ask until all books are on the table
the winner is determined by who ever has more books
"""

from lib.deck import StandardDeck, Deck


class Player(object):
    """
    """
    def __init__(self):
        self.hand = Deck()
        self.book = list()

class Table(object):
    """
    """
    def __init__(self):
        self.played_cards = Deck()

