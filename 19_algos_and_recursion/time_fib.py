import time


#add all numbers greater than zero but less than any given number together
def sum_of_num(num):
    the_sum = 0
    for i in range(1, num+1):
        the_sum += i 
    return the_sum

def sum_of_num2(num):
    return sum([i for i in range(1, num+1)])

def sum_of_num3(num):
    return (num * (num+1) ) / 2

print "sum"
print sum_of_num(4)
print sum_of_num2(4)
print sum_of_num3(4)

def sum_of_num_time(num):
    start = time.time()
    the_sum = 0
    for i in range(1, num+1):
        the_sum += i 
    end = time.time()
    return the_sum, end - start

def sum_of_num2_time(num):
    start = time.time()
    return sum([i for i in range(1, num+1)]), time.time() - start

def sum_of_num3_time(num):
    start = time.time()
    return (num * (num+1) ) / 2, time.time() - start

print "sum timed"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num_time(10000))

print "\n\n"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num2_time(10000))

print "\n\n"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num3_time(10000))




#recursive sumlist
def list_sum(numList):
   print "numList", numList
   start = time.time()
   #, time.time() - start

   if len(numList) == 1:
        return numList[0]
   else:
        print numList[0], "and the rest", numList[1:]

        #what is happening with this return statement?
        return numList[0] + list_sum(numList[1:]) 

print "\n\n"
print "recursive list sum"
print(list_sum([1,3,5,7,9]))

print "\n\n"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%list_sum(10000))





#fibonacci!
def fib(num):
    print(num)
    if num < 2:
        return num 
    else: 
        return fib(num-1) + fib(num-2)

print fib(10)

