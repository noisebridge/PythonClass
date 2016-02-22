
### The 'SQLite' Relational Database Format

Use SQLite to store information inside your application. It was originally developed for the US Navy to embed in their hardware. SQLite is ubiquitous in software.



>SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. **It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.** It provides a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](http://www.python.org/dev/peps/pep-0249)." - from [The Python 'sqlite3' Module](https://docs.python.org/2/library/sqlite3.html)



1. #### Today's deep dive: Create a [database schema](https://www.sqlite.org/lang.html).

    1. Definitions:
        1. Table - similar to an excel spreadsheet, it is a collection of rows and columns.
            1. Each column has a `name` and `the same data type for each value` in the column.
            2. Each row has one field per column.
        2. Schema - A schema describes a table.
        3. Database - a collection of tables, schemas, and some related things.
    2. Type this code into a file to make a database:

        ```
        -- Run this file with the .read command.
        -- Older sqlite3 (osx packages a really old version) apparently don't have this.
        -- If this happens, you can run sqlite3 at the command prompt and type the following in.


        -- The .open command will open a database. If it doesn't
        -- exist, it will create it. (are there exceptions to this?)
        .open "polygons.sqlite" 


        CREATE TABLE IF NOT EXISTS "Polygons" ( 
            "pKey" INTEGER PRIMARY KEY,
            "Name" varchar(255) DEFAULT NULL, 
            "Sides"  varchar(255) DEFAULT NULL,
            "SidesEnglish"   varchar(255) DEFAULT NULL,
        );
        ```



```
SQLite version 3.8.10.2 2015-05-20 18:17:19
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open mypolygons.sqlite
```



2. ##### Interacting with our database in Python.

    In this section, we will use Python's [sqlite3 module](https://docs.python.org/2/library/sqlite3.html) to communicate with our database.
    
    1. Goals: read from the database, write to the database, see our work.

    2. Examples:
        1. Write Data:
        ```python
        """Write a sample directly from a Python list of lists.
        """
        import sqlite3

        FILENAME = "mypolygons.sqlite"
        TABLE_NAME = "Polygons"

        if __name__ == '__main__':
            """ Write some data to our database.
            """

            SAMPLE_DATA_1 = (None, "square", 4, "four")
            SAMPLE_DATA_2 = (None, "triangle", 3, "three")

            # Create a connection to the database, assign to a name
            conn = sqlite3.connect(FILENAME)

            # We will use the cursor object to perform transactions.
            c = conn.cursor()

            # we can use {table} with the string function "format"
            # more here: https://docs.python.org/2/library/string.html#format-string-syntax
            INSERT_STATEMENT = "INSERT INTO {table} VALUES (?,?,?,?)"
            MY_INSERT_STATEMENT = INSERT_STATEMENT.format(table=TABLE_NAME)

            # execute the insert transaction -- it isn't committed to the database yet!!
            c.execute(MY_INSERT_STATEMENT, SAMPLE_DATA_1)
            c.execute(MY_INSERT_STATEMENT, SAMPLE_DATA_2)

            # This commits the transaction
            conn.commit()

            # Close the connection to the database.
            conn.close()
        ```


        1. Read Data: add this after the cursor is established, comment out the line `c.execute(MY_INSERT_STATEMENT, SAMPLE_DATA)` for now.
        ```python
            
            SELECT STATEMENT = "SELECT * FROM {table}"
            MY_SELECT_STATEMENT = SELECT_STATEMENT.format(table=TABLE_NAME)
            c.execute(MY_SELECT_STATEMENT)

            # retool this select statement to accomodate WHERE for sides < 4
        ```
        3. See our work:
        ```
        sqlite> .open mypolygons.sqlite
        sqlite> .schema
        CREATE TABLE "Polygons" (
            "pKey" INTEGER PRIMARY KEY,
            "Name" varchar(255) DEFAULT NULL,
            "Sides"  varchar(255) DEFAULT NULL,
            "SidesEnglish"   varchar(255) DEFAULT NULL
        );
        sqlite> select * from Polygons;
        1|square|4|four
        sqlite> ^D
        ```

4. #### Extended Resources - An overview of sqlite technologies
    1. [What's SQL?](http://en.wikipedia.org/wiki/SQL) - "SQL (Structured Query Language) is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS).
    2. [RDBMS](http://en.wikipedia.org/wiki/Relational_database_management_system) - "A relational database management system (RDBMS) is a database management system (DBMS) that is based on the relational model."

    3. [DBMS](http://en.wikipedia.org/wiki/Database) - Database management systems (DBMSs) are computer software applications that interact with the user, other applications, and the database itself to capture and analyze data. A general-purpose DBMS is designed to allow the definition, creation, querying, update, and administration of databases.
    4. [Relational Model](http://en.wikipedia.org/wiki/Relational_model) - Most relational databases use the SQL data definition and query language; these systems implement what can be regarded as an engineering approximation to the relational model. A table in an SQL database schema corresponds to a predicate variable; the contents of a table to a relation; key constraints, other constraints, and SQL queries correspond to predicates. However, SQL databases deviate from the relational model in many details, and Codd fiercely argued against deviations that compromise the original principles.


Open Questions - Determine if these belong in this lesson:
* Discuss autocommmit, manual commit, buffered? commits (with example)
* row.keys() <-- get keys/headers for table
* SQLite and Python Types: https://docs.python.org/2/library/sqlite3.html#introduction
* Dealing with Date: https://docs.python.org/2/library/sqlite3.html#default-adapters-and-converters
* Munging data?
