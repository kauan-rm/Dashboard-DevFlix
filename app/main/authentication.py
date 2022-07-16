from flask_httpauth import HTTPTokenAuth
from flask import g#, current_app
from config import Config
from app.serializer import Serializer
secret_key = Config.SECRET_KEY
auth = HTTPTokenAuth()

@auth.verify_token
def verify_token(token):
    if token:
        u = Serializer.verify_auth_token(secret_key, token)
        if u:
            g.current_user = u
            return True
    return False

    #current_app.config['SECRET_KEY']