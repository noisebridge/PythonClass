""" 

"""
from collections import deque
import random


class StandardDeck(object):
    """ A standard 52-card deck. Cards are stored, ordered, in a collections.deque object.
    """

    class Card(object):
        """ A single playing card, contains a rank and a suit
        """
        
        def __init__(self, rank, suit):
            """
            """
            self.rank = rank
            self.suit = suit

    # These are sets. They are explicitly unique and unordered. This is just a collection of all possible cards.
    ranks = {"two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"}
    suits = {"spades", "clubs", "hearts", "diamonds"}

    def __init__(self):
        """ 
        """
        self.deck = deque()
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(self.Card(rank, suit))

    def shuffle(self):
        """ Randomizes the order of the deck
        """
        random.shuffle(self.deck)

    def cut(self, cut_size):
        """ Cuts the deck
        """
        self.deck.rotate(cut_size)

    def deal_n_cards(self, num_to_deal=1):
        """ Deals an iterable containing one card from the top of the deck.

        This function uses pop() to deal from the right. This must be consistent through the class.
        """
        cards_to_deal = collections.deque()

        for i in range(num_to_deal):
            cards_to_deal.append(self.deck.pop())

        return cards_to_deal


    def accept_n_cards(self, cards):
        """ Accepts an iterable of cards and puts them back in the deck. 

        This function uses extendleft to accept. This must be consistent through the class.
        """
        self.deck.extendleft(cards)



