from app.auth import auth
from flask import Flask, render_template, request, flash, redirect, url_for, make_response


@auth.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/registro')
def registro():
    return render_template("register.html")

@auth.route("/logout", methods=['GET','POST'])
def logout():
    return render_template("login.html")