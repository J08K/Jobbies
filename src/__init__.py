import flask
from src import db

from flask import render_template

app = flask.Flask(__name__)

# Initialize the db
database = db.JobbiesDB()


@app.route("/", methods=["GET"])
def index():
    count = database.get_count()

    print(f"Current count: {count}")
    
    return render_template("index.html", hobby_count=count)
            

@app.route("/api/add", methods=["GET"])
def get_count():
    new_count = database.add_one()
    
    return flask.jsonify({
        "status": "success",
        "new_count": new_count
    })