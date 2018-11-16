"""
Module for rendering routes
"""
from flask import request, jsonify
from api.controllers.controller import Controller
import jwt
from functools import wraps


class Routes:
    """
    Create a Routes class
    """

    def __init__(self):
        self.controller = Controller()

    def fetch_routes(self, app):
        """
        static method for fetching all routes
        """

        def required(func):
            @wraps(func)
            def decorated(*args, **kwargs):
                if 'token_value' in request.headers:
                    token = request.headers['token_value']
                else:
                    return jsonify({"status": "failure", "error": {"message": "Login, in-order to access this view"}}), 400
                try:
                    jwt.decode(token, 'json_web_token')
                except:
                    return jsonify({"status": "failure", "error": {"message": "Invalid, token"}}), 400
                return func(*args, **kwargs)
            return decorated

        @app.route('/api/v1/auth/login', methods=['POST'], strict_slashes=False)
        def login():
                return self.controller.login()

        @app.route('/api/v1/auth/signup', methods=['POST'], strict_slashes=False)
        def signup():
            return self.controller.signup()
            
        @app.route('/api/v1/parcels', methods=['POST', 'GET'], strict_slashes=False)
        @required
        def parcels():
            if request.method == 'POST':
                return self.controller.create_order()
            return self.controller.get_order()

        @app.route('/api/v1/parcels/<parcel_id>', methods=['GET'], strict_slashes=False)
        @required
        def get_single_parcel(parcel_id):
            return self.controller.get_order(parcel_id)

        @app.route('/api/v1/users/<user_id>/parcels', methods=['GET'], strict_slashes=False)
        @required
        def get_parcel_user(user_id):
            return self.controller.get_order_user(user_id)

        @app.route('/api/v1/parcels/<parcel_id>/cancel', methods=['PUT'], strict_slashes=False)
        @required
        def cancel_parcel(parcel_id):
            return self.controller.cancel_order(parcel_id)

        @app.route('/api/v1/users', methods=['GET'], strict_slashes=False)
        def get_users():
            return self.controller.get_users()