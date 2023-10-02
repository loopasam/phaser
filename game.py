from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/mario")
def mario():
    return render_template('mario.html')

@app.route("/tile_explorer")
def tile_explorer():
    return render_template('tile_explorer.html')


@app.route("/assets/<file>")
def assets(file):
    return send_from_directory(app.static_folder, file)
