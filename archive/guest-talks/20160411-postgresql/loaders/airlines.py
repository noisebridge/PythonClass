import csv
import psycopg2

# Open the data file
f = open('data/airlines.dat')
reader = csv.reader(f)

# Read each line in the data file
records = []
for row in reader:
    id, name, alias, iata, icao, callsign, country, active = row
    if len(iata) > 2:
        continue

    record = {
        'id': id,
        'name': name,
        'iata': iata,
        'icao': icao,
        'country': country,
        'active': active == 'Y',
    }
    records.append(record)


# Open a database connection
conn = psycopg2.connect('')
cursor = conn.cursor()

# Clear the existing entries
cursor.execute('delete from airlines')

# Build and execute our insert statement
statement = '''
    insert into airlines (id, name, iata, icao, country, active)
    values (%(id)s, %(name)s, %(iata)s, %(icao)s, %(country)s, %(active)s);
'''
cursor.executemany(statement, records)

# Commit and close the database connection
conn.commit()
conn.close()
