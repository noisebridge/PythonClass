

#### Introduction to Flask Microframework for Web Development

This is a basic introduction to flask intended to give us an understanding of the popular Model, Template, View web application code pattern. Flask has [an excellent tutorial](http://flask.pocoo.org/docs/0.10/).


1. ##### Today's deep dive: [Run Flask](http://flask.pocoo.org/)

    ```bash
    # This part goes in your bash shell.
    # you must have python-virtualenv and python-pip installed to use a virtualenv
    $ mkdir sampleapp
    $ cd sampleapp
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install flask
    ```

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello world!"

    if __name__ == "__main__":
        app.run()
    ```

    1. Ok... how do I see my work?
        1. Run your application `$ python app.py`
        2. In a browser, go to `http://localhost:5000`
        3. You should see these words: Hello World!

    2. Other topics we will cover today:
        1. Accessing a template
        2. Organizing your templates
        3. Static assets


2. ##### Lets get this working with a template!

    1. Flask [uses Jinja2](http://jinja.pocoo.org/docs/dev/)
        1. We just use it. There is [a tutorial](http://flask.pocoo.org/docs/0.10/tutorial/templates/) for this.
            ```python
            from Flask import flask, render_template
            
            # lets add a new route
            @app.route("/sample-page/")
            def samplepage():
                return render_template("sample-page.html")
            ```


    2. ###### Example 1: Using json.loads() and json.dumps()

        ``` Python
        ```

    3. ###### Example 2: Using json.load() and json.dump()

        ``` Python
        """
        ```

3. ##### Lets get this working with an HTML template!

    1. [Stuff]()
        1. More Stuff
            ```python
            ```
        2. Even more stuff


    2. ###### Example 1: Using json.loads() and json.dumps()

        ``` Python
        ```

    3. ###### Example 2: Using json.load() and json.dump()

        ``` Python
        """
        ```

