# Inicio import
from app.auth import auth
from flask import render_template, request, redirect, url_for, flash
from app import db
from config import Config
from app.models import User
from ..email import send_email 
from flask_login import login_required, current_user, login_user, logout_user
from app.serializer import Serializer
secret_key = Config.SECRET_KEY
# Termino Import

@auth.route("/login") # Rota de login
def login():
    return render_template("login.html")

@auth.route("/do_login", methods=['POST']) # Rota de login por post
def do_login():  
    if request.form:
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.verify_password(request.form['senha']): 
            login_user(user)
            return redirect(url_for('main.home'))
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.login')) # Renderiza arquivo html pasta templates


@auth.route('/registro') # Rota de registro 
def registro():
    return render_template("register.html")

@auth.route('/do_register', methods=['POST']) # Rota de registro por post
def do_register():
    if request.form:
        if request.form['senha'] == request.form['conf_senha']:
            user = User()
            user.nome = request.form['nome']
            user.sobrenome = request.form['sobrenome']
            user.email = request.form['email']
            user.cpf = request.form['cpf']
            user.senha = request.form['senha']
            if(user.email):
                db.session.add(user)
                db.session.commit()
                token = Serializer.generate_token(secret_key, user.id)
                send_email(user.email, 'Confirmação de E-mail',
                'confirm', user=user, token=token)
                flash('Um e-mail de confirmação foi enviado ao seu email!')
                return redirect(url_for('main.index'))
    return redirect(url_for('auth.registro'))

@auth.route('/confirm/<token>')
def confirm(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    if Serializer.verify_auth_token(secret_key,token):
        u = Serializer.verify_auth_token(secret_key,token)
        u.confirmed = True 
        db.session.add(u)
        db.session.commit()
        login_user(u)
        flash('Obrigado por confirmar seu email!')
        return redirect(url_for('main.home'))
    else:
        flash('O link de confirmação está inválido ou expirou!')
    return redirect(url_for('auth.registro'))

@auth.route('/resend_confirmation')#confirma email
@login_required
def resend_confirmation():
    token = Serializer.generate_confirmation_token(secret_key,current_user)
    send_email(current_user.email, 'Confirme Sua Conta',
    'confirm', user=current_user, token=token)
    flash('Um novo e-mail de confirmação foi enviado para seu e-mail!')
    return redirect(url_for('auth.register'))

@auth.route("/logout") # Rota de logout
def logout():
    logout_user() #funcao logout do flask
    return redirect(url_for('auth.login'))    