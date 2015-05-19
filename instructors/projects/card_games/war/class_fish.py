""" 
                        Rules:
Two players per game with a Standard Deck of playing cards
each player is initially dealt five cards
the rest of the cards are in the fishing_pot
the player to go first is chosen at random
the current player asks the other player for a rank
the other player must give the current asking player ALL of the cards of that rank to the asking player
if the answering player has none of that rank 
the asking player must "go fish" and draws a card from the top of the fishing_pot
when a player has four cards of one rank in their hand they must 
file those four cards from their hand into a book placed in front of them 
when the fishing_pot is empty then the players continue 
to ask until all books are on the table
the winner is determined by who ever has more books
"""

from lib.deck import StandardDeck, Deck
from collections import deque
from random import randint

class Player(object):
    """
    """
    def __init__(self):
        self.hand = Deck()
        self.book = list()


class GoFishGame(object):
    """
    """
    ranks = ("two", "three", "four", "five", "six", "seven", "eight", 
             "nine", "ten", "jack", "queen", "king", "ace") # defines the order of the cards

    def __init__(self):
        """
        """
        

        self.player1 = Player()
        self.player2 = Player()
        self.players = deque([self.player1, self.player2])
        self.players.rotate(randint(0, len(self.players)))
        self.asker = self.players[0]
        self.answerer = self.players[-1]

        #once players are initialized then we can deal
        self.fishing_pot = StandardDeck()
        self.fishing_pot.shuffle()
        self.deal_cards()


    def deal_cards(self):
        amt_to_deal = 5
        for player in self.players:
            player.hand.accept_n_cards(self.fishing_pot.deal_n_cards(amt_to_deal))
        #self.player1.accept_n_cards(self.deck.deal_n_cards(amt_to_deal))
        #self.player2.accept_n_cards(self.deck.deal_n_cards(amt_to_deal))

    def count_hand(self, player):
        org_hand = dict()
        for card in player.hand:
            times = org_hand.get(card.rank, 0)
            times += 1
            org_hand[card.rank] = times
        return org_hand

'''letter_frequency_dict = {}
word = "noisebridge"

for letter in word:
    print letter_frequency_dict
    times = letter_frequency_dict.get(letter, 0)
    print letter
    print times
    times += 1
    print times
    letter_frequency_dict[letter] = times
'''