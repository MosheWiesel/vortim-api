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
    vort = load_single_vort(parsha , vort_id)
    is_long_vort = is_long(parsha , vort_id)
    return vort , "/n is long vort : " , is_long_vort
@app.route("/current")
def current():
    return {
  "current": "ecev"
} , 200

app.run(debug=True)