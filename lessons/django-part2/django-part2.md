[Request-Response-Cycle](http://rnevius.github.io/django_request_response_cycle.png)

Introduction to Django Part 2 - Model driven approach 

    warm-up: briefly review structure of app in Part 1, what questions arise?

1. Starting a fresh project with proper names and structure         

-setting up the environment of course:
create a new directory to use as your project root    

    virtualenv .

    source bin/activate

    pip install Django

    django-admin.py startproject <projectname>

    mv <proj_name> repo_root

    touch .gitignore

    touch Makefile

    cd repo_root    

2. Creating Models and interacting with them in the shell and admin interfaces    

    python manage.py migrate  #creating database

    --make your models in <app>/models.py

    python manage.py makemigrations <appname>

    --let's check out what the actual SQL statements we just wrote look like

    python manage.py sqlmigrate <appname> 0001

    python manage.py shell

    --import the class you defined in your <appname>.models

    python manage.py createsuperuser

    --enter ‘me’ for everything (cuz not putting this into production)

    --now we can start the server for a quick check

    python manage.py runserver <port # optional>

    --need to let admin.py know about the models we defined

    --then a single line will connect everything for you

    admin.site.register(<ModelClass>)

    --we can do a lot of customization of this admin form 

3. Setting up proper urls.py structure

    re-routing the urls can be a bit tricky and but its necessary for sane and reusable code down the line.

    <appname>/urls
    from django.conf.urls import patterns, url

    from . import views

    urlpatterns = patterns('',
        url(r'^$', views.<view_func_name>, name=‘<good name>'),
        )

    <appname>/urls
    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', ‘<proj_name>.views.home', name='home'),
        # url(r’^<url_name>/', include(‘<appname>.urls')),
        url(r’^<url_name>/', include(‘<appname>.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )

4. Setting up the template path in settings.py     
    
    #add to settings.py
    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

5. Setting up the view function in views.py

    def <view-func-name>(request):
        <data_to_post> = Post.objects.all()
        context = {'<data_to_post>': <data_to_post>}
        return render(request, '<appname>/main.html', context)

    #ok, now we can finally run the server!

    python manage.py runserver <port# optional>

6. Slightly intelligent templates

    <html> 
    <head> 
    <style type="text/css"> 
    ul#list { list-style-type: none; } 
    </style> 
    </head> 

    <body>
    {% for item in <data_to_post> %}
     
        <p>{{ item.<data_field1>}}</p>
    <ul id="list">
        <li>amount: {{ item.<data_field2>}}</li>
        <li>weight: {{ item.<data_field3>}}</li>
        <li>content: {{ item.<data_field4>}}</li>
        <li>created: {{ item.<data_field5>}}</li>
    </ul>

    {% endfor %}

    </body>
</html>

Extra: customize the admin template

    #find where everything in django resides    

    python -c "import sys sys.path = sys.path[1:]import djangoprint(django.__path__)"    

    #open that path and then 
    (django/contrib/admin/templates/admin/base_site.html)

    find where it says Django Admin and change the naming scheme around
 