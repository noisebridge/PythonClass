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


1. #### Examining our raw data

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
