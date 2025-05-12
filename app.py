from cs50 import SQL
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, '/static')

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///scores.db")

@app.route("/")
def index():

    scores = db.execute("SELECT * FROM scores ORDER BY datetime DESC LIMIT 10;")

    # Return scores
    return render_template("index.html", scores=scores)

@app.route('/process', methods=['POST'])
def process():
    # retrieves the data sent from JavaScript
    data = request.get_json()
    # add data to DB
    db.execute("INSERT INTO scores (winner_name, player, score) VALUES (?,?,?);", data['winner'], data['player'], data['score'])
    # returns sucessful result to JavaScript
    return jsonify(result=data)
