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
    
    # c.execute("select typeID from invTypes where typeName like ?", (typeName,) )

    c.execute("SELECT * from OfficeSupplies;")

    result_list = c.fetchall()

    conn.close()

    # This is returned as a list of tuples, howeever SQL specifies a row as an 
    # unordered group of values defined by their attribute name (column heading).  
    # In this way, a SQL row is more like a set of key-value pairs. The keys are 
    # shared by all other rows in the group/table.

    for result in result_list:
        print result
