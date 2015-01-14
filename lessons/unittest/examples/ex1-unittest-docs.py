

import random
import unittest


# This is a child (inheritance) of the TestCase class in unittest module.
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # seq = (0..9)
        self.seq = range(10)
        self.cat = 4
        self.mouse = 2
        
        self.cats = []
        for factor in range(10):
            self.cats.append(factor*self.mouse)

    def robots_are_awesome(self):
        self.assertEqual("robots", "robots")

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    def test_cat_eq_mouseplusmouse(self):
        self.assertEqual(self.cat, self.mouse+self.mouse)

    def test_cats_factorof_mouse(self):
        for poss_cat in self.cats:
            self.assertEqual(poss_cat % self.mouse, 0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)


