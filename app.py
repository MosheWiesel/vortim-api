from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def status():
    return { "status": "server is running" } , 200
if __name__ == "__main__":
    app.run(debug=True)