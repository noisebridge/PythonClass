from os.path import dirname, abspath, join

from flask.ext.sqlalchemy import SQLAlchemy


#for the config section
_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')


#need to run this just ONCE to create the database
db.create_all()
#note that in class we ran this in the interactive shell


class Person(db.Model):
    __tablename__ = 'people'

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
