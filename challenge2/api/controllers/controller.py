"""
Module controlling views
"""
from api.models.model import Model
from flask import jsonify, request
from flask.views import MethodView
from api.config.data_validation import DataValidation

class Controller(MethodView):
    
    def __init__(self): 
        self.parcel = Model() 
    
    def get(self, parcel_id=None, user_id=None):
        if parcel_id is None and user_id is None:
            return self.parcel.get_order()
        elif user_id is None:
            return self.parcel.get_order(parcel_id)
        return self.parcel.get_order_user(user_id)

    def put(self, parcel_id):
        return self.parcel.cancel_order(parcel_id)

    def post(self):
        post_data = request.get_json()
        value = DataValidation(post_data).validate()
        
        if isinstance(value, bool):
            data = {
                'order_id': len(self.parcel.lsts) + 1,
                'user_id': post_data['user_id'],
                'pickup': post_data['pickup'],
                'destination': post_data['destination'],
                'description': post_data['description'],
                'weight': post_data['weight'],
                'product': post_data['product'],
                'status': 'in-transit'
            }
            return self.parcel.create_order(data)
        return value