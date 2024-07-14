from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/play")
def play():
    return render_template("play.html", num = 3)

@app.route("/play/<int:num>")
def play_mult(num):
    return render_template("play.html", num = int (num) )

@app.route("/play/<int:num>/<string:color>")
def play_mult_color(num, color):
    return render_template("play.html", num = int (num), color = color)

if __name__=="__main__":      
    app.run(debug=True)   