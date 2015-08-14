from flask import render_template, request, redirect, url_for, session, flash, abort
from flask.ext.login import LoginManager, login_user, login_required

from config import app, db
from forms import HackNewsUserForm, HackNewsPostForm
from models import User, Post 


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signup'


@login_manager.user_loader
def load_user(user):
    print user 
    return User.query.get(user)


@app.route("/to_delete")
@login_required
def hello():
    print session
    print "next is dir(session)"
    print dir(session)

    session['logged_in'] = "yes I'm logged in"
    print session

    return render_template("hack_news_base.html")


@app.route("/hi", methods=["GET", "POST"])
def hello_again():
    all_users = User.query.all()
    return render_template("custom_hello.html", all_users=all_users)


@app.route("/", methods=["GET", "POST"])
def home():
    all_posts = Post.query.all()
    return render_template("home.html", all_posts=all_posts)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    hack_news_submit_form = HackNewsPostForm(request.form)
    print session 
    if request.method == "POST":
        if hack_news_submit_form.validate_on_submit():
            post = Post(hack_news_submit_form.title.data, 
                        hack_news_submit_form.url.data, 
                        'test_user')
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('home'))

    return render_template("submit.html", hack_news_submit_form=hack_news_submit_form)


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

            return redirect(url_for('hello_again'))
        else:
             print error

    return render_template("signup.html", signup_form=signup_form, error=error)

if __name__ == '__main__':
    app.run(debug=True)