

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

	# never leave this on in production or someone will break your site.
	app.debug = True

    @app.route("/")
    def hello():
        return "Hello world!"

    if __name__ == "__main__":
        app.run()
		# app.run(0.0.0.0) # will run your site on all public IPs. No need to do this.
    ```

    1. Ok... how do I see my work?
        1. Run your application `$ python app.py`
        2. In a browser, go to `http://localhost:5000`
        3. You should see these words: `Hello world!`

    2. Other topics we will cover today:
        1. Accessing a template
        2. Organizing your templates
        3. Static assets


2. ##### Lets get this working with a template!

    1. Flask [uses Jinja2](http://jinja.pocoo.org/docs/dev/).
        1. We just import it. There is [a tutorial](http://flask.pocoo.org/docs/0.10/tutorial/templates/) for this.
        2. Lets update our code to have the extra import and a new route/template.

            ```python
            from Flask import flask, render_template
            
            # lets add a new route
            @app.route("/sample-page/")
            def samplepage():
                return render_template("sample-page.html")
            ```

        3. This sample is from the tutorial's template page. Put this in `/templates/sample-page.html`. `/templates/` is the default path in a Flask project.

            ```html
            <!doctype html>
            <title>Sample Template</title>
            <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
            <div class=page>
              <h1>This is our sample app!</h1>
              {% block body %}
              {% endblock %}
            </div>
            ```

        4. Another thingy

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

