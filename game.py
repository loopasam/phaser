from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('part10.html')


@app.route("/assets/<file>")
def assets(file):
    return send_from_directory(app.static_folder, file)
