import csv

tot = 100

def squareme(num):
    return num*num

list_of_pairs = []

for i in range(tot):
    list_of_pairs.append((i, squareme(i)))

with open('pairs.csv','w') as f:
    w = csv.writer(f)
    for row in list_of_pairs:
        w.writerow(row)

