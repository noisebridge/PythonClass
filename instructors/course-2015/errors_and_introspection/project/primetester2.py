

def prime_test(i):
    """
    Cases:
    Return False if i is not prime
    Return True if i is prime

    Caveat: cannot test 1.
    Caveat 2: Cannot test 2.
    It is fortuitous that these tests both return true.
    """
    for possible_factor in range(2,i):
        if i % possible_factor == 0:
            return False

    return True


for prime in range(2,50):
    print prime, prime_test(prime)





