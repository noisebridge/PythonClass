from calculate_mortgage import calculate_monthly_payment


def test_single_payment():
    monthly_payment = calculate_monthly_payment(
        principal=1_000_000,
        rate_percent=1,
        mortgage_years=1/12
    )

    assert monthly_payment == 1_000_000
