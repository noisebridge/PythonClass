from flask.ext.sqlalchemy import SQLAlchemy

_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')

db.create_all()


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fav_food = db.Column(db.String)
    timesff_eaten_per_day = db.Column(db.Integer)

    def __init__(self, name, fav_food, timesff_eaten_per_day):
        self.name = name 
        self.fav_food = fav_food
        self.timesff_eaten_per_day = timesff_eaten_per_day


    def __repr__(self):
        return '<Person: {}'.format(self.name)
