import unittest

from calculate_mortgage import calculate_monthly_payment


class TestMortgateCalculator(unittest.TestCase):
    def test_calculate_monthly_payment(self):
        monthly_payment = calculate_monthly_payment(
            principal=1_000_000,
            rate_percent=1,
            mortgage_years=1/12
        )

        self.assertEqual(monthly_payment, 1_000_000)


if __name__ == '__main__':
    unittest.main()
