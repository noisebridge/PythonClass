"""
Goal: Import all csv files, recursively, in the data directory and export
them to the mysqlite database in the market orders table.

The database format requires me to hardcode the database table into the SQL string.
"""
import csv
import sqlite3

dbdir = "db/"
sqlite_filename = dbdir + 'EVEumm.sqlite'

expected_headers = ['price', 'volRemaining', 'typeID', 'range', 'orderID', 'volEntered', 'minVolume', 'bid', 'issueDate', 'duration', 'stationID', 'regionID', 'solarSystemID', 'jumps', '']

csvdir = 'Marketlogs/'


def import_csv_data(csvfile):
    """ Import csv tables and pass them back.

    """

    data = list()
    with open(csvfile, 'r') as f:
        for row in csv.reader(f):
            data.append(row)

    # data_headers, data
    return data[0], data[1:]


def read_available_csv_filenames(csvdir):
    """ Find all csv files recursively in the target directory... read on...

    We have specified the extension 'txt' because eve exports market order
    files as CSV with the txt extension and it's not worth it to change this.

    """
    from os import walk

    extension = 'txt'

    csvfiles = list()
    for (dirpath, dirnames, filenames) in walk(csvdir):
        for filename in filenames:
            # This is the default extension for EVE market order exports.
            if type(filename) is str and filename[-3:] == extension:
                csvfiles.append(dirpath + '/' + filename)
    
    return csvfiles


if __name__ == '__main__':
    """
    
    """

    csvfiles = read_available_csv_filenames(csvdir) 
    
    for csvfile in csvfiles:
        data_headers, data = import_csv_data(csvfile)

        # sqlite3 executemany takes a list of tuples.
        datatuples = list()
        for datarow in data:
            sql_str_list = list()
            sql_str_list.extend(datarow[:-1])
            # Extend by none for the primary key row. It needs 'null'.
            sql_str_list.append(None)
            # Last value is empty for some reason, the header doesn't have anything.
            datatuples.append(tuple(sql_str_list))

        # DB connection per file.
        conn = sqlite3.connect(sqlite_filename)
        c = conn.cursor()
        c.executemany('INSERT INTO mktOrder VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', datatuples)
        conn.commit()
        conn.close()


