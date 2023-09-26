import flask

app = flask.Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='World'):
  return f'Hello {name}'