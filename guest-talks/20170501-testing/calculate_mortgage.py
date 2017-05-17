def calculate_monthly_payment(principal, rate_percent, mortgage_years):
    if round(rate_percent, 8) == 0:
        return principal / (mortgage_years * 12)

    rate = rate_percent / 12 / 100
    escalator = 1 + rate
    n_payments = mortgage_years * 12

    return round((
        principal * rate * escalator ** n_payments
    ) / (escalator ** n_payments - 1), 2)


def calculate_total_payments(principal, rate_percent, mortgage_years):
    return calculate_monthly_payment(principal, rate_percent, mortgage_years) * mortgage_years * 12
