""" 

"""
import collections.deque

class StandardDeck(object):
    """ A standard 52-card deck. Cards are stored, ordered, in a collections.deque object.
    """
    ranks = set("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
    suits = set("spades", "clubs", "hearts", "diamonds")

    def __init__(self):
        """ 
        """
        
