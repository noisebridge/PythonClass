### Database Applications ###

A 'database' can be any collection of data in a structured format.  When people talk about databases in programming, they usually mean a system which lets you as the developer define a 'schema' for a dataset - a way to describe how to store data as a set of tables, each of which contains rows and columns.

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
            "age" varchar(255) DEFAULT NULL,
            "first_name" varchar(255) DEFAULT NULL,
            "last_name" varchar(255) DEFAULT NULL,
            "fav_color" varchar(255) DEFAULT NULL
        );
        ```
    3. Now let's create a new SQLite database on disk.  Run `sqlite3`.  You should see something like:
        ```
        SQLite version 3.8.5 2014-08-15 22:37:57
        Enter ".help" for usage hints.
        Connected to a transient in-memory database.
        Use ".open FILENAME" to reopen on a persistent database.
        sqlite>
        ```
    4.
        This is prompting us for a command, and instructing us how to create a 'persistent' (saved) database, which is what we want.  Type `.open users.db` to create a database named `users.db`
        ```
        sqlite> .open users.db
        sqlite>
        ```
        
    5. Now we can create our users table by reading and executing our schema file:

        ```
        sqlite> .read users_schema.sql
        sqlite>
        ```
    

2. ##### Interacting with our database in Python.

    In this section, we will use Python's [sqlite3 module](https://docs.python.org/2/library/sqlite3.html) to communicate with our database.
    
    1. Goals: *read* from the database, *write* to the database, *see* our work in the sqlite3 CLI.

        1. Write Data:
            ```python
            """Write a sample directly from a Python list of lists.
            """
            import sqlite3

            FILENAME = "users.db"
            TABLE_NAME = "users"

            if __name__ == '__main__':
                """ Write some data to our database.
                """

                # some default users
                MY_LIST_1 = [None, 'jennymc', '30', 'jenny', 'mccloud', 'blue']
                MY_LIST_2 = [None, 'joewilson', '30', 'joe', 'wilson', 'yellow']

                # Create a connection to the database, assign to a name
                conn = sqlite3.connect(FILENAME)

                # We will use the cursor object to perform transactions.
                c = conn.cursor()

                # we can use {table} with the string function "format"
                # more here: https://docs.python.org/2/library/string.html#format-string-syntax
                INSERT_STATEMENT = "INSERT INTO {table} VALUES (?,?,?,?,?,?)"
                MY_INSERT_STATEMENT = INSERT_STATEMENT.format(table=TABLE_NAME)

                # execute the insert transaction 
                # TODAY: add the correct variables for MY_LIST_X
                # OPTIONAL: try `execute many`
                c.execute(MY_INSERT_STATEMENT, MY_LIST_1)
                c.execute(MY_INSERT_STATEMENT, MY_LIST_2)

                # This commits the transaction
                conn.commit()

                # Close the connection to the database.
                conn.close()
            ```


        2. Read Data: add this after the cursor is established. Comment out the lines similar to `c.execute(MY_INSERT_STATEMENT, SAMPLE_DATA)` for now.
            ```python
                
                SELECT_STATEMENT = "SELECT * FROM {table}"
                MY_SELECT_STATEMENT = SELECT_STATEMENT.format(table=TABLE_NAME)
                c.execute(MY_SELECT_STATEMENT)
                print c.fetchone()
                print c.fetchone()
                print c.fetchone()
                # print c.fetchall()  # try this with fetchone commented out.

                # retool this select statement to accomodate WHERE for sides < 4
                # hint: you must make a new SELECT statement.
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



4. #### Open Questions - Determine if these belong in this lesson:
* Discuss autocommmit, manual commit, buffered? commits (with example)
* row.keys() <-- get keys/headers for table
* SQLite and Python Types: https://docs.python.org/2/library/sqlite3.html#introduction
* Dealing with Date: https://docs.python.org/2/library/sqlite3.html#default-adapters-and-converters
* Munging data?
