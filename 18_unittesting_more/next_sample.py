import unittest

def setUpModule():

    print("in module {} - setUpModule()".format(__name__))

def tearDownModule():
    print("in module {} - tearDownModule()".format(__name__))

class TextFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('in class {} - setUpClass()'.format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        print('in class {} - tearDownClass()'.format(cls.__name__))

    def setUp(self):
        print('in setup()')

    def tearDown(self):
        print('in tearDown()')

    def test_1 (self):
        print('in test_1()')

    def test_2 (self):
        print('in test_2()')

if __name__ == '__main__':
    unittest.main()
