from lib.deck import Deck


class Player(object):
    """
    """
    def __init__(self):
        self.stack = Deck()

class Table(object):
    """
    """
    def __init__(self):
        pass

class WarGame(object):
    """
    """
    ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace") # defines the order of the cards

    def __init__(self):
        """
        """
        self.deck = StandardDeck()

        self.player1 = Player()
        self.player2 = Player()

        self.table = Table()

        
        self.deck.shuffle()
        self.deal_cards()
    

    def deal_cards(self):
        """
        """
        while len(self.deck.deck):

            deal_this_card = self.deck.deal_n_cards()
            if deal_this_card:
                self.player1.stack.accept_n_cards(deal_this_card)

            deal_this_card = self.deck.deal_n_cards()
            if deal_this_card:
                self.player2.stack.accept_n_cards(deal_this_card)




print ranks

print ranks.index('two')
print ranks.index('ace')

# ranks.index('ace') will give the index of ace

for rank in ranks:
    print ranks.index(rank)

if ranks.index('two') < ranks.index('ace'):
    print 'ace is greater than two'

def compare_cards(card1, card2):
    """
    """

    if ranks.index(card1) > ranks.index(card2):
        return 'card1 is greater than card2'
    elif ranks.index(card1) < ranks.index(card2):
        return 'card2 is greater than card1'
    else:
        return 'war'





