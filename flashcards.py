from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


counter = 0

@app.route("/")
def welcome():
    global counter
    counter += 1
    return render_template("welcome.html",
                           message="This page has been served " + str(counter) + " times.")


@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page has been served " + str(counter) + " times."