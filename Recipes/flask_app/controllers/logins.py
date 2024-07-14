from flask import Flask, render_template, redirect, session, request
from flask_app.models.login import Login
from flask_app.models import recipe
from flask_app import app


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/recipes')
def log():
    if 'user_id' not in session: return redirect('/')
    recipes = recipe.Recipe.get_all_recipes_w_hosts()
    return render_template("recipes.html", recipes = recipes)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create', methods=['POST'])
def create():
    user_id = Login.save(request.form)
    if user_id:
        return redirect('/recipes')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if Login.login(request.form):
        return redirect('/recipes')
    return redirect('/')


