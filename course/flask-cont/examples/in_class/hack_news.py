from flask import render_template, request, redirect, url_for, session, flash, abort
from flask.ext.login import LoginManager, login_user, login_required

from config import app, db
from forms import HackNewsUserForm
from models import User


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signup'


@login_manager.user_loader
def load_user(user):
    print user 
    return User.query.get(user)


@app.route("/")
@login_required
def hello():
    print session
    print "next is dir(session)"
    print dir(session)

    session['logged_in'] = "yes I'm logged in"
    print session

    return render_template("hack_news_base.html")


@app.route("/hi", methods=["GET", "POST"])
@login_required
def hello_again():
    all_users = User.query.all()
    return render_template("custom_hello.html", all_users=all_users )



@app.route("/signup", methods=["GET", "POST"]) 
def signup():

    print 'signup'
    print 'request.args', request.args

    error = None
    signup_form = HackNewsUserForm(request.form)
    if request.method == "POST":
        print 'poster'
        if signup_form.validate_on_submit():



            print "was valid"

            user = User(signup_form.name.data,
                        signup_form.password.data,
                        signup_form.email.data)

            login_user(user)
            flash('Logged in successfully.')

            print 'request.args', request.args
            print session

            print request.args.get('next')

            print user, 'user'

            print 'signup form attrs', (signup_form.name.data,
                                        signup_form.password.data,
                                        signup_form.email.data)
            db.session.add(user)
            db.session.commit()

            return redirect(request.args.get('next'))
        else:
             print error

    return render_template("signup.html", signup_form=signup_form, error=error)

if __name__ == '__main__':
    app.run(debug=True)