from pathlib import Path
import json
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

  