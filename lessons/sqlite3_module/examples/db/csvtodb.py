import sqlite3
import csv
import logging

dbstring = "square.db"

conn = sqlite3.connect(dbstring)

cur = conn.cursor()

insert = 'INSERT INTO squares VALUES ({},{})'

with open("pairs.csv", "r") as csvfile:
    pairs = csv.reader(csvfile)
    for pair in pairs:
        try:
            intpair = (int(pair[0]),int(pair[1]))
        except ValueError as e:
            raise e, "Not an integer"

        cur.execute(insert)
        
conn.commit()
conn.close()
