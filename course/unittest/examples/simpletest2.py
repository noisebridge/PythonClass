"""
"""

myconditions = [1,2]
myresult = 3

def sum_my_list(mylist):

    myresult = 0
    for item in mylist:
        myresult += item

    return myresult


assert sum_my_list(myconditions) == myresult
