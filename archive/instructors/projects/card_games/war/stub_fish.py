from lib.deck import StandardDeck, Deck
from collections import deque, Counter
import random



class Player(object):
    """
    """
    def __init__(self):
        self.stack = Deck()
        self.book = list()

class Table(object):
    """
    """
    def __init__(self):
        self.played_cards = Deck()
        #self.fishing_pot = StandardDeck()
        self.cur_player_deq = deque()

#decision of what DS to use with hands, discuss what operations we will need 
#and what will be most manageable getters and setters, 
#time and memory shouldn't be of concern
class GoFishGame(object):
    """
    """
    ranks = ("two", "three", "four", "five", "six", "seven", "eight", 
             "nine", "ten", "jack", "queen", "king", "ace") # defines the order of the cards

    def __init__(self):
        """
        """
        self.fishing_pot = StandardDeck()

        self.player1 = Player()
        self.player2 = Player()


        self.table = Table()
        self.cur_players = self.table.cur_player_deq.extend([self.player1, self.player2])
        self.losers_list = list()
        
        self.fishing_pot.shuffle()
        self.deal_cards()

        #self.play_gofish()

    def deal_cards(self):
        """
        """
        amt_of_cards = 7 #this may vary with version of GoFish rules
        amt_dealt_init_hand1 = self.fishing_pot.deal_n_cards(amt_of_cards)
        amt_dealt_init_hand2 = self.fishing_pot.deal_n_cards(amt_of_cards) #redundant

        self.player1.stack.accept_n_cards(amt_dealt_init_hand1)
        self.player2.stack.accept_n_cards(amt_dealt_init_hand2)
        print "dealing {} cards to each player".format(amt_of_cards)

    def computer_guesser(self):
        #guess_card = random.random(len(self.fishing_pot))
        cur_player = self.cur_players[0]

        mock_deck = StandardDeck()
        rand_cardrank_num_fromdeck = random.randint(0, len(mock_deck.ranks) - 1)
        rand_cardrank_num_fromhand = random.randint(0, len(cur_player.stack) - 1)
        #current player value?
        guessed_card_method_deck = list(mock_deck)[rand_cardrank_num_fromdeck]

        guessed_card_method_hand = list(cur_player.stack)[rand_cardrank_num_fromhand]

        return guessed_card_method_hand

    def compare_books(self):
        if self.player1.book > self.player2.book:
            return "player one wins!"
        elif self.player1.book < self.player2.book:
            return "player two wins!"
        else:
            "you both lose"


#
    def run_round(self):
        if self.fishing_pot: #if there aren't any cards in the fishing pot compare books and game ends
            card_rank_guess = self.computer_guesser()
            not_cur_player = self.cur_player_deq[-1] #starting to think about mult players
            if card_rank_guess in list(not_cur_player.stack.ranks):
                pass
            self.cur_player_deq.rotate()

        else:
            self.compare_books()
#end TM 040615
    def check_hand_for_books(self): #put logic in org_cards
        cur_player = self.cur_players[0]
        for card in cur_player.stack.deck:
            pass
        c = Counter(cur_player.stack.deck)
        lis = list()
        for i in c.itervalues():
            if c[i] == 4:
                lis.append(c.pop[i])

    def go_fish(self):
        cur_player = self.cur_players[0]
        cur_player.stack.accept_n_cards(self.fishing_pot.deal_n_cards())
        


    def org_cards_in_hand(self):
        count = Counter(self.cur_players[0].stack.deck)
        for gr_rank in count:
            if gr_rank.value == 4:
                pass #deal to cur_player.book


    #def win_condition(self):
    #   if 
