
import flask
import db
from flask import render_template, jsonify

app = flask.Flask(__name__)
app.debug = True

DB = db.JobbiesDB()

@app.route('/')
def index():
    return render_template('index.html', hobby_count=DB.get_count())

@app.route("/api/add")
def add():
    new_count = DB.add_one()
    
    return jsonify({
        "status": "success",
        "new_count": new_count,
    })

if __name__ == '__main__':
    app.run()