"""
Write a sample directly from a Python list of lists.
"""
import sqlite3

dbdir = "data/"

sql_filename = 'craigslistdata.sqlite'

sqlite_fileandpath = dbdir + sql_filename

sample_data_list_of_lists = [

    [   'pencil',
        'A pencil is used to write using lead and typically has an eraser.',
        '5',
        'grams',
        '3',
        'ounces',
        '01-01-15' 
    ],
    [   'pen',
        'A pen is used to write using ink.',
        '3',
        'grams',
        '3',
        'ounces',
        '01-01-15' 
    ]
]

if __name__ == '__main__':
    """
    
    """

    for datarow in sample_data_list_of_lists:

        # Extend data by Python's None object for the primary key row. It needs 'null'.
        datarow.append(None)

        # DB connection per file.
        conn = sqlite3.connect(sqlite_fileandpath)
        
        c = conn.cursor()

        c.execute('INSERT INTO OfficeSupplies VALUES (?,?,?,?,?,?,?,?)', tuple(datarow))

        conn.commit()

        conn.close()


"""

"""
import sqlite3

dbdir = "db/"

sql_filename = 'sampledb.sqlite'

sqlite_fileandpath = dbdir + sql_filename

if __name__ == '__main__':

    # DB connection per file.
    conn = sqlite3.connect(sqlite_fileandpath)

    # return bytestrings instead of unicode
    # https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.text_factory
    conn.text_factory = str

    c = conn.cursor()
    
    c.execute("SELECT * from OfficeSupplies;")

    result_list = c.fetchall()

    conn.close()

    # This is returned as a list of tuples, howeever SQL specifies a row as an 
    # unordered group of values defined by their attribute name (column heading).  
    # In this way, a SQL row is more like a set of key-value pairs. The keys are 
    # shared by all other rows in the group/table.

    for result in result_list:
        print result
