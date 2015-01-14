import unittest

class TestLists(unittest.TestCase):

    def setUp(self):
        print('')
        print('in {} - setUp()'.format(self.id()))
        self.myList = range(1,5)


    def test_len(self):
        print('in {} - test_len()'.format(self.id()))
        self.assertEqual( len(self.myList), 4)
        self.myList.append(-1)
        self.assertEqual( len(self.myList), 5)

    def test_min(self):
        print('in {} - test_len()'.format(self.id()))
        self.assertEqual( min(self.myList), 1 )

    def tearDown(self):
        print('in {} - tearDown()'.format(self.id()))


if __name__ == '__main__':
    unittest.main()