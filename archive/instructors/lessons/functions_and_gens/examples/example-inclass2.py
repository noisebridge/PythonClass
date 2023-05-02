import unittest
from example1 import square_x_plus_ten

class TestSquare(unittest.TestCase):

    def test_square_x_plus_ten(self):
        self.assertEqual(square_x_plus_ten(10), 110)

    def test_negs(self):
        self.assertEqual(square_x_plus_ten(-10), 110)

    def test_floats(self):
        self.assertEqual(square_x_plus_ten(10.0), 110)

if __name__ == '__main__':
    unittest.main()