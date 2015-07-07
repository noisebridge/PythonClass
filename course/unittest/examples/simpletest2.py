"""
"""

mytestconditions = [ ([1,2],3), ([2,4],6), ([3,6],9) ]

def sum_my_list(mylist):

    myresult = 0
    for item in mylist:
        myresult += item

    return myresult

try:
    for condition, result in mytestconditions:
        # check that the conditions produce the result
        assert sum_my_list(condition) == result
        print "Passed"
except AssertionError:
    print "Failed"
