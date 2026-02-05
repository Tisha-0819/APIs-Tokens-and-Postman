# Task 6: Create a Flask API that takes a number and returns its square via POST method.
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["POST"])
def square_number():
    data = request.json
    num = data.get("number")

    return jsonify({
        "number": num,
        "square": num * num
    })

if __name__ == "__main__":
    app.run(debug=True)

    
# To test this API, you can use Postman or curl to send a POST request with a JSON body like:
# {
#     "number": 4
# }
# The response will be:
# {
#     "number": 4,
#     "squared": 16
# }
