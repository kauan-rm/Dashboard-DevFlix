from app.auth import auth
from flask import render_template, request, redirect, url_for, flash
from app import db
from config import Config
from app.models import User
from ..email import send_email 
from flask_login import login_required, current_user, login_user, logout_user
from app.serializer import Serializer
secret_key = Config.SECRET_KEY


@auth.route("/login") # Rota de login
def login():
    return render_template("login.html")

@auth.route("/do_login", methods=['POST']) # Rota de login por post
def do_login():  
    if request.form:
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.verify_password(request.form['senha']): 
            login_user(user)
            return redirect(url_for('main.index'))
        return redirect(url_for('auth.login'))
    return render_template("login.html") # Renderiza arquivo html pasta templates


@auth.route('/registro') # Rota de registro 
def registro():
    return render_template("register.html")

@auth.route('/do_register', methods=['POST'])
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
                token = Serializer.generate_confirmation_token(secret_key, user.id)
                send_email(user.email, 'Confirmação de E-mail',
                'confirm', user=user, token=token)
                flash('Um e-mail de confirmação foi enviado ao seu email!')
                return redirect(url_for('main.index'))
    return render_template('register.html')


@auth.route('/confirm/<token>')#confirma email
@login_required
def confirm(token):

    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if Serializer.confirm(secret_key, current_user, token):
        current_user.confirmed = True
        db.session.add(current_user) 
        db.session.commit()
        flash('Conta confirmada. Obrigado!')
    else:
        flash('O link de confirmação está inválido ou expirou!')
    return redirect(url_for('main.index'))

@auth.route('/confirm')#confirma email
@login_required
def resend_confirmation():
    token = Serializer.generate_confirmation_token(secret_key,current_user)
    send_email(current_user.email, 'Confirme Sua Conta',
    'confirm', user=current_user, token=token)
    flash('Um novo e-mail de confirmação foi enviado para seu e-mail!')
    return redirect(url_for('auth.register'))

@auth.route("/logout", methods=['GET','POST'])
def logout():
    logout_user(current_user)
    return redirect(url_for('auth.login'))

