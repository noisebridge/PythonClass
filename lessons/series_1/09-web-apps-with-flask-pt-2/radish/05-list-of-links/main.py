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
  if not name or not url:
    flask.abort(400)

  db = sqlite3.connect('../db.sqlite')
  with closing(db.cursor()) as cursor:
    cursor.execute('''
      INSERT INTO links (name, url) VALUES (?, ?)
    ''', (name, url))
  db.commit()

  return flask.redirect('/')