

#### Taming the web with [Flask!](http://flask.pocoo.org/)


Basics concepts and interactive pipeline


0. #### Installation: Inside activated virtualenv    
    1. Now    
        1. pip install flask    
    2. Later    
        1. pip install flask-wtf    
        2. pip install flask-sqlalchemy    


1. #### Today's dive: Entering the browser... - 20 minutes    

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/hi")
    def hello_again():
        return "<h1>Hello my friend!</h1>"

    app.run(debug=True)
    ```    

    1. Amazing! What does it do? - 10 minutes
        1. not going to cover [@app.route in depth](http://ains.co/blog/things-which-arent-magic-flask-part-1.html)    
        2. html turns out to be just a string! interpreted by your browser     
        3. play with this, add whatever python you want, use string substitution    
    2. What are the key objects here and how can we get to know them?    
        1. what environments are we in?     
        2. one new environment within the total environment is surely the browser    
    

2. #### Wonderful, but how do all my regular sites work? - 20 minutes    
    1. Look at a popular site or two     
        1. how can we inspect all the html?    
        2. which patterns can we apply to our own app?    
    2. We've done some database programming, so where is the db on this site?    
        1. in an OOP paradigm what objects are you seeing and how one might model them?    

3. #### Getting a bit smarter than return simply string substitution - 20 minutes     
    1. Making html files with embedded python objects in a 'templates' folder    
        1. jinja2 objects and control statements    
        2. syntax   
        3. communication with the view   

4. #### Danger! Accepting User input with forms - 20 minutes     
    0. Justification for addressing this topic    
    1. extending flask: install and import    
    2. canonical extension (https://flask-wtf.readthedocs.org/)    
       1. it wraps wtforms    
       2. the library of tools as functions that we now have    
    3. necesary configuration    
    4. communication with template    
    5. quick but intelligent debugging    


5. #### Database: Amazing abstractions with SQLAlchemy so we can write fast! - 20 minutes     
    1. canonical extension [flask-sqlalchemy](https://pythonhosted.org/Flask-SQLAlchemy/)    
       1. it wraps SQLAlchemy and was written by Armin    
       2. what is SQLAlchemy?    
    2. how to connect to a database    
    3. how to define a model    
    4. accessing the model    


6. #### Lab Primer 
    1. Play with some more routes!    



7. #### Extended Resources - any links or resources to take this concept further    
    1. [What is a web framework: Jeff Knupp](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)    
    2. [What exactly is a web framework: SO](http://stackoverflow.com/questions/3345512/what-exactly-is-a-web-framework#3345751)    
    3. Knowing where the flask package and source code lives in your virtualenv    
        1. the source code is relatively readable     
    4. [what is whisky?](https://www.python.org/dev/peps/pep-0333/) or WSGI?    
 
 8. spiel on webflow    
    browser sends the request (which is essentially a string of bytes) through the web to your web server, most likely nginx
    your web server, hands over the request to a WSGI server, most likely uWSGI, or directly serves a file from the filesystem (although i’m not sure i fully gather the latter part)
    unlike a web server, a WSGI server can run python applications, the request populates a Python dictionary called environ and optionally passes through several layers of middleware, ultimately reaching your Web application
    after going through all the application logic of routing to a specific view, probably querying the database, doing database filtering and view logic, then finally the HttpResponse object gets rendered into a huge string and a web page is rendered in the user’s browser.

