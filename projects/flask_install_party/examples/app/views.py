#from flask import Flask 
from flask import render_template, request, session, flash
from app import app
from app.forms import LoginForm

@app.route("/")
def hello():
    return 'hello world'

@app.route("/watsup")
def watsup():
    return 'what"s up? buddee?'

@app.route("/user")
def go_user():
    user = { 'nickname': 'Teddy' } # fake user
    return render_template("user.html",
        title = 'Home',
        user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        """u = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if u is None:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['user_id'] = u.user_id"""
        flash('You are now logged in')
        return render_template('register.html', form=LoginForm(request.form), error=error)
    return render_template('register.html', form=LoginForm(request.form), error=error)

@app.route('/fake_route')
def make_fake():
    return render_template("user.html",
        title = 'Home',
        user = "fake-user")

app.run()
