import datetime

import flask

app = flask.Flask(__name__)

@app.route('/goodbye')
def goodbye():
  return flask.render_template(
    'greeting.html',
    greeting='Goodbye!',
    time_value=datetime.datetime.now())

@app.route('/greet')
def index():
  return flask.render_template(
    'greeting.html',
    greeting='Hello World!',
    time_value=datetime.datetime.now())

@app.route('/greet/<name>')
def greet(name):
  greeting = f'Hello {name}!'
  return flask.render_template(
    'greeting.html',
    greeting=greeting,
    time_value='')