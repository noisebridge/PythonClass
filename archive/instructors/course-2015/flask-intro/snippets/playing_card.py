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
