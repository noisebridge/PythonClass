import unittest
from square_grid import SquareGrid

class TestSquareGrid(unittest.TestCase):
    def setUp(self):
        a = [0] * 3
        b = [1] * 3
        c = [2] * 3
        self.matrix= [a,b,c]
        self.good_grid = SquareGrid(self.matrix)

    def test_error_on_mixed_dimensions(self):
        """Test object initialization"""
        four_by_three = self.matrix + [[3] * 3]
        with self.assertRaises(ValueError) as err:
            g = SquareGrid(four_by_three)

    def test_string_representation(self):
        """Test that the object behaves correctly with the `str()` built-in"""
        expected_string = "0 0 0\n1 1 1\n2 2 2"
        self.assertEqual(str(self.good_grid), expected_string)

    def test_length(self):
        """Test that the object returns a useful length"""
        self.assertEqual(len(self.good_grid), 3)

    def test_addition(self):
        """Test that addition for well-defined grids succeeds"""
        m = [[1,1,1],[1,1,1],[1,1,1]]
        g = SquareGrid(m)
        grid_sum = self.good_grid + g
        result_matrix = grid_sum.matrix
        expected_matrix = [[1,1,1],[2,2,2],[3,3,3]]
        self.assertEqual(result_matrix, expected_matrix)

    def test_addition_fails_on_mixed_dimensions(self):
        """Test that addition is undefined for grids of unequal dimension"""
        m = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        g = SquareGrid(m)
        with self.assertRaises(ValueError) as err:
            c = self.good_grid + g
