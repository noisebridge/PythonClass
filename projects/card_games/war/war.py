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
        self.played_cards = Deck()


class WarGame(object):
    """
    """
    ranks = ("two", "three", "four", "five", "six", "seven", "eight", 
             "nine", "ten", "jack", "queen", "king", "ace") # defines the order of the cards

    def __init__(self):
        """
        """
        self.deck = StandardDeck()

        self.player1 = Player()
        self.player2 = Player()

        self.table = Table()
        self.losers_list = list()
        
        self.deck.shuffle()
        self.deal_cards()
        self.play_war()

    
    def play_war(self):
        """ This run each round and checks if the game is over.
        """
    
        # break when someone loses (for now)
        while True:
            run_round()
        # Runs at the end of while, even if it never loops
        else:
            finish_game()

    def finish_game():
        """ Resolve the game
        """

        print losers_list

        
    def run_round(self):
        """ Each player plays a card and the cards are compared.
        """
        
        def compare_cards(card1, card2):
            """
            What do we want to get out of compare_cards?
            1. Player 1 wins (1>2): player 1 is given all the played cards
            2. Player 2 wins (2>1): player 2 is given all the played cards
            3. WAR!! (1=2): We do a war

            """

            if ranks.index(card1) > ranks.index(card2):
                print card1, " > ", card2, " Player 1 wins."
                return self.player1
            elif ranks.index(card1) < ranks.index(card2):
                print card1, " < ", card2, " Player 2 wins."
                return self.player2
            # WAR!!
            else:
                print "A war is on!"
                return None

        def draw_cards(num_to_draw, player):
            """
            """
            card = player.deck.deal_n_cards(num_to_draw)
            if len(card) = 0:
                losers_list.append(player)

        player1_card = draw_cards(1, self.player1)
        player2_card = draw_cards(1, self.player2)
        winner = None

        while not winner:
            
            winner = compare_cards(player1_card, player2_card)
            
            # Give all played cards to the table.
            table.played_cards.accept_n_cards(player1_card)
            table.played_cards.accept_n_cards(player2_card)

            if not winner:
                # initialize a war
                table.played_cards.accept_n_cards(draw_cards(3, self.player1))
                table.played_cards.accept_n_cards(draw_cards(3, self.player2))
                player1_card = draw_cards(1, self.player1)
                player2_card = draw_cards(1, self.player2)
            """
            """
         


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

