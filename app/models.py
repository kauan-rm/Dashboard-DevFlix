from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #carregamento do usuário

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    sobrenome = db.Column(db.String(128))
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    criado_em = db.Column(db.DateTime, nullable=False)
    #modificado_em = db.column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, default = True)
    confirmed = db.Column(db.Boolean, default=False) #teste email

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    @property
    def senha(self):
        raise AttributeError("Este não é um atributo que possa ser lido")

    @senha.setter
    def senha(self, valor):
        self.senha_hash = generate_password_hash(valor)

    def verify_password(self, senha):
        return check_password_hash(self.senha_hash, senha)


    def __init__(self) -> None:
        self.criado_em = datetime.now()

class Permission: # Classe de permissões
    USAR = 1
    CRIAR = 2
    DESABILITAR = 4
    ADMIN = 8          


class Role(db.Model):
    __tablename__= "roles"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(16), nullable= False)
    users = db.relationship("User", backref="role")

    @staticmethod # Método statico
    def insert_roles(): # Método de papéis
        roles ={
            'desabilitado' :[],
            'usuario comum':[Permission.USAR],
            'financeiro':[Permission.DESABILITAR],
            'moderador':[Permission.CRIAR],
            'administrador':[Permission.USAR, Permission.CRIAR, Permission.DESABILITAR, Permission.ADMIN]
        }
        padrao = 'usuario comum'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if not role:
                role = Role()
                role.nome = r

            role.reset_permission()
            for permissao in role[r]:
                role.add_permission(permissao)
            role.padrao =(role.nome == padrao)
            db.session.add(role)
        db.session.commit()


        


    def add_permission(self,permissao):
        if not self.has_permission(permissao):
         self.permissao += permissao

    def remove_permission(self, permissao):
        self.permissao -= permissao

    def reset_permission(self):
        self.permissao = 0 

    def has_permission(self, permissao):
        return self.permissao & permissao == permissao