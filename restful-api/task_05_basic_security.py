#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this to a random secret key

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

# JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")

# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(port=5000)
