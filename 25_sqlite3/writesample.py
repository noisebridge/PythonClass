"""
Write a sample directly from a Python list of lists.
"""
import sqlite3

dbdir = "./"

sql_filename = 'sampledb.sqlite'

sqlite_fileandpath = dbdir + sql_filename

sample_data_list_of_lists = [

    []
    []


        ]

if __name__ == '__main__':
    """
    
    """

    for datarow in sample_data_list_of_lists:

        # Extend data by Python's None object for the primary key row. It needs 'null'.
        datarow.append(None)

        # DB connection per file.
        conn = sqlite3.connect(sqlite_filename)
        
        c = conn.cursor()

        c.executemany('INSERT INTO mktOrder VALUES (?,?,?,?,?,?,?,?)', datatuples)

        conn.commit()

        conn.close()


