from flask import Flask, render_template, redirect, session, request
from users import User

app = Flask(__name__) 
app.secret_key = "adfjdlh;a"

@app.route('/')          
def index():
    return render_template("user.html")

@app.route("/newuser")
def newuser():
    users = User.get_all()
    return render_template('newuser.html', users=users)

@app.route("/process", methods=['POST'])
def answer(): 
    data = {
        'first_name':request.form["first_name"],
        'last_name':request.form["last_name"],
        'email':request.form["email"],
    }
    User.save(data)
    return redirect("/newuser")


if __name__=="__main__":      
    app.run(debug=True)   