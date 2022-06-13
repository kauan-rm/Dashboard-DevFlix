# Inicio import
from app.auth import auth 
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from ..models import User
from app import db
# Termino Import

@auth.route("/login") # Rota de login
def login():
    return render_template("login.html")

@auth.route("/do_login", methods=['POST']) # Rota de login
def do_login():  
    if request.form:
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.senha_hash == request.form['senha']: #verify_password(request.form['senha']):
            login_user(user)
            return redirect(url_for('main.index'))
        return redirect(url_for('auth.login'))
    return render_template("login.html") # Renderiza arquivo html pasta templates


@auth.route('/registro') # Rota de registro 
def registro():
    return render_template("register.html")

@auth.route('/do_register', methods=['POST']) # Rota de registro 
def do_register():
    if request.form and request.form['senha']==request.form['conf_senha']:    
        user = User()
        user.nome = request.form['nome']
        user.cpf = request.form['cpf']
        user.email = request.form['email']
        user.senha_hash = request.form['senha']
        db.session.add(user)
        db.session.commit()
        return "dados inseridos no banco de dados" # Alan aqui sua parte
    return render_template("register.html")  # Renderiza arquivo html pasta templates
    

@auth.route("/logout", methods=['GET','POST']) # Rota de logout
def logout():
    logout_user() #funcao logout do flask
    return redirect(url_for('auth.login'))    