import unittest

from calculate_mortgage import calculate_monthly_payment


class TestMortgateCalculator(unittest.TestCase):
    def test_calculate_short_term(self):
        monthly_payment = calculate_monthly_payment(
            principal=1_000_000,
            rate_percent=1,
            mortgage_years=10
        )

        self.assertAlmostEqual(monthly_payment, 8760, 0)

    def test_calculate_long_term(self):
        monthly_payment = calculate_monthly_payment(
            principal=500_000,
            rate_percent=1,
            mortgage_years=20
        )

        self.assertEqual(monthly_payment, 2299.47)

if __name__ == '__main__':
    unittest.main()
