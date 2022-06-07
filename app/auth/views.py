# Inicio import
from app.auth import auth 
from flask import Flask, render_template, request, flash, redirect, url_for, make_response
# Termino Import

@auth.route("/login", methods=['GET','POST']) # Rota de login
def login():  
    return render_template("login.html") # Renderiza arquivo html pasta templates

@auth.route('/registro') # Rota de registro 
def registro():
    return render_template("register.html")  # Renderiza arquivo html pasta templates

@auth.route("/logout", methods=['GET','POST']) # Rota de logout
def logout():    
    return render_template("login.html")  # Renderiza arquivo html pasta templates