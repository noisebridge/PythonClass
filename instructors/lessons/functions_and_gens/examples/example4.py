import unittest
from example1 import square_x

class SquareTest(unittest.TestCase):

    def test_square_pos_numbers(self):
        self.assertEqual(square_x(10), 100)

    def test_square_neg_numbers(self):
        self.assertEqual(square_x(-10), 100)

if __name__ == '__main__':
    unittest.main()