def multiply(a, b, c):
    """Multiplies three values and returns the result."""
    return a * b * c


def present_value(payment, rate, years):
    """Calculates the present value of a series of future payments."""
    pv = 0
    for t in range(1, years * 12 + 1):
        pv += payment / ((1 + rate / 100 / 12) ** t)
    return pv

monthly_payment = 450
annual_rate = 8
total_years = 20

pv_result = present_value(monthly_payment, annual_rate, total_years)
print(pv_result)

result = multiply(9, 8, 7)
print(result)
