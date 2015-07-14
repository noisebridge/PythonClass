from flask import Flask, render_template, request, redirect

from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

#config section
SECRET_KEY = 'total secret'

app = Flask(__name__)

app.config.from_object(__name__)


class PersonForm(Form):
    name = StringField('name', validators=[DataRequired()])
    SSN = IntegerField('SSN', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])


@app.route("/person_form", methods=["GET", "POST"])
def hello():
    person_form = PersonForm()
    
    if request.method == "POST":
       if person_form.validate_on_submit():
           print person_form.name.data 
           print person_form.SSN.data 
           print person_form.age.data 
           return redirect("/hello")

    return render_template("base.html", person_form=person_form)


@app.route("/hi")
def hello_again():
    num_list = range(10)
    name = "me"
    hello = "hello there"
    return render_template("base.html", num_list=num_list, name=name, hello=hello)

@app.route("/hello")
def hello_again_again():
    num_list = range(10)
    li_numlist = ["<li>" + str(num) + "</li>" for num in num_list]
    return "<h2> This is a list </h2> <p> {} </p>  ".format(li_numlist)

#print dir(app)




app.run(debug=True)