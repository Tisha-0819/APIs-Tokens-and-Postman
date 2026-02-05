# Task 3: Build GET, POST, PUT, DELETE Flask API and test it on Postman.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data (acts like database)
users = [
    {"id": 1, "name": "Tisha", "age": 21},
    {"id": 2, "name": "Ram", "age": 25}
]

# GET: Fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# POST: Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT: Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            return jsonify(user)
    return {"error": "User not found"}, 404

# DELETE: Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"error": "User not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)


# You can test this API using Postman by sending GET, POST, PUT, and DELETE requests to the respective endpoints.