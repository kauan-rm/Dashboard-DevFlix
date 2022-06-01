import os

class Config:
    SQLALCHEMY_DATABASE_URI= os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

config = {
    "default": Config
}
