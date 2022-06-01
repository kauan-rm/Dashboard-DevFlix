from app import db
from datetime import datetime

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(64),unique=True, nullable=False)
    senha = db.Column(db.String(64), nullable=False)
    criado_em = db.Column(db.DateTime,nullable=False)
    #modificado_em = db.column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, default = True)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __init__(self) -> None:
        self.criado_em = datetime.now()

class Role(db.Model):
    __tablename__= "roles"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(16), nullable= False)
    users = db.relationship("User", backref="role")