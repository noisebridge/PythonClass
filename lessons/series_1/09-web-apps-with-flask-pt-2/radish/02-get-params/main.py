import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.render_template('index.html')
  
@app.route('/hello/')
def hello():
  name = flask.request.args.get('name', 'World')
  return f'Hello {name}'