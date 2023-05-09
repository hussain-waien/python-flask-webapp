from flask import Flask, redirect, render_template, request, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 0,
        'title': 'Data Scientist',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 55000'
    },
    {
        'id': 1,
        'title': 'Backend Web Developer',
        'location': 'Karachi, Pakistan',
        'salary': 'Rs. 60000'
    },
    {
        'id': 2,
        'title': 'Frontend Web Developer',
        'location': 'Islamabad, Pakistan',
        'salary': 'Rs. 45000'
    },
    {
        'id': 3,
        'title': 'Graphic Designer',
        'location': 'Faisalabad, Pakistan',
        'salary': 'Rs. 40000'
    },
    {
        'id': 4,
        'title': 'People Manager',
        'location': 'Faisalabad, Pakistan',
        'salary': 'Rs. 70000'
    },
]

@app.route("/")
def home():
    return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)