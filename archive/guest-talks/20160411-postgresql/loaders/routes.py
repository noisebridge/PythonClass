import csv
import psycopg2

# Open the data file
f = open('data/routes.dat')
reader = csv.reader(f)

# Read each line in the data file
records = []
for row in reader:
    airline_id, from_airport_id, to_airport_id, equipment = \
        row[1], row[3], row[5], row[8]

    if not airline_id.isdigit():
        continue

    if not from_airport_id.isdigit():
        continue

    if not to_airport_id.isdigit():
        continue

    record = {
        'airline_id': airline_id,
        'from_airport_id': from_airport_id,
        'to_airport_id': to_airport_id,
        'equipment': equipment,
    }
    records.append(record)


# Open a database connection
conn = psycopg2.connect('')
cursor = conn.cursor()

# Clear the existing entries
cursor.execute('delete from routes')

# Build and execute our insert statement
statement = '''
    insert into routes (airline_id, from_airport_id, to_airport_id, equipment)
    values (%(airline_id)s, %(from_airport_id)s, %(to_airport_id)s, %(equipment)s);
'''
cursor.executemany(statement, records)

# Commit and close the database connection
conn.commit()
conn.close()
