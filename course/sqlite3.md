### Database Applications ###

A 'database' can be any collection of data in a structured format.  When people talk about databases in programming, they usually mean a system which lets you as the developer define a 'schema' for a dataset - a way to describe how to store data as a set of tables, each of which contains rows and columns.

Data itself can be any type of information we can extract structure from.  It could be a list of registered users for a website, so that we can provide them with user accounts.  Or it could be a set of products, prices, and categories (perhaps with one table for each?).

Good schema design generally reduces 'duplication' of information between tables - reducing duplication is called 'normalization'.

Once a schema is created, we can start to populate the tables with data.  You can think of each table as being like a sheet in a spreadsheet - for example, here's what a snippet of a noisebridge 'events' table might look like:


| class_id | name | hyperlink |
| ------- | ------------ | ----- |
| 1 | CircuitHackingMondays | https://www.noisebridge.net/wiki/Circuit_Hacking_Monday |
| 2 | PythonClass | https://github.com/noisebridge/PythonClass |
| ... | ... | ... |

Defining the schema, populating the tables with data, and accessing data from table(s) is all achieved using a standard language called 'Structured Query Language' - commonly abbreviated as 'SQL'.


### The 'SQLite' Relational Database Format

There are numerous database systems available - some open source, some commercial - and most of them could easily handle storing the data shown above.  In this class, we'll use a system called 'SQLite', which is available for free and provides read & write access to databases stored as single files on disk.

Many other database servers - such as PostgreSQL or Microsoft SQL Server - require you to run a 'server' which provides access to your database over the network.  SQLite is in some ways easier, since we can read and write from the database within a single program; we'll be using Python programs to do exactly this.  After a program exits, the database remains as-is until another program runs and modifies or accesses it.

>SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. **It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.** It provides a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](http://www.python.org/dev/peps/pep-0249)." - from [The Python 'sqlite3' Module](https://docs.python.org/2/library/sqlite3.html)

Let's install SQLite before we get started with some practical examples.

- On OSX with Homebrew, type `brew install sqlite`
- On Debian/Ubuntu or similar Linux distributions, type `apt-get install sqlite`
- For Centos/Fedora, use `yum install sqlite`
- For anything else, ask the instructor :)

1. ##### Today's deep dive: Create a [database schema](https://www.sqlite.org/lang.html).

    1. Definitions:
        1. Table - similar to an excel spreadsheet, it is a collection of rows and columns.
            1. Each column has a `name` and `the same data type for each value` in the column.
            2. Each row has one field per column.
        2. Schema - A schema describes the layout and columns for the tables in a database
        3. Database - The on-disk representation of tables and other objects ('views', 'functions', ...)
    2. Type this code into a file, `users_schema.sql`:

        ```
        CREATE TABLE IF NOT EXISTS "users" ( 
            "pKey" INTEGER PRIMARY KEY,
            "username" varchar(255) DEFAULT NULL, 
            "age" INT DEFAULT NULL,
            "first_name" varchar(255) DEFAULT NULL,
            "last_name" varchar(255) DEFAULT NULL,
            "fav_color" varchar(255) DEFAULT NULL
        );
        ```
        - Take a moment to think about what this code is doing and what it represents
        - Ask questions if anything seems unclear!
        - Once you understand, feel free to continue on with the next few steps
       
    3. Now that we have a schema, let's create the SQLite database on disk.  Run `sqlite3`.  You should see something like:
        ```
        SQLite version 3.8.5 2014-08-15 22:37:57
        Enter ".help" for usage hints.
        Connected to a transient in-memory database.
        Use ".open FILENAME" to reopen on a persistent database.
        sqlite>
        ```
        
    4. Create a 'persistent' (saved) database on disk, by typing `.open users.db` to create a database named `users.db`
        ```
        sqlite> .open users.db
        sqlite>
        ```
        - You should see a new file called 'users.db' appear in your working directory
        - This is our (currently empty) database, and no schema has yet been specified for it
        
    5. Now we can apply our database schema by reading and executing our schema file:
        ```
        sqlite> .read users_schema.sql
        sqlite>
        ```
    

2. ##### Interacting with our database in Python.

    In this section, we will use Python's [sqlite3 module](https://docs.python.org/2/library/sqlite3.html) to communicate with our database.
    
    1. Goals: *read* from the database, *write* to the database, *see* our work in the sqlite3 CLI.

        1. Write Data:
            ```python
            # Import the database access library
            import sqlite3

            FILENAME = "users.db"
            TABLE_NAME = "users"

            # some default users
            JENNY_DATA = [None, 'jennymc', '30', 'jenny', 'mccloud', 'blue']
            JOE_DATA = [None, 'joewilson', '30', 'joe', 'wilson', 'yellow']

            # Create a connection to the database
            with sqlite3.connect(FILENAME) as conn:

                # We will use the cursor object to perform transactions.
                c = conn.cursor()

                # we can use {table} with the string function "format"
                # more here: https://docs.python.org/2/library/string.html#format-string-syntax
                INSERT_STATEMENT = "INSERT INTO {table} VALUES (?,?,?,?,?,?)" \
                                   .format(table=TABLE_NAME)

                # execute the insert transaction 
                # TODAY: add the correct variables for MY_LIST_X
                # OPTIONAL: try `execute many`
                c.execute(INSERT_STATEMENT, JENNY_DATA)
                c.execute(INSERT_STATEMENT, JOE_DATA)
            ```

        2. Read Data: add this after the cursor is established. Comment out the lines similar to `c.execute(INSERT_STATEMENT, SAMPLE_DATA)` for now.

            ```python
            SELECT_STATEMENT = "SELECT * FROM {table}".format(table=TABLE_NAME)
            c.execute(SELECT_STATEMENT)
            print c.fetchone()
            print c.fetchone()
            print c.fetchone()
            # print c.fetchall()  # try this with fetchone commented out.

            # retool this select statement to accomodate WHERE for sides < 4
            # hint: you must make a new SELECT statement.
            
            # tuples can be messy to work with - can you figure out how to
            # get the column names for each of the values we fetch?
            ```

        3. See our work:
            ```
            sqlite> .open users.db
            sqlite> .schema
            sqlite> select * from users;
            sqlite> ^D
            ```

3. #### Extended Resources - An overview of SQL
    1. [What's SQL?](http://en.wikipedia.org/wiki/SQL) - "SQL (Structured Query Language) is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS).
    2. [RDBMS](http://en.wikipedia.org/wiki/Relational_database_management_system) - "A relational database management system (RDBMS) is a database management system (DBMS) that is based on the relational model."

    3. [DBMS](http://en.wikipedia.org/wiki/Database) - Database management systems (DBMSs) are computer software applications that interact with the user, other applications, and the database itself to capture and analyze data. A general-purpose DBMS is designed to allow the definition, creation, querying, update, and administration of databases.
    4. [Relational Model](http://en.wikipedia.org/wiki/Relational_model) - Most relational databases use the SQL data definition and query language; these systems implement what can be regarded as an engineering approximation to the relational model. A table in an SQL database schema corresponds to a predicate variable; the contents of a table to a relation; key constraints, other constraints, and SQL queries correspond to predicates. However, SQL databases deviate from the relational model in many details, and Codd fiercely argued against deviations that compromise the original principles.
