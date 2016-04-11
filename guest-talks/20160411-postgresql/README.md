### PostgreSQL with Python

PostgreSQL is a powerful and mature open source database system which anyone
can download and use.  It has an extensive feature set and can be used easily
from Python.


## Installing PostgreSQL

If you'd like to run PostgreSQL on your own machine during this class, the
recommended way to install it is to visit http://www.postgresql.org/download
and follow the installation instructions for your OS/distribution.

Alternatively you may ask to connect to a shared instance that the instructor
will be running during the class, or use a free hosted instance of PostgreSQL,
such as the ones provided by Heroku or ElephantSQL.


## OpenFlights

OpenFlights is an open data set of airlines, airports, and the routes which
airlines operate between those airports.  We'll be using it as an example of a
dataset we can load into PostgreSQL and then run queries against.


1. ##### Examining our raw data

The data directory contains three files downloaded from OpenFlights:

* airlines.dat - a list of airlines

```
324,"All Nippon Airways","ANA All Nippon Airways","NH","ANA","ALL NIPPON","Japan","Y"
412,"Aerolineas Argentinas",\N,"AR","ARG","ARGENTINA","Argentina","Y"
413,"Arrowhead Airways",\N,"","ARH","ARROWHEAD","United States","N"
```

* airports.dat - airports around the world (with identifying codes)

```
507,"Heathrow","London","United Kingdom","LHR","EGLL",51.4775,-0.461389,83,0,"E","Europe/London"
26,"Kugaaruk","Pelly Bay","Canada","YBB","CYBB",68.534444,-89.808056,56,-7,"A","America/Edmonton"
3127,"Pokhara","Pokhara","Nepal","PKR","VNPK",28.200881,83.982056,2712,5.75,"N","Asia/Katmandu"
```

* routes.dat - routes operated by airlines between origin/destination airports

```
BA,1355,SIN,3316,LHR,507,,0,744 777
BA,1355,SIN,3316,MEL,3339,Y,0,744
TOM,5013,ACE,1055,BFS,465,,0,320
```

2. ##### Creating an appropriate schema

In the SQL language, before loading data into a database, you should first
define a schema - this tells the database which tables of data we will collect,
what columns those tables will have, and what values we'll allow for each row
in each table.

Let's aim to import a subset of the fields available - we should aim to build
our tools in a way that we can always add other fields later if they become
relevant.

Here's a suggested schema in SQL:

```
drop table airlines if exists;
create table airlines
(
    id int,
    name text,
    iata char(2),
    icao char(3),
    country text,
    active boolean,

    primary key (id)
);

drop table airports if exists;
create table airports
(
    id int,
    name text,
    city text,
    country text,
    iata char(3),
    icao char(4),
    latitude float,
    longitude float,

    primary key (id)
);

drop table routes if exists;
create table routes
(
    airline_id int,
    from_airport_id int,
    to_airport_id int,
    equipment char(3),

    primary key (airline_id, from_airport_id, to_airport_id)
);
```

This schema is available in `schema/openflights.sql`, and we can use that to
create our schema:

```
psql -f schema/openflights.sql
```

3. ##### Loading data into our database

Now let's use Python's support for reading CSV files to load the raw data
from OpenFlights into our PostgreSQL database tables one by one.

See the loader code in:

```
loaders/airlines.py
loaders/airports.py
loaders/routes.py
```

4. ##### Making it easier to query our routes

The output from our routes table is hard to read:

```
# select * from routes limit 5;
 airline_id | from_airport_id | to_airport_id | equipment
------------+-----------------+---------------+-----------
        410 |            2965 |          2990 | CR2
        410 |            2966 |          2990 | CR2
        410 |            2966 |          2962 | CR2
        410 |            2968 |          2990 | CR2
        410 |            2968 |          4078 | CR2
(5 rows)
```

We can use a SQL 'view' to make this more readable:

```
create view routes_view as
select
    a.name,
    a.iata as airline_iata,
    f.iata as from_iata,
    f.country as from_country,
    t.iata as to_iata,
    t.country as to_country,
    r.equipment
from routes as r
join airlines as a on a.id = r.airline_id
join airports as f on f.id = r.from_airport_id
join airports as t on t.id = r.to_airport_id
```
