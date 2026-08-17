from pathlib import Path
import json
import bcrypt
import jwt
import datetime
from config import *
BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "data" / "users.json"

class VortNotFoundError(Exception):
    pass

def load_vortim_for_parsha(parsha_name):
  folder = Path("data/parshiot") / parsha_name 
  if not folder.is_dir():
    return {"error": "Parsha not found"}, 404
  vortim = []
  for file in folder.glob("*.json"):
    try:
      with open(file , "r" , encoding="utf-8") as f:
         vort = json.load(f)
         vort["is_long"] = is_long(vort["text"])
         vortim.append(vort)
    except FileNotFoundError:
        return {"error": "File not found"}, 404
  return vortim , 200

def load_single_vort(parsha_name, vort_id):
  folder = Path("data/parshiot") / parsha_name
  if not folder.is_dir():
    return {"error": "Parsha not found"}, 404
  for file in folder.glob("*.json"):
    try:
      with open (file , "r" , encoding="utf-8") as f:
         vort = json.load(f)
    except FileNotFoundError:
          return {"error": "File not found"} , 404
    if vort["id"] == vort_id:
      vort["is_long"] = is_long(vort["text"])
      return vort
  raise VortNotFoundError ("Vort not found")

def is_long(text):
  list_text = text.split("\n")
  if len(list_text) > 20:
    return True
  return False

def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes,bcrypt.gensalt())
    return hashed.decode()

def save_new_users(username , password):
  with open (USERS_FILE , "r" , encoding="utf-8") as file:
      users = json.load(file)
      users[username] = password
  with open (USERS_FILE , "w" , encoding="utf-8") as file:
      json.dump(users , file)

def verify_password(password, hashed):
  if bcrypt.checkpw(password.encode(),hashed.encode()):
     return True
  else:
     return False
   
def create_token(username):
   exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
   paload = {"username" :username , "exp" :exp}
   token = jwt.encode(paload , JWT_SECRET_KEY)
   return token
  