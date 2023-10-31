from contextlib import closing
import sqlite3

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  db = sqlite3.connect('../db.sqlite')
  with closing(db.cursor()) as cursor:
    cursor.execute('SELECT url, name FROM links')
    links = cursor.fetchall()
  return flask.render_template('index.html', links=links)

@app.route('/links/new')
def new_link():
  return flask.render_template('new_link.html')
  
@app.route('/links/create', methods=["POST"])
def create_link():
  name = flask.request.form.get('name')
  url = flask.request.form.get('url')
  
  name_error = None
  if not name:
    name_error = 'This is not a correct entry!'
  url_error = None
  if not url:
    url_error = 'The data you provided is somehow unsatisfactory!'

  if name_error or url_error: 
    return flask.render_template('new_link.html', name=name, url=url, name_error=name_error, url_error=url_error)

  db = sqlite3.connect('../db.sqlite')
  with closing(db.cursor()) as cursor:
    cursor.execute('''
      INSERT INTO links (name, url) VALUES (?, ?)
    ''', (name, url))
  db.commit()

  return flask.redirect('/')