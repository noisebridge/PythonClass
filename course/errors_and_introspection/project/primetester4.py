"""
For any given number, we only need to test the primes below it.

e.g. 9 -- we need only test 1,2,3,5,7

e.g. 8 -- we need only test 1,2,3,5,7

for example, the number 12 has factors 1,2,3,6,12.
We could find the six factor but we will find the two factor first.

The definition of a composite number is that it is composed of primes, therefore it will always have a prime as a factor.

This prime test should have an index of all primes below i.
"""

total_range = 1000
primes = list()

def prime_test(i):
    """
    Cases:
    Return False if i is not prime
    Return True if i is prime

    Caveat: cannot test 1.
    Caveat 2: Cannot test 2.
    It is fortuitous that these tests both return true.
    """
    for possible_factor in primes:
        if i % possible_factor == 0:
            return False

    return True


for prime in range(2,total_range):
    import timeit
    # This isn't good enough, we'll have to use a context
    # manager or something to set up and tear down the right
    # prime list and current integer to test.
    setup = "from __main__ import prime_test"
    print(timeit.timeit("is_prime = prime_test(prime)", number=1, setup=setup))
    if is_prime:
        primes.append(prime)

print len(primes)


