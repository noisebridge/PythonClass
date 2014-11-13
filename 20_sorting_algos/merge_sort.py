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