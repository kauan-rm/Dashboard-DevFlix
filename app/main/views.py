# Inicio import
from app.main import main
from flask_login import login_required
from flask import render_template, request
from ..models import Imagem
# Termino import

@main.route("/") # Rota index em desenvolvimento
@login_required
def index():
    ROWS_PER_PAGE = 6

     # Set the pagination configuration
    page = request.args.get('page', 1, type=int)

    pages = Imagem.query.paginate(page=page, per_page=ROWS_PER_PAGE)
   
    return render_template('index.html', pages=pages)  # Renderiza arquivo html pasta templates