psuedo_code = """
If the list is empty or has one item, it is sorted by definition. 
This is our base case. 

"""

###
print "merge sort"
count = 0

def merge_sort(alist):
    """list -> list 
    sorted from least to greatest
    """

    #print("Splitting ", alist)
    global count 

    #splitting list section 
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        #merging splices section
        i=0 #should be called first_value
        j=0 #should be called second_value
        k=0 #rebuilding list


        while i<len(lefthalf) and j<len(righthalf):
            count += 1
            if lefthalf[i]<righthalf[j]:
                
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            print "alist[k]", alist[k]
            k=k+1

        while i<len(lefthalf):
            count += 1
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            count += 1
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        #helper print statement
        #print("Merging ", alist)

    return alist, count



alist = [18, 18, 12, 12, 3, 1, 2, 10, 13, 17]
ls2 = range(20,10,-1)
#merge_sort(alist)

merge_sort(ls2)

#print(alist)
print("iterations {}".format(count))