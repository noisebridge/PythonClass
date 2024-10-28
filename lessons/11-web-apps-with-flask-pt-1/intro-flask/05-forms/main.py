import flask

app = flask.Flask(__name__)

def compute_meaning_of_life(arg):
  if arg == 42:
    return True
  return False

@app.route('/')
def index():
  return flask.render_template('index.html')

@app.route('/greet')
def greet():
  name = flask.request.args.get('first_name')
  if name is None:
    return flask.render_template('error.html')
  return flask.render_template('greet.html', name=name)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if flask.request.method == 'POST':
    email = flask.request.form.get('email')
    password = flask.request.form.get('password')
    join_list = flask.request.form.get('join_list')

    # Check for email existing.
    # Check password requirements.
    # Create user in database.
    compute_meaning_of_life(password)

    return flask.redirect('/')

  return flask.render_template('signup.html')