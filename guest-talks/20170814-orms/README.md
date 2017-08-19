# ORMs (Object-Relational Mappings)

This lesson covers 3 Python ORMs: [the Django ORM](docs.djangoproject.com/#the-model-layer), [SQLAlchemy](http://docs.sqlalchemy.org/), and [Records](https://github.com/kennethreitz/records).

---

# What is an ORM?

Say you have a database that looks like this:

```
+-------------------|---------------+
| email             | name          |
|-------------------|---------------|
| razzi53@gmail.com | Razzi Abuissa |
+-------------------|---------------+
```

And a python class like this:


```python
class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name
```

---

You might find yourself writing code like this:

(this example uses [psycopg2](https://pypi.python.org/pypi/psycopg2), a Python-PostgreSQL database adapter)

```python
import psycopg2

connection = psycopg2.connect("dbname=orms")
cursor = connection.cursor()

def get_user_by_email(email):
    cursor.execute(
        """
        select * from users where email = %(email)s
        """,
        {'email': email}
    )

    record = cursor.fetchone()

    return User(record[0], record[1])


me = get_user_by_email('razzi53@gmail.com')
```

[ORMs (object-relational mappings)](https://en.wikipedia.org/wiki/Object-relational_mapping) allow you to accomplish what the functionality of the code without having to convert Python to and from SQL.

Here are 3 examples of Python ORMs doing the same as above using built-in functionality:

---

## [Django](docs.djangoproject.com/#the-model-layer)

```python
me = User.objects.get(email='razzi53@gmail.com')
```

[Django](docs.djangoproject.com) is a full-featured web framework and its ORM is at its core.

Database connection pooling, transaction, and result caching all handled for you.

---

## [SQLAlchemy](http://docs.sqlalchemy.org/)

```python
me = session.query(User).filter(User.email == 'razzi53@gmail.com').one()
```

SQLAlchemy is a stand-alone ORM library with tons of features - it's arguably the most advanced ORM in existence.

---

## [Records](https://github.com/kennethreitz/records)

```python
me = db.query('select * from users where email = (:email)', email='razzi53@gmail.com')[0]
```

"SQL for Humans" - simple, low abstraction library where you write plain SQL.

Records uses SQLAlchemy under the hood.

---

# ORM benefits

- Can think in Python types everywhere - ORM will map between python and sql
- Can write database-agnostic code - ORM will take care of differences between MySQL and Postgres, etc
- Can work with query as an object - compose filters, joins, aggregations without string concatenation
- ORM will escape dangerous query parameters that could cause (SQL injection)[https://en.wikipedia.org/wiki/SQL_injection]

# ORM drawbacks

- Might not be able to access advanced features if your ORM does not know about them
- Generated sql might be overly complex - ORM might hide bad database/query design
- Database operations might not do what you expect - obj.delete() might cascade surprisingly

# Conclusion

Relational databases are at the core of many applications, and Python ORMs are a great way to interact with them.

When used properly, they provide a powerful database abstraction that allows you to focus on your application.
