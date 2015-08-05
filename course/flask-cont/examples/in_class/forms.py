from flask_wtf import Form, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class HackNewsUserForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    # recaptcha = RecaptchaField()