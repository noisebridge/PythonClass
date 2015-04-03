""" 
Deck class -    A generic deck with some functions for manipulating decks.
                Also the home of self.deck = deque(), child classes may inherit self.deck.

StandardDeck class - Uses Deck to implement a 52-card standard deck of playing cards, no jokers.


Unit Test Ideas
===============
Test the shuffle method
Test the cut method
Test that the StandardDeck attributes are there
Test deal_n_cards
Test accept_n_cards
DONE Test that deck is a deque


"""
from collections import deque
import random
import pprint 


class Deck(object):
    """ Contains common deck methods.
    """
    def __init__(self):
        self.deck = deque()

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
        If there aren't enough cards, return as many cards as are left.
        """
        cards_to_deal = deque()
        for i in range(num_to_deal):
            try:
                cards_to_deal.append(self.deck.pop())
            except IndexError:
                pass
        return cards_to_deal

    def accept_n_cards(self, cards):
        """ Accepts an iterable of cards and puts them back in the deck. 

        This function uses extendleft to accept. This must be consistent through the class.
        """
        self.deck.extendleft(cards)


class StandardDeck(Deck):
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

        def __repr__(self):
            return "Card of rank {0}, suit {1}\n".format(self.rank, self.suit)

    # These are sets. They are explicitly unique and unordered. This is just a collection of all possible cards.
    ranks = {"two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"}
    suits = {"spades", "clubs", "hearts", "diamonds"}

    def __init__(self):
        """ 
        """
        # idiom from: http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
        super(self.__class__, self).__init__()

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(self.Card(rank, suit))

    def __repr__(self):
        #this = [card.rank for card in self.deck]
        return "cards {}".format(pprint.pprint((self.deck)))
