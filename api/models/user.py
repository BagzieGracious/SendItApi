from flask import jsonify, json
import uuid
from werkzeug.security import  check_password_hash, generate_password_hash


class Users:

    users = []
    found_user = []

    def __init__(self, username=None, email=None):
        self.user_id = uuid.uuid4()
        self.username = username
        self.email = email

    def add_user(self, password):
        """
        Method for adding a user to data structures
        """
        user = {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": generate_password_hash(password, method='sha256')
        }
        Users.users.append(user)
        return jsonify({"success":True, "data": user}), 201

    def get_all_users(self):
        """
        Method for getting all users from data structures
        """
        if len(Users.users) < 1:
            return jsonify({"success":False, "error":{"message": "no user available"}}), 404
        return jsonify({"success":True, "data":Users.users}), 200

    def check_user_details(self, username, email):
        """
        Method for checking users details
        """
        for user in Users.users:
            if user['username'] == username or user['email'] == email:
                return jsonify({"success":False, "error":{"message": "username or email already exists"}}), 403
        return False

    def check_credentials(self, username, password):
        """
        Method for checking users username or password
        """
        for user in Users.users:
            if user['username'] == username:
                if check_password_hash(user['password'], password):
                    return True
        return jsonify({"success":False, "error":{"message": "invalid username or password"}}), 403

    def get_user_id(self, username):
        """
        Method that return user_id
        """
        for user in Users.users:
            if user['username'] == username:
                return user['user_id']