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
    if vortim is None:
        return {"error": "Parsha not found"}, 404
    token = None
    auth_header = request.headers.get("Authorization")
    if auth_header:
        token = auth_header.split(" ")[1]
    vortim = load_vortim_for_parsha(parsha)
    if decode_token(token):
        return vortim , 200
    else:
        for vort in vortim:
            if vort["is_long"]:
                vort["text"] = ("This vort is available to registered users only. \n"
                " Please sign up or log in to view the full vort.")
        return vortim , 200
    
@app.route("/parshiot/<parsha>/vortim/<vort_id>")
def vort(parsha, vort_id):
    try:
        vort = load_single_vort(parsha, vort_id)

        if vort is None:
            return {"error": "Parsha not found"}, 404

        token = None
        auth_header = request.headers.get("Authorization")

        if auth_header:
            token = auth_header.split(" ")[1]

        if decode_token(token) or not vort["is_long"]:
            return vort, 200

        return (
            "This vort is available to registered users only. "
            "Please sign up or log in to view the full vort"
        ), 403

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