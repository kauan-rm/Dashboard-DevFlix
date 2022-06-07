from flask import Blueprint # Import biblioteca

main = Blueprint('main',__name__) # Cria planta de interface 

from app.main import views  # Import views