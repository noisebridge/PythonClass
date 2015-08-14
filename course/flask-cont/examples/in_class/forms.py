from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField 
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired


class HackNewsUserForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])


class HackNewsPostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    url = URLField('url')
    text = TextAreaField('text')

