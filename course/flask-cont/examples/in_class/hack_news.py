from flask import render_template, request, redirect, url_for

from config import app, db
from forms import HackNewsUserForm
from models import User


@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/hi", methods=["GET", "POST"])
def hello_again():
    return render_template("custom_hello.html")

@app.route("/signup", methods=["GET", "POST"]) 
def signup():
    print 'signup'
    error = None
    signup_form = HackNewsUserForm(request.form)
    if request.method == "POST":
        print 'poster'
        if signup_form.validate_on_submit():
            print "was valid"

            user = User(signup_form.name.data,
                        signup_form.password.data,
                        signup_form.email.data)
            print user, 'user'

            print 'signup form attrs', (signup_form.name.data,
                                        signup_form.password.data,
                                        signup_form.email.data)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('hello_again'))
        else:
             print error

    return render_template("signup.html", signup_form=signup_form, error=error)

if __name__ == '__main__':
    app.run(debug=True)