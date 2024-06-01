#!/usr/bin/python3

from flask import Flask, jsonify, request

# Instantiate a Flask web server from the Flask module
app = Flask(__name__)

# In-memory dictionary to store user data
users = {}


# Define a route for the root URL ("/") and create a function to handle this route
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Create a new route /data to return a list of all usernames stored in the API
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


# Add a route to return OK status
@app.route('/status')
def get_status():
    return "OK"

# Add a dynamic route to get user information by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Add a route to handle POST requests to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "username": username,
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }
    return jsonify({"message": "User added", "user": users[username]}), 200

# Run the Flask development server
if __name__ == "__main__":
    app.run(port=5000)
