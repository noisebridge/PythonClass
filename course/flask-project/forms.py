from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField 
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, URL, Optional


class HackNewsUserForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    #note there is an Email Validator as well



class HackNewsPostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    url = URLField('url', validators=[URL(message="link to post"), DataRequired()])
    text = TextAreaField('text', validators=[Optional()])


