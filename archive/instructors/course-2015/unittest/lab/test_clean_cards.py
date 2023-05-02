import unittest
from collections import deque

from clean_cards import PlayingCard, PlayingDeck


class TestPlayingCard(unittest.TestCase):

   def setUp(self):
       self.single_card = PlayingCard("two", "diamonds")


   def test_playing_card_existence(self):
        self.assertTrue( self.single_card )


   def test_playing_card_repr(self):
       self.assertEqual( self.single_card.__repr__(), "two of diamonds")


class TestPlayingDeck(unittest.TestCase):

    def setUp(self):
        self.empty_deck = PlayingDeck( PlayingCard )

        self.built_deck = PlayingDeck( PlayingCard )
        self.built_deck.build_standard_deck()


    def test_playing_deck_existence(self):
        self.assertTrue( self.built_deck )

    def test_built_standard_deck_length(self):
        self.assertEqual( len(self.built_deck.deck_container), 52 )

    def test_twoofdiamonds_lessthan_threeofclubs(self):
        self.assertLess( self.built_deck.deck_container[0], self.built_deck.deck_container[5] )

    def test_pass_n_cards_removes_card(self):
         self.assertEqual( deque([PlayingCard("ace", "spades")]) , self.built_deck.pass_n_cards(1) )


#below: list of things to test! (revisable)

#test existence of object, testing proper initialization
#test repr and string print out

#test ranks and comparison values
#test for 52 cards, each card being unique
#pop container does actually take away card from self.deck_container
#test pseudo randomness
#cut is effective
#x_times works in the shuffle method
#pass and receiving


