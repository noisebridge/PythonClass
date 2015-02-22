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

# First optimization, we pull the test condition a<b<c into the control structure
# This is very helpful because instead of discarding many cases on test, we exclude
# them from the considered problem set.
for a in range(1,1000):
    for b in range(a+1,1000):
        for c in range(b+1,1000):
            if a+b+c==1000 and a**2+b**2==c**2:
                print("answer:", a*b*c)
                exit(0)

