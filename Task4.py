# Task 4: Add Bearer Token authentication to your Flask API.

from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)
TOKEN = "mysecrettoken123"

def auth(f):
    @wraps(f)
    def wrap():
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {"error": "invalid or missing token"}, 401

        parts = auth_header.split()

        if parts[0] != "Bearer" or parts[1] != TOKEN:
            return {"error": "invalid or missing token"}, 401

        return f()
    return wrap

@app.route("/users", methods=["GET"])
@auth
def users():
    return {"message": "Access granted"}

app.run(debug=True)
