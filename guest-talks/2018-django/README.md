# Python Class Django Mini-Course

Slides are at http://slides.com/razzi/pyclass-django

## What we'll be building

RetroSocial, a basic social network

- signup / login / logout
- posting
- messaging
- API

## Week 1: Serving html

- installing
- startproject
- development server
- migrating the database
- createsuperuser
- django.contrib.auth
- admin
- apps and startapp
- views
- url routing
- templates

## Week 2: Modeling data and deploying django

- models
- basic fields
- relational fields
- shell
- ORM
- forms
- migrations

## Week 3: Real-time communications

- polling
- channels
- work queues

## Week 4: APIs and static frontends

- collectstatic
- rest framework
- api
- static files on cdn

## Other topics, as time allows

- testing
- extensions
- caching
- queues using redis
- debugging
- stacktrace emails
- project templates

# Week 1 instructions

### install django

```sh
brew install python3
pip install django
```

### startproject
```sh
django-admin startproject retrosocial
cd retrosocial
```
### runserver
```sh
python manage.py runserver
```
### migrate

```sh
python manage.py migrate
```
### createsuperuser
```sh
python manage.py createsuperuser
```
### admin

```sh
python manage.py runserver
open localhost:8000/admin
```

### startapp

```
python manage.py startapp social
```

### register app (settings.py)

Edit retrosocial/retrosocial/settings.py

### Add index view

Edit retrosocial/users/views.py

### edit urls

Edit retrosocial/retrosocial/urls.py

### create template

Edit retrosocial/users/templates/users/index.html

### Checkpoint: display user list on homepage

![homepage with user list](https://imgur.com/qD5Huce.jpg)

### delete database for fresh start

If you want to clear your database and start over, you can db.sqlite3:

```sh
rm db.sqlite3
```
