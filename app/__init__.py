from flask import Flask
from config import config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# Termino import bibliotecas do flask

db = SQLAlchemy()  # Instanciando o Banco de Dados do sqlAlchemy
login_manager = LoginManager()
login_manager.session_protection = "strong" #nível de encriptação
login_manager.login_view = 'auth.login' #


db = SQLAlchemy()
mail = Mail()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app) 
    login_manager.init_app(app)  
    mail.init_app(app)

    from app.auth import auth as auth_bp
    from app.main import main as main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp) #, url_prefix ='/auth')
    
    return app
