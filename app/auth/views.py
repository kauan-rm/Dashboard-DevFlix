from app.auth import auth
from flask import Flask, render_template, request, flash, redirect, url_for, make_response


@auth.route("/login", methods=['GET','POST'])
def login():
    dados = request.form
    if dados:
        user = dados['user']
        if user:
            flash("Usuario logado com sucesso")
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('user', user)
            return resp
        flash("Usuario invalido")
    return render_template("login.html", user=request.cookies.get('user'))

@auth.route('/registro')
def registro():
    return render_template("register.html",  user=request.cookies.get('user'))

@auth.route('/logout')
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie('user', '', expires=0)

    return resp
