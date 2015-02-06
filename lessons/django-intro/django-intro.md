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
