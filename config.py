import os
SECRET_KEY = os.urandom(32)
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY ='blindspot1'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ekirapa:99405897@localhost/blog1'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = '34730875'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True