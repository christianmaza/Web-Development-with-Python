from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/<string:name>")
def routeName(name):
    name = name.capitalize()
    return render_template("stringInput.html", name=name)
