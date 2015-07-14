'''Standard playing deck and card objects rewritten to be more modular, main difference is that 
   PlayingCard and PlayingDeck are their own independent objects and inheritance has not been 
   utlized to extend functionality. For instance we could implement different kinds of decks and 
   cards necesary to play different games such as poker with jokers and wild cards, uno or Tarock  
'''

import random
from collections import deque


class PlayingCard(object):
    '''A classic 'Playing Card' for traditional games such as poker, war and go fish.
       each PlayingCard has a rank, suit, and color
    '''
    
    def __init__(self, rank, suit):  #every single instance needs a rank and suit! 

        self.rank = rank
        self.suit = suit 

    def __repr__(self): 
        '''used to print info about Card
        '''
        return "{0} of {1}".format(self.rank, self.suit)


class PlayingDeck(object):
    '''A Deck of 'Playing Cards'
       initialized with classic the 52 cards, no jokers
       double-ended queue is used to emulate a real-world Deck of Cards
       the left side of the deque is the bottom of a Deck and the right side is the top
    ''' 

    ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    suits = ["spades", "clubs", "hearts", "diamonds"]

    def __init__(self, type_of_card):

        self.deck_container = deque()
        self.type_of_card = type_of_card


    def build_standard_deck(self):
        for rank in self.ranks:
             for suit in self.suits:
                 self.deck_container.append(self.type_of_card(rank, suit))

        return "deck of type {} built".format(self.type_of_card)


    def __repr__(self):
        '''used to print info about Card
        '''
        return "deck of length: {0}\n all cards: {1}".format(len(self.deck_container), self.deck_container)


    def cut(self):
        '''cut the deck using a generated psuedo random integer
        '''
        randint = random.randint(0, len(self.deck_container) )
        self.deck_container.rotate(randint)
  
    def shuffle(self, x_times):
        '''shuffle the deck in place according to a psuedo random number algorithm within python,
           x_times is entered to ensure quality of shuffle, however beware psuedo random patterns!
        '''
        for x_time in range(x_times):
            random.shuffle(self.deck_container)
    
    def pass_n_cards(self, num_to_deal):
        '''take n amount of cards from top of PlayingDeck instance, 
               that is from the right side of the deck_container
               this method needs the ability to hold each 'popped' card until 
                  it is passed and received by another Deck-like object
        '''
        holder = deque()    
        for num in range(num_to_deal):
            holder.append(self.deck_container.pop())
        return holder

    def receive_n_cards(self, cards):
        '''receive n amount of cards and put on bottom of PlayingDeck instance, 
              the bottom is the left side of the deck_container 
              designed to receive another deque object
              needs to take each element of the deque and append it to self.deck_container
        '''
        for card in cards:
            self.deck_container.appendleft(card)


if __name__ == '__main__':
    '''Inside this block is code that should only be run when this module is exectued directly, 
       not when its objects imported
    '''
 
    pd = PlayingDeck(PlayingCard) 
    another_playing_deck = PlayingDeck(PlayingCard)

    print dir(pd)
    print pd.build_standard_deck()

