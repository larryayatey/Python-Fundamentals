from flask import Flask, render_template, redirect, session, request
from flask_app.models import recipe
from flask_app import app


# create recipe controller
@app.route('/recipes/create')
def create_page():
    if 'user_id' not in session: return redirect('/')
    return render_template('create_recipe.html')

@app.post('/recipes/create')
def create_recipe():
    if 'user_id' not in session: return redirect('/')
    if recipe.Recipe.create_recipe(request.form):
        return redirect('/recipes')
    return redirect('/recipes/create')


# read recipe controller
@app.route('/recipes/view/<int:id>')
def view_recipes(id):
    if 'user_id' not in session: return redirect('/')
    this_recipe = recipe.Recipe.get_recipe_by_id_w_host(id)
    return render_template('recipe_details.html', recipe = this_recipe)


# update recipe controller
@app.route('/recipes/edit/<int:id>')
def edit_page(id):
    if 'user_id' not in session: return redirect('/')
    this_recipe = recipe.Recipe.get_recipe_by_id_w_host(id)
    return render_template('edit_recipe.html', recipe = this_recipe)

@app.post('/recipes/edit')
def edit_recipe():
    if 'user_id' not in session: return redirect('/')
    if recipe.Recipe.update_recipe(request.form):
        return redirect('/recipes')
    return redirect(f'/recipes/edit/{request.form["id"]}')

# delete recipe controller

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session: return redirect('/')
    recipe.Recipe.delete_recipe_by_id(id)
    return redirect('/recipes')