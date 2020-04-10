from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/ops")
def opisanie():
    return render_template("ops.html")

@app.route("/pred/<name>")
def reklama(name):
    return render_template("pred.html", name=name)