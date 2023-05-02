#### Taming the web with [Flask!](http://flask.pocoo.org/)


Basics concepts and interactive pipeline


0. #### Installation: Inside activated virtualenv    
    1. Getting installations out of the way    
        1. pip install [flask](http://flask.pocoo.org/)        
        2. pip install [flask-wtf](https://flask-wtf.readthedocs.org/en/latest/)    
        3. pip install [flask-bootstrap](http://pythonhosted.org/Flask-Bootstrap/)    
        3. pip install [flask-sqlalchemy](https://pythonhosted.org/Flask-SQLAlchemy/)    


1. #### Today's dive: Gluing together a basic app with common aspects of web frameworks - 40 minutes    

    ```python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return render_template("base.html")

    @app.route("/hi")
    def hello_again():
        return "<h1>Hello my friend!</h1>"
    
    if __name__ == '__main__':
        app.run(debug=True)
    ```    

    1. Amazing! What does it do? - 10 minutes
        1. what are the key concepts?    
        2. are there any reserved words at play here?      
        3. what are        other aspects of a modern web framework not included here?    
    2. What are the key objects here and how can we get to know them?    
        1. what environments are we in?     
        2. one new environment within the total environment is surely the browser    
    

2.  spiel on webflow    
    browser sends the request (which is essentially a string of bytes) through the web to your web server, most likely nginx
    your web server, hands over the request to a WSGI server, most likely uWSGI, or directly serves a file from the filesystem (although i’m not sure i fully gather the latter part)
    unlike a web server, a WSGI server can run python applications, the request populates a Python dictionary called environ and optionally passes through several layers of middleware, ultimately reaching your Web application
    after going through all the application logic of routing to a specific view, probably querying the database, doing database filtering and view logic, then finally the HttpResponse object gets rendered into a huge string and a web page is rendered in the user’s browser.
