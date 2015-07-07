"""
"""
#from listutils import sum_my_list
import listutils

mytestconditions = [ ([1,2],3), ([2,4],6), ([3,6],9) ]

try:
    for condition, result in mytestconditions:
        # check that the conditions produce the result
        assert listutils.sum_my_list(condition) == result
        print "Passed"
except AssertionError:
    print "Failed"
