from flask import Flask, render_template, redirect, session, request
from flask_app.models import sasquatch
from flask_app import app


# create sasquatch controller
@app.route('/sasquatchs/create')
def create_page():
    if 'user_id' not in session: return redirect('/')
    return render_template('create_sasquatch.html')

@app.post('/sasquatchs/create')
def create_sasquatch():
    if 'user_id' not in session: return redirect('/')
    if sasquatch.Sasquatch.create_sasquatch(request.form):
        return redirect('/sasquatchs')
    return redirect('/sasquatchs/create')


# read sasquatch controller
@app.route('/sasquatchs/view/<int:id>')
def view_sasquatchs(id):
    if 'user_id' not in session: return redirect('/')
    this_sasquatch = sasquatch.Sasquatch.get_sasquatch_by_id_w_host(id)
    return render_template('sasquatch_details.html', sasquatch = this_sasquatch)


# update sasquatch controller
@app.route('/sasquatchs/edit/<int:id>')
def edit_page(id):
    if 'user_id' not in session: return redirect('/')
    this_sasquatch = sasquatch.Sasquatch.get_sasquatch_by_id_w_host(id)
    return render_template('edit_sasquatch.html', sasquatch = this_sasquatch)

@app.post('/sasquatchs/edit')
def edit_sasquatch():
    if 'user_id' not in session: return redirect('/')
    if sasquatch.Sasquatch.update_sasquatch(request.form):
        return redirect('/sasquatchs')
    return redirect(f'/sasquatchs/edit/{request.form["id"]}')

# delete sasquatch controller

@app.route('/sasquatchs/delete/<int:id>')
def delete_sasquatch(id):
    if 'user_id' not in session: return redirect('/')
    sasquatch.Sasquatch.delete_sasquatch_by_id(id)
    return redirect('/sasquatchs')