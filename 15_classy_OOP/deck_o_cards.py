#from Think Python 

class Card(object):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # Suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # Ranks are the same... it's a tie
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + '\n'
        return s

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    #reimplementation of shuffle function
    """def shuffle(self):
        import random
        numCards = len(self.cards)
        for i in range(numCards):
            j = random.randrange(i, numCards)  # pick a card to swap with i
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])"""



d = Deck()
#can we do the below? why not?
print(d)
d.shuffle()
print(d)
