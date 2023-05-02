

def prime_test(i, j=2):
    """
    Cases:
    Return False if i is not prime
    Return True if i is prime

    Caveat: cannot test 1.
    Caveat 2: Cannot test 2.
    It is fortuitous that these tests both return true.
    """
    if j >= i: # i used greater than to cover 1
        return True
    if i % j == 0: # this chokes on 1 % 2
        return False
    
    return prime_test(i, j+1)

for number in range(1,50):
    if prime_test(number) == True:
        print number


