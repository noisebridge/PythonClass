"""
messages ascii codes can only include: 20,21,32,39-41,44-46,48-59,63,65-90,97-122
encrypt includes 3 ascii codes in range of: 97-122
"""


def isValid(arr, key):
    dec = map(lambda x, y: x^y, arr, key)
    for e in dec:
        # note: there may be a nicer way to encapsulate this query in
        # a data structure
        if (e < 20) or (e > 21 and e < 32) or (e>32 and e<39) or (e>41 and e<44) \
        or (e==47) or (e>59 and e<63) or (e==64) or (e>90 and e<97) or (e > 122) :
            #print 'fail: ',arr,' XOR ',key,' = ',dec
            return False
    return True

inFilename = 'test_data.txt'
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
                if not isValid(tmpMsg, tmpKey):
                    valid = False
                    break
            if valid:
                print chr(a) + chr(b) + chr(c)
                quit()
