import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.render_template('index.html')
  
@app.route('/hello/', methods=["POST"])
def hello():
  name = flask.request.form.get('name', 'World')
  return f'Hello {name}'