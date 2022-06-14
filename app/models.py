# Inicio import bibliotecas
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Termino import biblioteca


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #carregamento do usuário

def insert_users(request):
    user = User()
    user.nome = request['nome']
    user.cpf = request['cpf']
    user.email = request['email']
    user.senha = request['senha']
    db.session.add(user)
    db.session.commit()

class User(db.Model,UserMixin): # Classe com ORM - criar tabela usuário
    __tablename__="users" # Cria nome da tabela users
   
    # Inicio colunas  
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(64),unique=True, nullable=False)
    senha_hash = db.Column(db.String(256), nullable=False)
    criado_em = db.Column(db.DateTime,nullable=False)
    # modificado_em = db.column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, default = True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id")) # Coluna de papeis - chave estrangeira de Role()
    # Término colunas tabela

    def __init__(self) -> None: # Método cria data/hora automático
        self.criado_em = datetime.now() 
        self.modificado_em = datetime.now()
        if not self.role:
            self.role = Role.query.filter_by(padrao=True).first()

    @property
    def senha(self):
        raise AttributeError("Este não é um atributo que possa ser lido")

    @senha.setter
    def senha(self, valor):
        self.senha_hash = generate_password_hash(valor)

    def verify_password(self, senha):
        return check_password_hash(self.senha_hash, senha)

 

class Role(db.Model): # Classe cria tabela de papeis
    __tablename__= "roles" # Cria nome da tabela roles

    # Inicio colunas
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(16), nullable= False)
    users = db.relationship("User", backref="role") # Cria relacionamento com User()
    padrao = db.Column(db.Boolean, default=False, index=True)
    # Término colunas 