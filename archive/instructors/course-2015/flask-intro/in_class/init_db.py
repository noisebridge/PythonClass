from os.path import dirname, abspath, join

from flask.ext.sqlalchemy import SQLAlchemy
from single_mod_app import db

#for the config section
_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')


#need to run this just ONCE to create the database
db.create_all()
#note that in class we ran this in the interactive shell
