from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route("/")
def index():
    dateNow = datetime.datetime.now()
    newYear = dateNow.month == 1 and dateNow.day == 1
    return render_template("index.html", newYear=newYear)

   # --alternate way but is inefficient--
   # if newYear:
   #     return render_template("yes.html")
   # else:
   #     return render_template("no.html")


@app.route("/loops")
def loopsExample():
    names = ["Christian", "Eder", "Dad", "Mom"]
    return render_template("loops.html", names=names)
