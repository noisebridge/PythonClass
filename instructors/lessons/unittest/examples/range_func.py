
def dummy_range_function(param):
    ls = list()
    for num in range(param):
        ls.append(num)
    return ls

def range_func2(param):
    ls = list()
    start = 0
    while start < param:
        ls.append(start)
        start += 1
    return ls

#print dummy_range_function(5)

#print range_func2(5)