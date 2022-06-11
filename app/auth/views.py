from app.auth import auth
from flask import render_template, requests, redirect, url_for, flash
from app import db
from app.models import user
from flask_mail import send_email 
from flask_login import login_required, current_user

@auth.route("/login", methods=['POST'])
def login():
    
    return render_template("login.html")


#
@auth.route('/register', methods=['POST'])
def register():
    #verificar se o botao criar foi clicado e enviado os dados
    email = requests.form('email')
    if(email):
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirme Sua Conta',
        'auth/email/confirm', user=user, token=token)
        flash('Um e-mail de confirmação foi enviado ao seu email!')
        return redirect(url_for('main.index'))
    return render_template('register.html')


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('Conta confirmada. Obrigado!')
    else:
        flash('O link de confirmação está inválido ou expirou!')
    return redirect(url_for('auth.register'))

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirme Sua Conta',
    'auth/email/confirm', user=current_user, token=token)
    flash('Um novo e-mail de confirmação foi enviado para seu e-mail!')
    return redirect(url_for('auth.register'))

@auth.route("/logout", methods=['GET','POST'])
def logout():
    
    return render_template("login.html")