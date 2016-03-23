'''rough benchmarking to illustrate how much the runtime of a generator expression
is less than a different type of sequence'''

import time

start_rr = time.time()
reg_range = range(50000000)
print reg_range[100000] #access an object in our container for measuring
end_rr = time.time() 

print "regular list - start: {0}, end: {1}, diff: {2}".format(start_rr, end_rr, end_rr-start_rr)

start_xr = time.time()
x_range = xrange(50000000)
#after creation we have to access, this is because of a gen's lazy nature
print x_range[100000]
end_xr = time.time() 

print "generator - start: {0}, end: {1}, diff: {2}".format(start_xr, end_xr, end_xr-start_xr)
