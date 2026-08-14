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
    return {
  "vortim": [
    {
      "id": 1,
      "title": "כוחה של התחלה",
      "text": "רעיון קצר על משמעות ההתחלה בפרשה."
    },
    {
      "id": 2,
      "title": "אמונה ובחירה",
      "text": "רעיון קצר נוסף על המסר המרכזי של הפרשה."
    }
  ]
} , 200
@app.route("/parshiot/<parsha>/vortim/<vort_id>")
def vort(parsha , vort_id):
    return {
  "id": 1,
  "title": "כוחה של התחלה",
  "text": "כל התחלה חדשה דורשת החלטה לעשות את הצעד הראשון."
} , 200
@app.route("/current")
def current():
    return {
  "current": "ecev"
} , 200

app.run(debug=True)