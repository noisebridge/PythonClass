Introduction to Django    

    warm-up: model your very basic app in your head and be able to write it down on paper
    -write up a data model of something eg: grocery list or sports team, 
    -sketch up what it would look like to the user 
    -draw bubbles and arrows to show what would happen to data and/or UI on updates 

REQUIRES BLANK PAPER    

1. How we build web apps, [the simple Django diagram](http://www.thomaswhitton.com/django-presentation/images/432038560_9f8b830dfe_o.png), and [a nicer flow diagram](http://www.aprendendodjango.com/gallery/fluxo-no-mvc/file/) en espanol    
    -semantics problem of canonical MVC v. django's MTV    
    -btw why is it called django? and what is its story?    


2. Unwrapping the present that is django's MTV framework    
    -setting up the environment of course: virtualenv, pip install Django==1.5    
    -setting up the project: django-admin.py startproject <projectname>    
    -note that your project will contain multiple apps for the purpose of reusable code and uniformity of a contained project    
    -manage.py: Think running CLI scripts. This file is a command-line utility, used to manage and interact with your project. You probably won't ever have to edit the file itself; however, it is used with almost every process as you develop your Project.    
    -settings.py: Think configuration (modification: True). This is your project settings file for your project, where you configure your project's resources, such as database connections, external applications, and template files. There are numerous defaults setup in this file, which often get changed as you develop your Project.    
    -urls.py: Think routing (modification: True). This file contains the URL mappings, connecting URLs to Views    

####what an app is    
    -models.py: This file is used to define your data models that are connected to the database.    
    -tests.py: This houses your test files used for setting up unit and integration tests (don't worry about this for now).    
    -views.py: This file is your application's controller (as mentioned above), defining the business logic in order to render a view to the browser. 


    virtualenv .
    source bin/activate

    pip install Django==1.5

    django-admin.py startproject <projectname>

    cd <projectname>

    subl .

    python manage.py runserver <port #>

####Checkpoint: this should work!

python manage.py startapp <appname>
briefly checkout the files that we just created

Now, there are 3 steps to actually make things happen

######1. let your project settings in settings.py know the apps that you have created. 
    INSTALLED_APPS = ('<appname>')
Deciphering between the two can be one of the most frustrating and confusing things in django IMO

######2.  then you make a view function in views.py without making a template.     

    from django.http import HttpResponse
    def extreme_basic_view_function(request):   
       return HttpResponse('<html><body>Hello,World!</body></html>')

  notice the difference in what you have to pass to a view function in contrast to flask, the request object is necessary for django to function. notice that we have instantiated an HttpResponse object which we can just call a response object here

######3. but this won’t work until we let our project know about our url, in urls.py!
notice that we are using regex here!

add to urls.py

    urlpatterns = patterns('',
         url(r'^hello/$', ‘<appname>.views.extreme_basic_view_function')

now check to see if that can run


###Checkpoint
what are we trying to do on the highest level? what are web-apps? what is our purpose? 



####templates
create a template folder in your projects folder.
to do a template then we must pwd and get our absolute path to hookup the templates folder 

views.py
    from django.template import Context, loader
    from datetime import datetime

    def better_view_function(request):
        template = loader.get_template('main_list.html')
        context = Context({'current_time': datetime.now(),})
        return HttpResponse(template.render(context))

make a template folder in your <appname> folder. Inside that folder make an html file, in this case its main_list.html

    <html>￼
    <body>
    <h1>Hello, World! </h1>
    <p>This template was rendered on
    {{current_time}}.</p>
    </body>
    </html>

don’t forget to hook up the url with the proper regex code.

url(r'^better/$', ‘<appname>.views.better_view_function'),

####Data Model:

first, more config    

    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': '/Users/me/Documents/Py/PyClass/lessons/django-intro/examples/grocery_project/example.db',                      

we have to create it first tho. then synchronize 

    python manage.py syncdb

    define your model in models.py

    python manage.py sql <appname>
    python manage.py validate
    python manage.py syncdb

can use the shell if necessary, but we are only going to use the admin

    make an admin.py file in your <appname>

#then uncomment necessary lines in urls.py and settings.py   
