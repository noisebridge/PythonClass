import time


#recursive sumlist
def list_sum(numList):
   print "numList", numList
   start = time.time()
    

   if len(numList) == 1:
        print "time taken %10.7f" %(time.time() - start)
        return numList[0]
   else:
        print numList[0], "and the rest", numList[1:]

        #what is happening with this return statement?
        return numList[0] + list_sum(numList[1:]) 

print "\n\n"
print "recursive list sum"
print(list_sum(range(10)))

print "\n\n"
#for i in range(5):
 #   print("Sum is %d required %10.7f seconds"%list_sum(10000))













#fibonacci!  Solution
def fib(num):
    print(num)
    if num < 2:
        return num 
    else: 
        return fib(num-1) + fib(num-2)

print fib(10)

