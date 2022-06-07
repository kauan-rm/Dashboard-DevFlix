# Inicio import
from app.main import main
from flask import Flask, render_template, request, flash, redirect, url_for, make_response
# Termino import
@main.route("/", methods=['GET','POST']) # Rota index em desenvolvimento
def index():
    return render_template("base.html")  # Renderiza arquivo html pasta templates