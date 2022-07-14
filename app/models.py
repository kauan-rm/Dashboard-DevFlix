# Inicio import bibliotecas
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Termino import biblioteca


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #carregamento do usuário

class Permission: # Classe de permissões
    USAR = 1
    CRIAR = 2
    DESABILITAR = 4
    ADMIN = 8  
   

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
            self.role = Role.query.filter_by(padrao=True).first() # Filtra os papéis para não serem duplicados

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
    nome = db.Column(db.String(16),  default=0)
    users = db.relationship("User", backref="role") # Cria relacionamento com User()
    padrao = db.Column(db.Boolean, default=False, index=True) # Define usuario como padrão
    # Término colunas 

    @staticmethod # Método statico
    def insert_roles(): # Método de papéis
        roles ={  # Inicio das definições de permissões dos papéis
            'desabilitado' :[],
            'usuario comum':[Permission.USAR],
            'financeiro':[Permission.CRIAR, Permission.DESABILITAR],
            'moderador':[ Permission.CRIAR],
            'administrador':[Permission.USAR, Permission.CRIAR, Permission.DESABILITAR, Permission.ADMIN]
        } # Término das definições de permissões dos papéis
        padrao = 'usuario comum' # Define usuário comum como padrão

        # Verificando se os papéis existem para criar um novo papel sem duplicar um já existente
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if not role:
                role = Role()
                role.nome = r

            # Reseta as pemissões para criar uma nova e adiciona os papéis banco de dados
            role.reset_permission()
            for permissao in role[r]:
                role.add_permission(permissao)
            role.padrao =(role.nome == padrao)
            db.session.add(role)
        db.session.commit()


        

    # Inicio dos métodos de permissões
    def add_permission(self,permissao):  # Adiciona permissão
        if not self.has_permission(permissao):
         self.permissao += permissao

    def remove_permission(self, permissao): # Remove permissão
        self.permissao -= permissao

    def reset_permission(self): # Reseta permissão
        self.permissao = 0 

    def has_permission(self, permissao): # Tem permissão
        return self.permissao & permissao == permissao

    # Témino dos métodos de permissões

class Imagem(db.Model): # Classe com ORM - criar tabela usuário
    __tablename__="tabela_imagens" # Cria nome da tabela users

    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(256), nullable=False)