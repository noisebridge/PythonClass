
### [sqlite3: The Python 2 Module](https://docs.python.org/2/library/sqlite3.html)



##### First, an excerpt from the Python 2 docs:

"SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. **It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.**

It provides a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](http://www.python.org/dev/peps/pep-0249)."

### 1. Basic Setup
- [Install sqlite](http://www.sqlite.org/quickstart.html)
- [sqlite Documentation](http://www.sqlite.org/docs.html)
- Create a database: [use these schema](https://github.com/PyClass/PyClass-lesson-plans/tree/master/25_sqlite3/db). First build the physics database, then build the sampledb database.
- Write to DB: Run [this](https://github.com/PyClass/PyClass-lesson-plans/blob/master/25_sqlite3/readsample.py) to add some sample entries.
- Read from DB: Inside the sqlite shell, execute `SELECT * FROM OfficeSupplies;` to see all entries.


### 2. Working with the sample databases
- An outline of our Python goals: make database connection, write or read entries, commit changes, close connection.
- First lets [read it](https://github.com/PyClass/PyClass-lesson-plans/blob/master/25_sqlite3/readsample.py) into a list of tuples. This is the default data structure returned by sqlite3.
- Now lets [write some data, note that we let the db assign the pkey](https://github.com/PyClass/PyClass-lesson-plans/blob/master/25_sqlite3/writesample.py).
- Most basic uses will be a variation on this.
- A word of caution: sqlite is best for single-user applications.  If you need to allow many users, like with a web app, swap over to Postgres.
- You can convert to Postgres, and TONS of your knowledge is transferrable, so just use sqlite3 for now and that knowledge will transfer!


### 3. Organizing Data
- Data will often need reorganized. Organize data based on how it will be used and avoid when you can.
- Relational Databases aren't particularly clever. They are typically 2d tables (rows and columns). This is usually a very good thing.
- Most of the time you are going to be using a variation of a Python list or a dictionary.
- List: Ordered, but no 'metadata' describing what is ordered.
- Dict: Everything has a unique 'hash' which can be considered metadata, but there is no inherent order.


#### Addendum: An overview of technologies:

1. SQL Databases: Disambiguation
  - [What's SQL?](http://en.wikipedia.org/wiki/SQL) - "SQL (Structured Query Language) is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS).

2. [RDBMS](http://en.wikipedia.org/wiki/Relational_database_management_system) - "A relational database management system (RDBMS) is a database management system (DBMS) that is based on the relational model."
  - [DBMS](http://en.wikipedia.org/wiki/Database) - Database management systems (DBMSs) are computer software applications that interact with the user, other applications, and the database itself to capture and analyze data. A general-purpose DBMS is designed to allow the definition, creation, querying, update, and administration of databases.
  - [Relational Model](http://en.wikipedia.org/wiki/Relational_model) - Most relational databases use the SQL data definition and query language; these systems implement what can be regarded as an engineering approximation to the relational model. A table in an SQL database schema corresponds to a predicate variable; the contents of a table to a relation; key constraints, other constraints, and SQL queries correspond to predicates. However, SQL databases deviate from the relational model in many details, and Codd fiercely argued against deviations that compromise the original principles.


### TODO: DELETE WHEN COMPLETE
  - Links below go to proper examples in folder.
  - Discuss autocommmit, manual commit, buffered? commits (with example)
  - Creating functions in queries: https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.create_function
  - Everything after functions: aggregates, collations, row factories, text factories, row objects, and the rest of that section.
  - Try to remove this from the code: explain why you have to specify str. That still isn't clear to me... 
  - row.keys() <-- get keys/headers for table
  - SQLite and Python Types: https://docs.python.org/2/library/sqlite3.html#introduction
  - Dealing with Date: https://docs.python.org/2/library/sqlite3.html#default-adapters-and-converters
  - 
