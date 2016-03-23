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
        return "{0} of {1}".format(self.rank, self.suit)


    #unneccesary example of a color of a card, however good illustration of an @property
    #color should be a data attribute but it needs calculation, thus it belongs as a property
    @property
    def color(self):
        if "diamonds" == self.suit or "hearts" == self.suit:
            self._color = "red"
            return self._color
        elif "spades" == self.suit or "clubs" == self.suit:
            self._color = "black"
            return self._color
        else: 
            self._color = None
            return self._color


class PlayingDeck(object):
    '''A Deck of 'Playing Cards'
       initialized with classic the 52 cards, no jokers
    ''' 

    ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    suits = ["spades", "clubs", "hearts", "diamonds"]

    def __init__(self, type_of_card):

        #double-ended queue is going to be used to emulate a real-world Deck of Cards
        #the left side of the deque is the bottom of a Deck and the right side is the top
        self.deck_container = deque()

        for rank in self.ranks:
             for suit in self.suits:
                 self.deck_container.append(PlayingCard(rank, suit))

    def __repr__(self):
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
            #print 'running shuffle for the {}'.format(x_time)
            random.shuffle(self.deck_container)
    
    def pass_n_cards(self, num_to_deal):
        '''take n amount of cards from top of PlayingDeck instance, 
               that is from the right side of the deck_container
        '''

        holder = deque()    #need ability to hold each 'popped' card until passed and received by another Deck like object
        for num in range(num_to_deal):
            holder.append(self.deck_container.pop())
        return holder

    def receive_n_cards(self, cards):
        '''receive n amount of cards and put on bottom of PlayingDeck instance, 
              that is the left side of the deck_container 
        '''

        #designed to receive another deque object
        #needs to take each element of the deque and append it to self.deck_container 
        for card in cards:
            self.deck_container.appendleft(card)
'''
pd = PlayingDeck(PlayingCard) 
another_playing_deck = PlayingDeck(PlayingCard)

another_playing_deck.receive_n_cards( pd.pass_n_cards(22) )

print len(another_playing_deck.deck_container)
print(another_playing_deck)

print pd.deck_container[0]
print pd.deck_container[0].color 
print pd.deck_container[1]
print pd.deck_container[1].color 

     


'''

#unnecessary list "dead-end" code alley below
  
  #self.deck_container.insert( self.deck_container[randint], self.deck_container[randint:] )
