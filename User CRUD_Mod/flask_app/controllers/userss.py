from flask import Flask, render_template, redirect, session, request
from flask_app.models.users import User

from flask_app import app

@app.route('/')          
def index():
    return render_template("user.html")

@app.route("/edituser")
def edituser():
    users = User.get_all()
    return render_template('edituser.html', users=users)

@app.route("/edit/<int:id>")
def edit(id):
    user = User.read(id)
    return render_template("edit.html", user = user)

@app.route("/read/<int:id>")
def read(id):
    user = User.read(id)
    return render_template("read.html", user = user)


@app.route("/process", methods=['POST'])
def answer(): 
    data = {
        'first_name':request.form["first_name"],
        'last_name':request.form["last_name"],
        'email':request.form["email"],
    }
    User.save(data)
    return redirect("/edituser")

@app.route("/delete/<int:id>")
def deletes(id):    
    User.delete(id)
    return redirect("/edituser")


@app.route("/edit", methods = ['POST'])
def updated():
    User.edit(request.form)
    return redirect("/edituser")

