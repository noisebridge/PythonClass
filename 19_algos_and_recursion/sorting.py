#remember this assumes an already sorted data structure, we are merely searching!
def binary_search(alist, item):
    """list -> bool
    binary search using a while loop
    """

    first = 0 
    last = len(alist) - 1
    found = False

    while first<=last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True 
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1 
    return found


#remember this assumes an already sorted data structure, we are merely searching!
def binary_search2(alist, item):
        """list -> bool
        binary search using a while loop
        """
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist) // 2
            if alist[midpoint]==item:
              return True
            else:
              if item<alist[midpoint]:
                return binary_search(alist[:midpoint], item)
              else:
                return binary_search(alist[midpoint+1:], item)



#print section
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print("binary search for 1")
print(binary_search(testlist, 8))
print("binary search for 2")
print(binary_search2(testlist, 8))






#change names to make more readable and understandable
psuedo_code = """
If the list is empty or has one item, it is sorted by definition. 
This is our base case. 

"""

###
print "merge sort"
def merge_sort(alist):
    """list -> list 
    sorted from least to greatest
    """

    print("Splitting ", alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        #helper print statement
        print("Merging ", alist)

    return alist

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)