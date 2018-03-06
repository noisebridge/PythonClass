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

If you want to clear your database and start over, you can remove db.sqlite3:

```sh
rm db.sqlite3
```

# Week 2 instructions

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

Add the following html somewhere on the page.

```html
<a href="/login">Login</a>
```

### Redirect after login to home page

If we use the form to log in now, we see

```
http://127.0.0.1:8000/accounts/profile/

Page not found (404)
```

Instead, let's redirect to the home page.

Edit retrosocial/retrosocial/settings.py

```python
LOGIN_REDIRECT_URL = '/'
```

### Show logged in as user on home page

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
python manage.py makemigrations
python manage.py migrate
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

### Make a form for Post

Edit retrosocial/users/models.py

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

### Make a PostCreateView

Edit retrosocial/users/views.py

```python
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from users.models import Post, PostForm

...

class PostCreateView(CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        post = form.save(commit=False)
        # add the currently-logged-in user as the post user
        post.user = self.request.user
        post.save()

        return HttpResponseRedirect('/')
```

### Render the posts and post form on the home page

Edit retrosocial/users/views.py

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

<h2>Posts</h2>
{% for post in posts %}
  <div>
    {{ post.user.username }}:
    {{ post.text }}
  </div>
{% endfor %}


{% if user.is_authenticated %}
  <h2>Make a post</h2>

  <form method="post" action="/post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Post</button>
  </form>
{% else %}
  <p>You must be logged in to post.</p>
{% endif %}
```

### Checkpoint: ability to log in and post

![homepage with posts and form](https://i.imgur.com/hO4QYA5.png)

For more information on Django generic views, see https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/.

## Week 3

https://devcenter.heroku.com/articles/deploying-python
