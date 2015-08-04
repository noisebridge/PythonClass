from datetime import datetime

from hack_news import db


class User(db.Model):
 
    __tablename__ = "hack_news_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), unique=True)
    date_created = datetime.now()

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User {0}, Email: {1}>'.format(self.username, self.email)