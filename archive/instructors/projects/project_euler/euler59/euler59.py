"""
One solution for Problem 59 of Euler Project.

Original Stated Problem: https://projecteuler.net/problem=59
The file test_data.csv is downloaded from this original problem.  The file is
converted to a space separated file, which is used as the input to this script.

Solution is Compatible with: https://www.hackerrank.com/contests/projecteuler/challenges/euler059/
The file test_data2.txt is downloaded from this hackerrank problem.

Notes:
The original messages can only include ascii codes from this range:
32-33,39-41,44-46,48-59,63,65-90,97-122

The key only includes 3 ascii codes in range of: 97-122

This solution uses these above assumptions to perform a brute force search
for a key.

"""

inFilename = 'test_data.txt'

def isValidXor(arr, key):
    dec = map(lambda x, y: x ^ y, arr, key)
    for e in dec:
        # note: there may be a nicer way to encapsulate this query in
        # a data structure
        if e < 32 or (e > 33 and e < 39) or (e > 41 and e < 44) or e == 47 or \
           (e > 59 and e < 63) or e == 64 or (e > 90 and e < 97) or e > 122:
            return False
    return True

with open(inFilename, 'r') as f:
    N = int(f.readline())
    encMsg = [int(x) for x in f.readline().split()]

if N != len(encMsg):
    print N, '!=', len(encMsg), '!'
    quit()

# Brute force all possible ascii codes combinations
# for the 3 character key
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            valid = True
            key = [a, b, c]
            # print 'key=',key
            for i in range(0, N, 3):
                # create a temp msg and key so we can test the end of the list.
                # this allows us to test a 2 digit key or 1 digit key
                tmpMsg = encMsg[i:(i + 3)]
                tmpKey = key[0:len(tmpMsg)]
                if not isValidXor(tmpMsg, tmpKey):
                    valid = False
                    break
            if valid:
                # note: ascii codes can be converted to a character
                #       via the chr() command
                print 'found key: ', chr(a) + chr(b) + chr(c)
                print 'answer: ', a + b + c
                quit()

# the search ended with no results found.
print 'No answer found!'
