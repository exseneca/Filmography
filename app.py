from flask import Flask, render_template, request 
from filmography import Filmography
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list', methods=["POST"])
def list():
    user_input = request.form.get("string")
    F = Filmography()
    films = F.get_films(user_input)
    return render_template("list.html", films=films, actor=user_input)