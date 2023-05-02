"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a<995
b<996
c<997

They tell us there is only one, so we only need to test for existence, not uniqueness.

We have 2 equations:
a2+b2=c2
a+b+c=1000

"""

# Lets test all three cases for all numbers until we get the answer.
# The problem told us it was unique, so we can exit.
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a<b<c and a+b+c==1000 and a**2+b**2==c**2:
                print("answer:", a*b*c)
                exit(0)

