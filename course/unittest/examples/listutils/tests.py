"""
"""
import listutils
import unittest

class TestListMethods(unittest.TestCase):

    def setUp(self):
        
        self.mytestconditions = [ ([1,2],3), ([2,4],6), ([3,6],9) ]

    def test_sum_my_list(self):
    
        for condition, result in self.mytestconditions:
            # check that the conditions produce the result
            self.assertEqual(listutils.sum_my_list(condition), result)

if __name__ == '__main__':
    unittest.main()
