from flask import Flask, render_template, redirect, session, request
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo
from flask_app import app

@app.route('/newninja')
def newninja():
    dojos = Dojo.get_all()
    return render_template('newninja.html', all_dojos = dojos)





@app.route('/ninjas/create', methods=['POST'])
def answer():
    Ninja.save(request.form)
    return redirect('/dojoshow/'+ request.form['dojo_id'])







