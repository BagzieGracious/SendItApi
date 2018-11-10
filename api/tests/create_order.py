"""
Module for creating an order
"""
from flask import json
from run import APP

class CreateOrder:
    """
    Class for creating an order
    """

    def __init__(self):
        """
        class constructor for initiating flask object
        """
        self.app = APP
        self.client = self.app.test_client

    def create_order(self, data):
        """
        Method for creating order
        """
        post = self.client().post(
            '/api/v1/parcels/',
            data=json.dumps(dict(
                user_id=data['user_id'],
                pickup=data['pickup'],
                destination=data['destination'],
                description=data['description'],
                weight=data['weight'],
                product=data['product']
            )),
            content_type='application/json'
        )
        return post
