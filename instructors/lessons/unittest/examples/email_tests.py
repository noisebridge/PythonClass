import unittest
from range_func import dummy_range_function, range_func2

class TestEmailFunctions(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEmailFunctions, self).__init__(*args, **kwargs)
        

    def setUp(self):  
        #self.ls = range(10)

        self.valid_email = "me@me.com"
        self.invalid_email1 = "evilperson.com"
        self.invalid_email2 = "person@evil"

        self.valid_user_domain = ".org"
        self.invalid_user_domain = ".evil"
        self.valid_domains = ['.net', '.com', '.org', '.edu', '.gov']

        self.valid_param = 10
        self.invalid_param = 20
        self.dummy_range_value = dummy_range_function(self.valid_param)
        self.dummy_range_value_bad = dummy_range_function(self.invalid_param)

        self.func2_value = range_func2(self.valid_param)
        self.func2_value_bad = range_func2(self.invalid_param)

    def test_exists(self):
        print(self.valid_email)
        self.assertIsNotNone(self.valid_email)

    def test_type_string(self):
        self.assertIsInstance(self.valid_email, str, msg="test for string type")

    def test_at_symbol(self):
        self.assertIn('@', self.valid_email, msg="there is an @ symbol in your address")

    def test_valid_domain(self):
        self.assertIn(self.valid_user_domain, self.valid_domains) 

    def test_not_valid_domain(self):
        self.assertNotIn(self.invalid_user_domain, self.valid_domains)  

    def test_dummy_range_works(self):
        self.assertEqual(range(10), self.dummy_range_value)

    def test_dummy_range_works_invalid(self):
        self.assertEqual(range(10), self.dummy_range_value_bad)

    def test_func2_works(self):
        self.assertEqual(range(10), self.func2_value)

    def test_func2_works_invalid(self):
        self.assertEqual(range(10), self.func2_value_bad)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite) 