import datetime

import flask

app = flask.Flask(__name__)

def get_document(greeting, time_value):
  return f'''<!DOCTYPE html>
    <html>
    <head>
      <title>Hello World website</title>
    </head>
    <body>
      {greeting} {time_value}
    </body>
    </html>'''

@app.route('/')
def index():
  return get_document('Hello World!', datetime.datetime.now())

@app.route('/goodbye')
def goodbye():
  return get_document('Goodbye!', datetime.datetime.now())