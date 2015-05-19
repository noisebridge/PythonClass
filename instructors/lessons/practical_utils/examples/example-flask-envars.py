'''
without knowing other objects the pattern on line 15 is the key 

''' 


import os 
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir 

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
#focus on the line below
oid = OpenID(app, os.path.join(basedir, 'tmp'))