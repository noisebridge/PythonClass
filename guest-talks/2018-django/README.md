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

## Week 2: Modeling data

- models
- basic fields
- relational fields
- shell
- ORM
- forms
- migrations

## Week 3: Deploying to Heroku

## Week 4: Real-time communications with django-channels

## Other topics, as time allows

- testing
- extensions
- caching
- queues
- debugging
- stacktrace emails
- project templates
- static frontend

# Week 1: Setup, apps, urls, views, templates

### install django

```sh
brew install python3
pip install django
```

### startproject
```sh
$ django-admin startproject retrosocial
$ cd retrosocial
```

Now's a good time to set up version control:

```sh
$ git init
$ git add .
$ git commit -m "Django project template"
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
python manage.py startapp users
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

If you want to clear your database and start over, you can remove db.sqlite3:

```sh
rm db.sqlite3
```

# Week 2: Login, logout, models, forms

### Add login page to our app

Edit retrosocial/retrosocial/urls.py

```python
from django.contrib.auth.views import login

...

urlpatterns = [
    ...
    path('login', login)
]
```

If we load localhost:8000/login, we see
```
TemplateDoesNotExist at /login
registration/login.html
```

So let's create that.

Edit retrosocial/users/templates/registration/login.html.

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
```

### Add link to login

To let users get to /login, let's add a link to our index.html.

Edit retrosocial/users/templates/users/index.html.

Add the following html at the top of the page.

```html
<a href="/login">Login</a>
...
```

### Redirect after login to home page

If we use the form to log in now, we see

```
http://127.0.0.1:8000/accounts/profile/

Page not found (404)
```

Django thinks we're going to account profile after logging in, but let's redirect to the home page instead.

Edit retrosocial/retrosocial/settings.py.

```python
LOGIN_REDIRECT_URL = '/'
```

### Show logged in user on home page

Edit retrosocial/users/templates/users/index.html.

```html
{% if user.is_authenticated %}
  <p>Logged in as {{ user.username }}.
  <a href="/logout">Logout</a></p>
{% else %}
  <a href="/login">Login</a>
{% endif %}
```

### Add logout view

Edit retrosocial/retrosocial/urls.py.

The `{'next_page': '/'}` makes it so that logging out redirects back to the home page.

```python
from django.contrib.auth.views import login, logout

urlpatterns = [
    ...
    path('logout', logout, {'next_page': '/'})
]
```

### Checkpoint: login, logout

