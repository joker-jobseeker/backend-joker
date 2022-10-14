import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_migrate import Migrate
from os import environ
from remotejob.config import DEV_DB, PROD_DB

# Create a login manager object
app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
# if os.environ.get('DEBUG')=="1":
#     app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB
app.config['SQLALCHEMY_DATABASE_URI'] =  environ.get('DATABASE_URL').replace("postgres", "postgresql") or DEV_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

from remotejob import routes
from remotejob import models