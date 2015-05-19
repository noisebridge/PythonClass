from flask import Flask, render_template, request
from os.path import dirname, abspath, join
from forms import PersonForm
from flask.ext.sqlalchemy import SQLAlchemy

_cwd = dirname(abspath(__file__))

SECRET_KEY = 'securekey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'really-secure-key'


app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)

@app.route("/", methods=("GET","POST", ))
def index():
    error = None
    if request.method == "POST":
        render_template("next.html", person_form=PersonForm(request.form), error=error)

    person_form = PersonForm()
    return render_template("home.html",
                           person_form=person_form,
                           )

'''<form method="POST" action="">
    {{ person_form.csrf_token }}
    {{ person_form.name.label }} {{ person_form.name(size=20) }}
    <input type="submit" value="Submit This Form">
</form>'''

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class PersonForm(Form):
    name = StringField('name', validators=[DataRequired()])

from conf_and_views import db 


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fav_food = db.Column(db.String) #db.relationship('Visit', backref='tracking_site', lazy='select')
    timesff_eaten_per_day = db.Column(db.Integer)

    def __repr__(self):
        return '<Person: {}'.format(self.name)

    def __str__(self):
        return self.name 

    def __unicode__(self):
        return self.name 

if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.run()