![home page with login](https://i.imgur.com/Eh0zbv4.png)

See also https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html.

### Create a Post model

Edit retrosocial/users/models.py

```python
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE
    )
```

### Make Post migration

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### Make a post in the shell

```
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> from users.models import Post
>>> me = User.objects.first()
>>> Post.objects.create(user=me, text='A post')
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
```

### Render the posts on the home page

Edit retrosocial/users/views.py.

```python
from users.models import Post
...


def home(request):
    users = User.objects.all()
    posts = Post.objects.all()

    return render(request, 'users/index.html', {
        'users': users,
        'posts': posts
    })
```

Edit retrosocial/users/templates/users/index.html.

```html
...

<h2>Posts</h2>

{% for post in posts %}
  <div>
    {{ post.user.username }}:
    {{ post.text }}
  </div>
{% endfor %}
```

### Make a form for Post

Edit retrosocial/users/models.py.

```python
from django import forms
...

class Post(models.Model):
    ...


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
```

### Render post form on the home page

Edit retrosocial/users/views.py.

```python
...
from users.models import Post, PostForm
...


def home(request):
    users = User.objects.all()
    posts = Post.objects.all()

    post_form = PostForm()

    return render(request, 'users/index.html', {
        'users': users,
        'posts': posts,
        'form': post_form
    })
```

Edit retrosocial/users/templates/users/index.html.

```html
...

<h2>Make a post</h2>

{% if user.is_authenticated %}
  <form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Post</button>
  </form>
{% else %}
  <p>You must be logged in to post.</p>
{% endif %}
```

### Allow POSTing data from html form

Edit retrosocial/users/views.py.

```python
def home(request):
    if request.method == 'POST':
        post = PostForm(request.POST).save(commit=False)
        post.user = request.user
        post.save()

    users = User.objects.all()
    ...
```

### Checkpoint: ability to log in and post

![homepage with posts and form](https://i.imgur.com/hO4QYA5.png)

# Week 3: Signup, Deploying to Heroku
## Create a signup form

In order for arbitrary users to be able to sign up for our social network, we'll need a way for them to sign up.

### Add signup url

We'll have a /signup route which will give them a signup form.

Edit retrosocial/urls.py:

```python
urlpatterns = [
    ...
    path('signup', views.signup)
]
```

### Add signup view

Here's the implementation of the signup view:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
```

And a barebones signup form, in retrosocial/users/templates/registration/login.html:

```html
<h2>Sign up</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign up</button>
</form>
```

Now we can navigate to localhost:8000/signup and see our form!

One last thing: let's add a link from the home page to the signup form. Can you figure out how to do that? Hint: we added a login link before, in a very similar way.

### Checkpoint: signup

![signup form](https://i.imgur.com/95bUlVH.png)

For more details on how to create a signup form, see https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html.

## Deploying to Heroku
### Switching to Postgres

The first thing we need to do to make our app production-ready is to switch from sqlite3 to Postgres.

Heroku runs multiple servers, each with their own file system, so sqlite won't work there.

Postgres is feature-rich and well-supported!

```sh
$ brew install postgres
```

Python bindings for postgres:

```sh
$ pip install psycopg2-binary
```

Start Postgres and create a database we can use:

```sh
$ brew services start postgresql
$ createdb master
```

You can confirm your database is running by connecting:

```sh
$ psql -d master
psql (10.3)
Type "help" for help.

master=# \q
```

(use \q or control-D to exit)

### Make our Django app use Postgres

Edit retrosocial/settings.py.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'master',
    }
}
```

Run your server, and you should get the familiar "unapplied migrations" warning.

Migrate your database and create a superuser and you'll be back up to speed.

### Sign up for heroku

It's free to sign up! No credit card required.

https://signup.heroku.com/

### Installing the Heroku CLI

See https://devcenter.heroku.com/articles/heroku-cli.

```sh
$ brew install heroku
```

### Gunicorn, a production-ready python server

Install gunicorn, our production server

```sh
$ pip install gunicorn
```

Test running our app using gunicorn

```sh
gunicorn retrosocial.wsgi
```

Now we can add that to Procfile so that Heroku knows how to run our app:

```
web: gunicorn retrosocial.wsgi
```

And we can test out how heroku will run our application:

```sh
$ heroku local
```

### Specify requirements for Heroku

Add the following to a new file, requirements.txt:

```
django
django-heroku
```

This tells Heroku the Python packages we need. Heroku will install them for us.

### Create the Heroku app

```sh
$ heroku create
```
### Settings tweaks for production

There is a library [django-heroku](https://github.com/heroku/django-heroku) which will configure settings for us.

```sh
$ pip install django-heroku
```

Edit retrosocial/settings.py to import (at the top) and configure (at the bottom) django_heroku.

```python
import django_heroku

...

django_heroku.settings(locals())
```

`django_heroku` will override the database setting to use whatever database is at the `DATABASE_URL` environment variable.

To use our local `master` database, we'll need to set `DATABASE_URL`:

```sh
$ export DATABASE_URL=postgres:///master
```

Make sure things are still working with:

```sh
heroku local
```

And open localhost:5000 (note the new port).

### Push to production

We start a deployment to heroku with `git push heroku master`.

```sh
$ git push heroku master
Counting objects: 25, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (22/22), done.
Writing objects: 100% (25/25), 5.08 KiB | 1.69 MiB/s, done.
Total 25 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.4
...
```

### Open our application

```
$ heroku open
```

We'll see an error, since we don't have a database yet.

```sh
$ heroku logs
```

### Create a database and run migrations

Heroku treats databases as an "add-on".

Once we add the database, we'll need to apply migrations on that database.

```sh
$ heroku addons:create heroku-postgresql
Creating heroku-postgresql on ⬢ stark-wave-50438... free
Database has been created and is available
...
$ heroku run python manage.py migrate
...
```

Now you should be able to `heroku open` to interact with your application on a URL anybody can access!

For the full Heroku guide on deploying python, see https://devcenter.heroku.com/articles/deploying-python.

## Week 4: Real-time communications with channels

One feature we've come to expect from modern web applications is having new information load on the page instantly, without waiting for us to refresh.

We can accomplish this in our own application with a websocket.

### Install channels

```sh
$ pip install channels
```

Add to installed apps in retrosocial/settings.py

```diff
@@ -39,7 +39,8 @@ INSTALLED_APPS = [
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
-    'users.apps.UsersConfig'
+    'users.apps.UsersConfig',
+    'channels'
 ]
```

Add asynchronous router to new file retrosocial/router.py

```python
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({})
```

Test our new asynchronous-ready project with `python3 manage.py runserver`:

```sh
$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
March 19, 2018 - 18:09:06
Django version 2.0.3, using settings 'retrosocial.settings'
Starting ASGI/Channels development server at http://127.0.0.1:8000/
```

### Server implementation of websocket

We first create a class that represents a websocket client.

Edit retrosocial/users/consumers.py.

```
import json

from channels.generic.websocket import AsyncWebsocketConsumer


GROUP_NAME = 'default'


class FeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            group=GROUP_NAME,
            channel=self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            GROUP_NAME,
            channel=self.channel_name
        )

    async def update_feed(self, event):
        await self.send(json.dumps(event))
```

Edit route `/socket` to this handler in retrosocial/users/routing.py.

```python
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('socket', consumers.FeedConsumer),
]

```

Update `retrosocial/router.py` to connect websocket protocol connections to our `websocket_urlpatterns`.

```python
from channels.routing import ProtocolTypeRouter, URLRouter

from users import routing


application = ProtocolTypeRouter({
    'websocket': URLRouter(
        routing.websocket_urlpatterns
    )
})
```

### Creating our Redis channel

Redis serves as a messaging control point which allows us to reach all of our clients, regardless of which server they are connected to, since we only have 1 redis.

```sh
$ pip install channels_redis
```

Edit `retrosocial/settings.py`:

```
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
```

#### Send the new post to all clients

Now in our view, we have to send an `update_feed` message to our group:

```python
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

import channels
from asgiref.sync import async_to_sync

from users.models import Post, PostForm

from .consumers import GROUP_NAME


channel_layer = channels.layers.get_channel_layer()


def notify_new_post(username, text):
    async_to_sync(channel_layer.group_send)(
        GROUP_NAME,
        {
            'type': 'update_feed',
            'text': text,
            'username': username
        }
    )


def home(request):
    if request.method == 'POST':
        post = PostForm(request.POST).save(commit=False)
        post.user = request.user
        post.save()

        notify_new_post(request.user.username, post.text)
        
    ...
```

#### Debugging websockets

We can test our implementation with the python `websocket-client` library and its script `wsdump.py`.

```sh
$ pip install websocket-client
...
$ wsdump.py localhost:8000/socket
```

It's also useful to open the developer tools in your browser, find the websocket, and inspect its messages (or lack thereof).

### Client implementation of websocket

We'll need to add some javascript to connect the websocket. For now, putting a `script` tag directly in index.html works just fine.

Edit retrosocial/users/templates/users/index.html

```javascript
<script>
  const ws = new WebSocket(`ws://${window.location.host}/socket`)
  ws.onmessage = event => {
    const data = JSON.parse(event.data)
    const div = document.createElement('div')

    div.innerText = `${data.username}: ${data.text}`

    document.getElementById('posts').appendChild(div)
  }
</script>
```
 
Wrap the posts in a div, so that we can access it from JavaScript:

```diff
-{% for post in posts %}
-  <div>
-    {{ post.user.username }}:
-    {{ post.text }}
-  </div>
-{% endfor %}
+<div id="posts">
+  {% for post in posts %}
+    <div>
+      {{ post.user.username }}:
+      {{ post.text }}
+    </div>
+  {% endfor %}
+</div>
```

#### Bonus: add autofocus attribute to new post form.

Makes it feel like real-time chat, even though the page reloads for the sender :)

Edit retrosocial/users/models.py

```python
class PostForm(forms.ModelForm):
    def __init__(self, data=None):
        super().__init__(data)
        self.fields['text'].widget.attrs.update({'autofocus': 'true'})

    ...
```

Generally I try not to do too much html configuration in Python, since server-side rendering has many limitations, but you can customize your form just by modifying the `PostForm` class.

### Additional directions

For a more-fleshed-out chat example of websockets, check out the [official channels tutorial](https://channels.readthedocs.io/en/latest/tutorial/index.html).

Deploying websockets to production is non-trivial - in particular, although the development server supports basic http as well as long-running connections, in production we'd need to switch out gunicorn for [daphne](https://github.com/django/daphne/).

The POST call could also be modified to send the post data over the websocket.

