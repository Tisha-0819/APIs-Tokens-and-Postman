# Task 2: Use Postman to send a POST request with JSON data to your local Flask app.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is Running Successfully"

@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.json
    return jsonify({
        "message": "User added successfully",
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True)
