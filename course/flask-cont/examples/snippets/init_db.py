'''This module will configure and initialize the database using the SQLAlchemy ORM.
   We only need to run this script once per database creation. 
'''

from os.path import dirname, abspath, join

from <your_app_name> import db


#for the config section
_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')


#need to run this just ONCE to create the database
db.create_all()


#note that it is possible to run this in the interactive shell
