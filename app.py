from helpers import *
from config import *
from flask import *
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
    return get_current_parsha() , 200

@app.route("/current/vortim")
def current_vortim():
    return load_vortim_for_parsha(get_current_parsha())

@app.route ("/register" , methods= ["POST"])
def register ():
    data = request.get_json()
    username = data.get("username")
    password = hash_password(data.get("password"))
    with open (USERS_FILE , "r" , encoding="utf-8") as file:
        users = json.load(file)
        if username in users:
            return f"eroor user already exsist" , 400
    save_new_users(username , password)
    return "saved successfully" , 201
@app.route("/login" , methods= ["POST"])
def login ():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    with open (USERS_FILE , "r" , encoding="utf-8") as file:
            users = json.load(file)
            if not username in users:
                return f"eroor user not exsist" , 401
            else:
                saved_hash = users[username]
    if not verify_password(password , saved_hash):
        return f"wrong password" , 401
    else:
        return create_token(username)
        
            
            
            
    

app.run(debug=True , port=5000)