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

# Count all lists of 3 numbers where a < b < c
# We optimized this twice, starting with the full range of a,b,c
# Then we iteratively pulled the three if conditions a<b<c, a^2+b^2==c^2, a+b+c=1000 into the
# control structures of the code, significantly reducing the range of each a,b,c tested.
# Really great example about optimizing code and pulling special conditions into the control structure
# of the application.
for a in range(1,1000):
    for b in range(a+1,1000):
        c = 1000 - (a+b)
        if c > 0 and a**2+b**2==c**2:
            print("answer:", a*b*c)
            exit(0)

