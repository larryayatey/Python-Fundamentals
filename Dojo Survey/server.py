from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)  
app.secret_key = "asdaddagd"

@app.route('/')          
def index():
    return render_template("DojoSurvey.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/redirect')
def direct():
    return redirect("DojoSurvey.html")

@app.route("/process", methods=["POST"])
def survey():
    session['Name'] = request.form['Name'] 
    session['location'] = request.form['states'] 
    session['Favorite'] = request.form['language'] 
    session['Comment'] = request.form['comment'] 

    return redirect("/result")

if __name__=="__main__":      
    app.run(debug=True)    
