from flask import Flask, render_template, redirect, request, session

app = Flask(__name__) 
app.secret_key = "helloWorld"

@app.route("/")
def counter():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 1
    return render_template('counter.html', count = session)

@app.route('/add')
def add():
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route("/destroy")
def destroy():
    session.clear()
    session["count"] = 0
    return redirect("/")

if __name__=="__main__":      
    app.run(debug=True) 