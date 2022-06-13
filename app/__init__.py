# Inicio Import bibliotecas do flask

from flask import Flask
from config import config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# Termino import bibliotecas do flask

db = SQLAlchemy()  # Instanciando o Banco de Dados do sqlAlchemy
login_manager = LoginManager()
login_manager.session_protection = "strong" #nível de encriptação
login_manager.login_view = 'auth.login' #

def create_app(config_name): # Método cria app
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # Seleciona o ambiente de desenvolvimento

    db.init_app(app) # Iniciando o Banco de Dados
    login_manager.init_app(app)   

    # Inicio import/registro Blueprint
    from app.auth import auth as auth_bp
    from app.main import main as main_bp
     
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp) #, url_prefix ='/auth') 
    # Termino import/registro Blueprint

    return app

