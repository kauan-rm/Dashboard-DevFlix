from flask import Blueprint  # Import de biblioteca

auth = Blueprint('auth',__name__) # Cria planta de autenticação

from app.auth import views # Import views