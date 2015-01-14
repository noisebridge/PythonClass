"""
This is from: https://docs.python.org/2/library/decimal.html#module-decimal
"""

import decimal

D = decimal.Decimal # Optional / from FAQ https://docs.python.org/2/library/decimal.html#decimal-faq

D_prec = 6 # Lets start with a precision of 6

print
print "Set precision to 6 decimals."
decimal.getcontext().prec = D_prec

# Take advantage of our shortened syntax above.
x = D(1)
y = D(7)

# We need to use quantize for non-integer multiplication and division.
print "divide x/y:", (x/y).quantize(D(10)**-D_prec), " - type:", type(x/y)
print

TWOPLACES = D(10) ** -2
print "divide x/y, two-digit quantize:", (x/y).quantize(TWOPLACES), " - type:", type(x/y)

print
print "reset to default precision, 28 decimals."
D_prec = 28
decimal.getcontext().prec = D_prec

# quantize again. It is a method of any Decimal type number.
print "divide x/y:", (x/y).quantize(D(10)**-D_prec), " - type:", type(x/y)
print
