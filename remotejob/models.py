from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from remotejob import db

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Integer, default=0)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class ExpToken(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    token_code = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, index=True)
    exp = db.Column(db.DateTime)
    
    def __init__(self, token_code, user_id, exp):
        self.token_code = token_code
        self.user_id = user_id
        self.exp = exp  
