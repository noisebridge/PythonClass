dummy = 888

test_num = 10
print id(test_num)

result = 1000
print "id result", id(result)

def mult_num_by_test_num(num):
    print id(test_num)
    print "id num", id(num)
    result = test_num * num
    print "id result", id(result)
    print "dummy", dummy
    return result

print test_num

another_num = 44
test_num = mult_num_by_test_num(another_num)

print test_num 
print id(test_num)

