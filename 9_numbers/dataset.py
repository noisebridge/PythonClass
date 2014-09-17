
import numpy

data1 = []
data2 = []

i = 9
j = 19

for val in range(100):
    data1.append(val*i)
    data2.append(val*j)

print len(data1), data1
print len(data2), data2

nd_arr1 = numpy.array(zip(data1,data2))

