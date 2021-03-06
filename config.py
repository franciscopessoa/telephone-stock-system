import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///database/storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.environ.get("SECRET_KEY")