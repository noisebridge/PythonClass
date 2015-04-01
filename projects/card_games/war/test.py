"""
Unit tests for deck.py

"""
import unittest
import collections

import lib.deck # Module to test


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        """
        """
        self.deck = deck.Deck()
        self.stddeck = deck.StandardDeck()


    def test_deck_is_a_deque(self):
        self.assertEqual(self.deck.deck, collections.deque())


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)


