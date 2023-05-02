import csv
import psycopg2

# Open the data file
f = open('data/airports.dat')
reader = csv.reader(f)

# Read each line in the data file
records = []
for row in reader:
    id, name, city, country, iata, icao, latitude, longitude = row[0:8]
    record = {
        'id': id,
        'name': name,
        'city': city,
        'country': country,
        'iata': iata,
        'icao': icao,
        'latitude': latitude,
        'longitude': longitude,
    }
    records.append(record)


# Open a database connection
conn = psycopg2.connect('')
cursor = conn.cursor()

# Clear the existing entries
cursor.execute('delete from airports')

# Build and execute our insert statement
statement = '''
    insert into airports (id, name, city, country, iata, icao, latitude, longitude)
    values (%(id)s, %(name)s, %(city)s, %(country)s, %(iata)s, %(icao)s, %(latitude)s, %(longitude)s);
'''
cursor.executemany(statement, records)

# Commit and close the database connection
conn.commit()
conn.close()
