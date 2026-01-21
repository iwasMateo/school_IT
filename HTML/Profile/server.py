print("Test")
from flask import Flask, request, jsonify, send_from_directory
import json
import os



app = Flask(__name__, static_folder="static")

FILE = os.path.join("static", "profile.json")
UPLOAD_FOLDER=os.path.join(".", "static")

@app.get("/")
def index():
    return send_from_directory(".", "JakobMateo.html")

@app.post("/add")
def add_person():
    print("POST /add received")
    name = request.form.get("name")
    alt = request.form.get("alt")
    description = request.form.get("description")
    pfp=request.files.get("pfp")
    
    if not name or not alt or not description:
        return jsonify({"error":"missing data"}), 400


    image_filename = None
    if pfp:
        image_filename = pfp.filename
        save_path = os.path.join(UPLOAD_FOLDER, image_filename)
        pfp.save(save_path)
    
    new_entry = {"name": name, "image": image_filename, "alt": alt, "description": description}

    if not os.path.exists(FILE):
        data = []
    else:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    data.append(new_entry)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Saved")
    return jsonify({"status": "ok", "entry": new_entry})

if __name__ == "__main__":
    app.run(debug=True)