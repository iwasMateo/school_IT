from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="static")

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(debug=True)