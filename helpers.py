from pathlib import Path
import json
import bcrypt
import jwt
import datetime
from config import *

BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "data" / "users.json"
ADMINS_FILE = BASE_DIR / "data" / "admins.json"
PARSIOT_DIR = BASE_DIR / "data" / "parshiot"

class VortNotFoundError(Exception):
    pass
def how_meny_vortim(parash):
    folder = PARSIOT_DIR / parash
    num = 0
    for file in folder.glob("*.json"):
        num += 1
    return num
   
def load_vortim_for_parsha(parsha_name):
  folder = Path("data/parshiot") / parsha_name 
  if not folder.is_dir():
    return None
  vortim = []
  for file in folder.glob("*.json"):
    try:
      with open(file , "r" , encoding="utf-8") as f:
         vort = json.load(f)
         vort["is_long"] = is_long(vort["text"])
         vortim.append(vort)

    except FileNotFoundError:
        return {"error": "File not found"}
  return vortim

def load_single_vort(parsha_name, vort_id):
  folder = Path("data/parshiot") / parsha_name
  if not folder.is_dir():
      return None
  for file in folder.glob("*.json"):
    try:
      with open (file , "r" , encoding="utf-8") as f:
         vort = json.load(f)
    except FileNotFoundError:
          return {"error": "File not found"}
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

def decode_token(token):  
  if not token:
    return None
  try:
    payload = jwt.decode(token , JWT_SECRET_KEY, algorithms=["HS256"])
    return payload["username"]
  except jwt.ExpiredSignatureError:
   return None
  except jwt.InvalidTokenError:
   return None
  
def load_admins():
    if not ADMINS_FILE.exists():
      return []
    with open(ADMINS_FILE , "r" , encoding="utf-8") as file:
        return json.load(file)
      
def check_admin (username):
    admins = load_admins()
    return username in admins

def check_parsha_exsist(parsha):
    parsha_path = PARSIOT_DIR / parsha
    return parsha_path.is_dir()
   

def validate_vort(data):
  if not isinstance(data, dict):
    return "Invalid JSON object"
  if not (all(key in data for key in ["title", "author", "text"])):
    return "MissingFields"
  for key , item in data.items():
    if not isinstance(key , str) or not isinstance(item, str) or key.strip() == "" or item.strip() == "":
      return "FieldsAreWrong"
  if not (3 <= len(data["title"]) <= 100) or not (20 <= len(data["text"]) <= 1000000):
    return "FieldsAreWrong"
  return data
  
