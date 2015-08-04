from os.path import dirname, abspath, join

from flask import Flask, render_template, request, redirect, url_for

from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from forms import HackNewsUserForm

app = Flask(__name__)
db = SQLAlchemy(app)

from models import User


#config section
SECRET_KEY = 'sshh it"s a secret'
RECAPTCHA_PUBLIC_KEY = 'hello captcha'
_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'hack_news.db')

app.config.from_object(__name__)

Bootstrap(app)



@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/hi")
def hello_again():
    return render_template("custom_hello.html")

@app.route("/signup", methods=["GET", "POST"]) 
def signup():
    error = None
    signup_form = HackNewsUserForm()
    if request.method == "POST":
        if signup_form.validate_on_submit():
            user = User(signup_form.name.data,
                        signup_form.password.data,
                        signup_form.email.data)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('hello_again'))

    return render_template("signup.html", signup_form=signup_form, error=error)

if __name__ == '__main__':
    app.run(debug=True)