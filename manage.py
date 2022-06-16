# Inicio imports
from app import create_app, db
from app.models import *
from flask_migrate import Migrate
# Termino imports

app = create_app("default") # Instanciando a criaçao da aplicação


migrate = Migrate(app,db) # Instancia a migração do banco de dados através do Alembic 

if __name__ == "__main__": # Verifica se "name" do app é igual ao "main" para rodar o app
    app.run(debug=True)