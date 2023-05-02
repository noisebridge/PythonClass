#using WTF-0.10.2
from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL

class RegisterForm(Form):
    ##NOTE: ADEQUATE ERROR MESSAGES AND POSSIBLE PASSWORD STRENGTH BAR NEEDED HERE!!!
    username = TextField('Username', validators=[DataRequired(), Length(min=4, max=25, message="name must be between 4 and 25 characters")])
    #Validates an email address. Note that this uses a very primitive regular expression and should only be used in instances where you later verify by other means, such as email activation or lookups.
    email = TextField('Email', validators=[DataRequired(), Length(min=6, max=40, message="email must be between 6 and 40 characters")])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=6, max=40, message="password must be between 6 and 40 characters")])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])