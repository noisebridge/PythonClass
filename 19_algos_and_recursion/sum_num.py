#better name for function would include describing
#we're finding the sum of all preceding numbers
#eg:
#def sum_prec_nums(num):




import time

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
    return sum(range(num+1)), time.time() - start

def sum_of_num4_time(num):
    start = time.time()
    return (num * (num+1) ) / 2, time.time() - start



print "sum timed:\n"

print "first"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num_time(10000))

print "\n\nsecond"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num2_time(10000))

print "\n\nthird"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num3_time(10000))

print "\n\nfourth"
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_num4_time(10000))



print "\n remember: 'pre-optimization is the root of all evil' - Knuth\n"

























#if you can figure out how to time this, KUDOS!!
def list_sum(num):
   #print "numList", numList
   start = time.time()
   numList = range(num)
    

   if len(numList) == 1:
        print "time taken %10.7f" %(time.time() - start)
        return numList[0]
   else:
        print numList[0], "and the rest", numList[1:]

        #what is happening with this return statement?
        return numList[0] + list_sum(numList[1:]) 

print "\n\nrecursive"
#for i in range(5):
#    print("Sum is %d required %10.7f seconds"%list_sum(10000))