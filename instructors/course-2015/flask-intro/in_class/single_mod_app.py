from os.path import dirname, abspath, join

from flask import Flask, render_template, request, redirect

from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

from flask.ext.sqlalchemy import SQLAlchemy


# config section
SECRET_KEY = 'total secret'  
#note: there are real ways to create and hide a secret key

_cwd = dirname(abspath(__file__))  # current working directory, here!
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')
#always make sure you have created your db before attempting to connect to it
#this can fail silently

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(__name__)


class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    SSN = db.Column(db.Integer)
    age = db.Column(db.Integer)

    def __init__(self, name, SSN, age):
        self.name = name 
        self.SSN = SSN 
        self.age = age

    def __repr__(self):
        return "Person: name {0} - SSN {1} - age {2}".format(self.name, self.SSN, self.age)


class PersonForm(Form):
    name = StringField('name', validators=[DataRequired()])
    SSN = IntegerField('SSN', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])


@app.route("/person_form", methods=["GET", "POST"])
def hello():
    person_form = PersonForm()
    error = None
    print "before request.method evaluated"

    if request.method == "POST":
       print "i've got a post request!"

       if person_form.validate_on_submit():
           print "form is valid"
           # the tricky part is realizing the data exists in the .data attribute 
           # of each field attribute of our PersonForm class
           # this is just how wtf_forms is modeled
           print person_form.name.data, person_form.SSN.data, person_form.age.data
           
           #here we instantiate a new SQLAlchemy object with our form data as its attributes!
           person = Person( person_form.name.data, 
                            person_form.SSN.data,
                            person_form.age.data)

           db.session.add(person)
           db.session.commit()

           #our database is now updated, so we redirect to a route/view that will show all queries 
           #so now follow the logic there  
           return redirect("/all_people")

    #remember that our first request to this route is a "GET" 
    #so the line below is run initially or when the form doesn't validate_on_submit()
    return render_template("main_person_form.html", person_form=person_form, error=error)


#this route queries database each time it is requested, 
#puts the results into people instance, and then renders it to 'all_people.html' 
#   context dictionary for jinja2 to parse
@app.route("/all_people")
def hello_again():
    people = Person.query.all()
    return render_template("all_people.html", people=people)


#the route below not part of the functioning app and can be deleted
#it was to demonstrate html being a string and how jinja2, the 'templating language'
#can be thought of as very intelligent string substitution
@app.route("/numbers_list")
def hello_again_again():
    num_list = range(10)
    li_numlist = ["<li>" + str(num) + "</li>" for num in num_list]
    return "<h2> This is a list </h2> <ul> num_list!! </ul> {} ".format( str(li_numlist) )

@app.route("/")
def other_routes():
    return "nuthin' here, look at urls we distinguished with an @app.route argument ie: \
           <li> <a href='person_form'> person_form </a> \
           <li> <a href='all_people'> all_people </a> \
           <li> <a href='numbers_list'> numbers_list </a> \
           "

if __name__ == "__main__":
    app.run(debug=True)
