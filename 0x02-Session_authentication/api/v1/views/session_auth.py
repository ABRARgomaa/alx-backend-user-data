#!/usr/bin/env python3
"""session auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from flask import Flask, request, jsonify, session
from api.v1.views import app_views
import os


cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
app = Flask(__name__)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login method"""
    user_email = request.form.get('email')
    usre_pass = request.form.get('password')
    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not usre_pass:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': user_email})
    if not user or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user1 = user[0]
    if not user.is_valid_password(usre_pass):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user1.id)
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
