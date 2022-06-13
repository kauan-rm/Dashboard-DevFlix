# Inicio import
from app.main import main
from flask_login import login_required
from flask import render_template
# Termino import

@main.route("/") # Rota index em desenvolvimento
@login_required
def index():
    return render_template("base.html")  # Renderiza arquivo html pasta templates