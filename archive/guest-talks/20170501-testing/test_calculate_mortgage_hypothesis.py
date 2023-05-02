from hypothesis import given
import hypothesis.strategies as st

from calculate_mortgage import calculate_monthly_payment


@given(st.floats(allow_nan=False, allow_infinity=False, min_value=100))
@given(st.floats(allow_nan=False, allow_infinity=False, min_value=0, max_value=100))
@given(st.integers(min_value=1, max_value=50))
def test_monthly_payment_does_not_exceed_principal(principal, rate_percent, mortgage_years):
    monthly_payment = calculate_monthly_payment(
        principal=principal,
        rate_percent=rate_percent,
        mortgage_years=mortgage_years
    )

    assert monthly_payment <= principal
