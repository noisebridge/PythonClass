
import csv

mode = 'r'
filename = 'ngsl1.01.csv'

with open(filename, mode) as f:
    words = csv.reader(f)

    for row in words:
        print row


