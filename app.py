from helpers import *
from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def status():
    return { "status": "server is running" } , 200

@app.route("/parshiot")
def parshiot():
    return {
  "parshiot": ["Bereshit", "Noach", "Lech Lecha"]
} , 200

@app.route("/parshiot/<parsha>/vortim")
def vortim(parsha):
    vortim = load_vortim_for_parsha(parsha)
    return vortim
@app.route("/parshiot/<parsha>/vortim/<vort_id>")
def vort(parsha , vort_id):
    try:
        return load_single_vort(parsha , vort_id)
    except VortNotFoundError:
        return {"error": "Vort not found"}, 404
@app.route("/current")
def current():
    return {
  "current": "ecev"
} , 200

app.run(debug=True , port=5000)