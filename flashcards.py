from datetime import datetime
from tempfile import TemporaryFile
from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)


counter = 0


@app.route("/")
def welcome():
    global counter
    counter += 1
    return render_template("welcome.html",
                           message="This page has been served " + str(counter) + " times.",
                           cards=db)


@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page has been served " + str(counter) + " times."


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route('/api/card/')
def api_card_list():
    return jsonify(db)

@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)