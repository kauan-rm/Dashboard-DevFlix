# Inicio import
from app.main import main
from flask_login import login_required
from flask import render_template, request
from ..models import Imagem, Permission
from app.main.decorators import permission_required
# Termino import

@main.route("/")
def index():
    return render_template('base.html')  # Renderiza arquivo html pasta templates

@main.route("/home")
@login_required
@permission_required(Permission.USAR)

def home(): 
    ROWS_PER_PAGE = 6

     # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    pages = Imagem.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('index.html', pages=pages)