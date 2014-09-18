#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI

from app import db
import os.path
db.create_all()