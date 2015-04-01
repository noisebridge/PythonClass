"""
Unit tests for deck.py

"""
import unittest
import collections
import copy

import lib.deck # Module to test


class TestDeck(unittest.TestCase):

    def setUp(self):
        """
        """
        self.deck = lib.deck.Deck()
        self.stddeck = lib.deck.StandardDeck()
        self.cardcount = len(self.stddeck.suits) * len(self.stddeck.ranks)


    def test_deck_is_a_deque(self):
        self.assertEqual(self.deck.deck, collections.deque())

    def test_stddeck_has_all_the_cards(self):
        self.assertEqual(self.cardcount, len(self.stddeck.deck))

    def test_each_stddeck_cards_are_valid(self):
        for card in self.stddeck.deck:
            self.assertIn(card.rank, self.stddeck.ranks)
            self.assertIn(card.suit, self.stddeck.suits)

    def test_each_stddeck_cards_are_unique(self):
        for card in self.stddeck.deck:
            card_instances = 0
            for card2 in self.stddeck.deck:
                if card.rank == card2.rank and card.suit == card2.suit:
                    card_instances += 1
            self.assertEqual(1,card_instances)

    def test_stddeck_cut_method(self):

        self.stddeck2 = copy.deepcopy(self.stddeck)
        # Check to make sure these are different objects (different memory)
        self.assertNotEqual(self.stddeck2, self.stddeck)
        
        def check_deck_equality(deck1, deck2):
            """ Check to make sure that the two decks have the same order of cards.
            """

            for i in xrange(len(deck1.deck)):
                self.assertEqual(deck1.deck[i].rank, deck2.deck[i].rank)
                self.assertEqual(deck1.deck[i].suit, deck2.deck[i].suit)

        check_deck_equality(self.stddeck, self.stddeck2)

        # cut both decks using rotate OR the cut method
        for cutsize in xrange(self.cardcount):
            self.stddeck.cut(cutsize)
            self.stddeck2.deck.rotate(cutsize)
            check_deck_equality(self.stddeck, self.stddeck2)

        


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeck)
    unittest.TextTestRunner(verbosity=2).run(suite)



