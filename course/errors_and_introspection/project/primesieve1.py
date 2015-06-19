"""
Sieve of Erasmus - Prime Sieve

Goal: Find the first n primes

What we know:

    For a given integer, take every integer between 1 and itself.
    Test itself modulo that integer. If results is zero, then it is nonprime.
    If none of these modulo give zero, then it is prime.


"""

# range will include the first argument and the 2nd argument minus 1.
range_to_test_for_primes = range(1,50)


def is_prime_helper(i):
    """ Spitballing prime helpers
    """

    if i % (i-1) == 0:
        return False


def is_prime(i):
    """
    """
    
     

for x in range_to_test_for_primes:
    range_to_test = range(2,x)
    if x % 2 =! 0:
        

