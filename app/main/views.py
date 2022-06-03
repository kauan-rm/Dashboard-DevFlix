from app.main import main
from flask import Flask, render_template, request, flash, redirect, url_for, make_response

@main.route("/", methods=['GET','POST'])
def index():
    return render_template("base.html")