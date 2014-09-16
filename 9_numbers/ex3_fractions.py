"""
'A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.'
From Fractions - https://docs.python.org/2/library/fractions.html



"""
import decimal

import fractions

F = fractions.Fraction
D = decimal.Decimal

x = D(1)
y = D(7)

z = F.from_decimal(x/y)

print "Lets get an exact fraction of our decimal:", z
print "What type is the fraction?", type(z)
print "Weird, I expected 1/7."
den_limit = 100000
print "Limiting the denominator to %s." % den_limit, z.limit_denominator(max_denominator=den_limit)
print "Must have fixed a precision issue."
print

print "GCD of 9,6:", fractions.gcd(9,6)


