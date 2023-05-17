from flask import Flask, redirect, render_template, request, jsonify
from db import display_jobs_from_db
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def home():
    jobs = display_jobs_from_db()
    return render_template('index.html', jobs=jobs)

@app.route("/api/jobs")
def jobs():
    jobs = display_jobs_from_db()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)