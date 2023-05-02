from calculate_mortgage import (
    calculate_monthly_payment,
    calculate_total_payments
)

def test_monthly_payment():
    monthly_payment = calculate_monthly_payment(
        principal=1_000_000,
        rate_percent=1,
        mortgage_years=10
    )

    assert monthly_payment == 8760.41


def test_total_payments():
    total = calculate_total_payments(
        principal=1_000_000,
        rate_percent=1,
        mortgage_years=30
    )

    assert total == 1157904
