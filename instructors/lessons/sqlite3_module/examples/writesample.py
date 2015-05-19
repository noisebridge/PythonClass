"""
Write a sample directly from a Python list of lists.
"""
import sqlite3

dbdir = "db/"

sql_filename = 'sampledb.sqlite'

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


