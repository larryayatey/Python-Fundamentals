from flask import Flask, render_template, redirect, session, request
from flask_app.models.login import Login
from flask_app.models import sasquatch
from flask_app import app


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/sasquatchs')
def log():
    if 'user_id' not in session: return redirect('/')
    sasquatchs = sasquatch.Sasquatch.get_all_sasquatch_w_hosts()
    return render_template("sasquatchs.html", sasquatchs = sasquatchs)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create', methods=['POST'])
def create():
    user_id = Login.save(request.form)
    if user_id:
        return redirect('/sasquatchs')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if Login.login(request.form):
        return redirect('/sasquatchs')
    return redirect('/')


