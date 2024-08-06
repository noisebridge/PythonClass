import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  return ('''<!DOCTYPE html>
    <html>
    <head>
      <title>Hello World website</title>
    </head>
    <body>
      Hello World! %s
    </body>
    </html>''' % str(datetime.datetime.now()))