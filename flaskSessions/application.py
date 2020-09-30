from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    # if the existing session does not contain any notes, create an empty note list
    if session.get("notes") is None:
        session["notes"] = []  # makes the sessions unique to each user
    if request.method == "POST":
        note = request.form.get("note")
        print(note)
        session["notes"].append(note)
        print(session)
    return render_template("index.html", notes=session["notes"])
