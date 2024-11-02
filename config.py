# config.py
import os


class Config:
    # or another URI for a different database (e.g., MySQL, PostgreSQL)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret123')
