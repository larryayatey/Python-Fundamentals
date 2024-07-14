from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
from flask_app import app

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)


@app.route('/dojos/create', methods=['POST'])
def ans():
    data = {
        'name':request.form["name"],
    }
    Dojo.save(data)
    return redirect('/')



@app.route('/dojoshow/<int:dojo_id>')
def dojoshow(dojo_id):
    dojo = Dojo.get_dojo_ninjas(dojo_id)
    return render_template('dojoshow.html', all_dojos = dojo)

