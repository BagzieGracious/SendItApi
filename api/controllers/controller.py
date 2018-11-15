"""
Module controlling views
"""
from flask import request, jsonify
import jwt
import uuid
import datetime
from api.models.user import Users
from api.models.model import Model
from api.config.data_validation import DataValidation

class Controller:
    """
    Controller class that inherits MethodView object
    """

    def __init__(self):
        """
        Class contructor for initialising model object
        """
        self.req = request
        self.security_key = 'json_web_token'
        self.model = Model()

    def login(self):
        """
        Method for login that deals with params from views
        """
        data = self.req.get_json()
        if isinstance(Users().check_credentials(data['username'], data['password']), bool):
            token = jwt.encode({
                'user': data['username'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, self.security_key)
            return jsonify({"success": True, "message": "logged in successfully", "token":token.decode('UTF-8')}), 200
        return Users().check_credentials(data['username'], data['password'])

    def signup(self):
        """
        Method for signup that deals with params from views
        """
        value = DataValidation(self.req, 'user').validate()
        if isinstance(value, bool):
            data = self.req.get_json()
            if not Users().check_user_details(data['username'], data['email']):
                return Users(data['username'], data['email']).add_user(data['password'])
            return Users().check_user_details(data['username'], data['email'])
        return value

    def get_users(self):
        """
        Method that returns all users to views
        """
        return Users().get_all_users()

    def create_order(self):
        """
        Method for creating a parcel delivery order
        """
        value = DataValidation(self.req, 'order').validate()
        if isinstance(value, bool):
            token = request.headers['token_value']
            usr = jwt.decode(token, 'json_web_token')
            user_id = Users().get_user_id(usr['user'])
            data = self.req.get_json()

            if not self.model.check_for_exist(user_id, data['product'], data['destination']):
                order = {
                    'user_id': Users().get_user_id(usr['user']),
                    'order_id': uuid.uuid4(),
                    'pickup': data['pickup'],
                    'destination':data['destination'],
                    'description': data['description'],
                    'weight': data['weight'],
                    'product':data['product'],
                    'status':'pending'
                }
                return self.model.create_order(order)
            return self.model.check_for_exist(user_id, data['product'], data['destination'])
        return value

    def get_order(self, parcel_id=None):
        """
        Method for getting orders from datastructures
        """
        if parcel_id is None:
            return self.model.get_order()

        token = request.headers['token_value']
        usr = jwt.decode(token, 'json_web_token')
        user_id = Users().get_user_id(usr['user'])
        return self.model.get_single_order(parcel_id, user_id)

    def get_order_user(self, user_id=None):
        """
        Method for getting orders by a specifc user
        """
        token = request.headers['token_value']
        usr = jwt.decode(token, 'json_web_token')
        usrid = Users().get_user_id(usr['user'])
        return self.model.get_order_user(usrid, user_id)

    def cancel_order(self, parcel_id=None):
        """
        Method for canceling an order
        """
        token = request.headers['token_value']
        usr = jwt.decode(token, 'json_web_token')
        usrid = Users().get_user_id(usr['user'])
        return self.model.cancel_order(parcel_id, usrid)

    