"""

"""
import sqlite3

dbdir = "./"

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

    print result_list
