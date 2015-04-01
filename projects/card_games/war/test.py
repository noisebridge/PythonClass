"""
Unit tests for deck.py

"""
import unittest
import collections

import lib.deck # Module to test


class TestDeck(unittest.TestCase):

    def setUp(self):
        """
        """
        self.deck = lib.deck.Deck()
        self.stddeck = lib.deck.StandardDeck()


    def test_deck_is_a_deque(self):
        self.assertEqual(self.deck.deck, collections.deque())

    def test_stddeck_has_52_cards(self):
        self.assertEqual(52, len(self.stddeck.deck))

    def test_each_stddeck_card_is_valid(self):
        for card in self.stddeck.deck:
            self.assertIn(card.rank, self.stddeck.ranks)
            self.assertIn(card.suit, self.stddeck.suits)

    def test_each_stddeck_card_is_unique(self):
        for card in self.stddeck.deck:
            card_instances = 0
            for card2 in self.stddeck.deck:
                if card.rank == card2.rank and card.suit == card2.suit:
                    card_instances += 1
            self.assertEqual(1,card_instances)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)



