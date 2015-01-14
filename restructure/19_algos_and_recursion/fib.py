


#add all numbers greater than zero but less than any given number together
def sum_of_num(num):
    the_sum = 0
    for i in range(1, num+1):
        the_sum += i 
    return the_sum
##########
import time

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()
   return theSum,end-start
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000))
######

def sum_of_num2(num):
    return sum([i for i in range(1, num+1)])

def sum_of_num3(n):
    return (n*(n+1))/2

print "sum"
print sum_of_num(4)
print sum_of_num2(4)
print sum_of_num3(4)

#recursive
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print "recursive list sum"
print(listsum([1,3,5,7,9]))




#
def fib(num):
    print(num)
    if num < 2:
        return num 
    else: 
        return fib(num-1) + fib(num-2)

print fib(10)

