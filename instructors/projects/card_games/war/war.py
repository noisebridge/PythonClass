from lib.deck import StandardDeck, Deck


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


    def play_war(self):
        """ This run each round and checks if the game is over.
        """
    
        # exit() when someone loses, for now (see finish_game method)
        while True:
            self.run_round()

    def finish_game(self):
        """ Resolve the game
        """

        print self.losers_list
        exit()

        
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

            card1_rank = self.ranks.index(card1[0].rank)
            card2_rank = self.ranks.index(card2[0].rank)

            player1_decksize = len(self.player1.stack.deck)
            player2_decksize = len(self.player2.stack.deck)

            if card1_rank > card2_rank:
                print card1[0].rank, " > ", card2[0].rank, " Player 1 wins.", 
                print "Player 1 deck: ", player1_decksize, " cards. Player 2 deck: ", player2_decksize, "cards."
                return self.player1
            elif card1_rank < card2_rank:
                print card1[0].rank, " < ", card2[0].rank, " Player 2 wins."
                print "Player 1 deck: ", player1_decksize, " cards. Player 2 deck: ", player2_decksize, "cards."
                return self.player2
            # WAR!!
            else:
                print "A war is on!"
                return None

        def draw_cards(num_to_draw, player):
            """
            """
            card = player.stack.deal_n_cards(num_to_draw)
            if len(card) == 0:
                self.losers_list.append(player)

            return card

        player1_card = draw_cards(1, self.player1)
        player2_card = draw_cards(1, self.player2)
        # Check if the game is done after all draws are complete.
        if len(self.losers_list) > 0:
            self.finish_game()
        winner = None

        while not winner:
            
            winner = compare_cards(player1_card, player2_card)
            
            # Give all played cards to the table.
            self.table.played_cards.accept_n_cards(player1_card)
            self.table.played_cards.accept_n_cards(player2_card)

            if not winner:
                # initialize a war
                self.table.played_cards.accept_n_cards(draw_cards(3, self.player1))
                self.table.played_cards.accept_n_cards(draw_cards(3, self.player2))
                player1_card = draw_cards(1, self.player1)
                player2_card = draw_cards(1, self.player2)
                # Check if the game is done after all draws are complete.
                if len(self.losers_list) > 0:
                    self.finish_game()
        
        # Give all the cards in the played_cards to the winner
        winner.stack.accept_n_cards(self.table.played_cards.deal_n_cards(len(self.table.played_cards.deck)))


if __name__ == "__main__":
    wargame = WarGame()

