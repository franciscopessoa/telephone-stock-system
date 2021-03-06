import datetime
from app import db, ma
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username   = db.Column(db.String(50), unique=True, nullable=False)
    password   = db.Column(db.String(200), nullable=False)
    name       = db.Column(db.String(200), nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name     = name
        self.email    = email
        
    def hash_password(self):
      self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
      return check_password_hash(self.password, password)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password')
