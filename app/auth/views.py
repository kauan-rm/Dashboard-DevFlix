# Inicio import
from app.auth import auth
from flask import render_template, request, redirect, url_for, flash
from app import db
from config import Config
from app.models import User
from ..email import send_email 
from flask_login import current_user, login_user, logout_user
from app.serializer import Serializer
secret_key = Config.SECRET_KEY
# Termino Import

@auth.route("/login") # Rota de login
def login():
    return render_template("login.html")

@auth.route("/do_login", methods=['POST']) # manipulação do post enviado pela rota Login
def do_login():  
    if request.form:
        user = User.query.filter_by(email=request.form['email']).first()
        if not user:    #verifica se o usuário existe no DB
            flash('Email não cadastrado.')
            return redirect(url_for('auth.login')) 
        if user.email == request.form['email'] and user.verify_password(request.form['senha']): 
            if not user.confirmed:        #verifica se o usuário está confirmado
                flash("Verifique se o email foi confirmado.")
                return redirect(url_for('auth.login'))          
            login_user(user)
            return redirect(url_for('main.home'))
        flash("Email ou senha inválidos")   #Senha inválida 
        return redirect(url_for('auth.login'))

    return redirect(url_for("auth.login"))#redireciona para a rota de login


@auth.route('/registro') # Rota de registro 
def registro():
    return render_template("register.html")

@auth.route('/do_register', methods=['POST']) # manipulação dos dados enviados pela rota Registro
def do_register():
    if request.form:
        if request.form['senha'] == request.form['conf_senha'] and request.form['email'] != '':
            user = User()
            user.nome = request.form['nome']
            user.sobrenome = request.form['sobrenome']
            user.email = request.form['email']
            if User.verify_cpf(request.form['cpf']):
                cpf = User.verify_cpf(request.form['cpf'])
                user.cpf = cpf
                user.senha = request.form['senha']
                db.session.add(user)
                db.session.commit()
                token = Serializer.generate_token(secret_key, user.id)
                send_email(user.email, 'Confirmação de E-mail',
                'confirm', user=user, token=token)
                flash('Um link de confirmação de conta, foi enviado ao seu e-mail!')
                return redirect(url_for('auth.login'))
            flash("CPF inválido!")    
    return redirect(url_for('auth.registro'))

    
@auth.route('/confirm/<token>')#Confirma email só funciona se o usuario já estiver logado e clicar no link de confirmação
def confirm(token):
    user_token = Serializer.verify_auth_token(secret_key, token)
    if user_token.confirmed: #Verifica se o user_id está com o atributo 'confimed' == True
        return redirect(url_for('main.home'))    
    if user_token: #Força o user_id a ser confirmado
        user_token.confirmed = True
        db.session.add(user_token)
        db.session.commit()
        flash('Obrigado por confirmar seu email!')
        return redirect(url_for('main.home'))
    flash('O link de confirmação está inválido ou expirou!')
    return redirect(url_for('auth.registro'))

@auth.route('/confirm')#confirma email
def resend_confirmation():
    token = Serializer.generate_confirmation_token(secret_key,current_user)
    send_email(current_user.email, 'Confirme Sua Conta',
    'confirm', user=current_user, token=token)
    flash('Um novo e-mail de confirmação foi enviado para seu e-mail!')
    return redirect(url_for('auth.registro'))

@auth.route("/logout") # Rota de logout
def logout():
    logout_user() #funcao logout do flask
    return redirect(url_for('auth.login'))    