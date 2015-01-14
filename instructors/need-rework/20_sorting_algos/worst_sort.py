ls = [18, 18, 12, 12, 3, 1, 2, 10, 13, 17]

ls2 = range(20,10,-1)


"""iterate over list, comparing each element with element
with index 1 greater and switch"""

def worst_sort(ls):
    for iters in range(len(ls)-1):

        for i in range(len(ls)-1):
            print ls 
            if ls[i] >= ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp

    return ls

print ls
#print worst_sort(ls)
print worst_sort(ls2)

