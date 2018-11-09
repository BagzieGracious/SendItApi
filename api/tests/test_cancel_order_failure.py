"""
Module returns getting single orders results
"""
from unittest import TestCase
from api.tests.create_order import CreateOrder
from flask import json
from api.models.model import Model

class TestNoCancelOrder(TestCase):
    """
    Class that return the test results for getting all orders
    """
    def test_cancel_order_failure(self):
        """
        Method for testing endpoint of getting all orders
        """
        Model.lsts.clear()
        Model.userLst.clear()
        
        CreateOrder().create_order({
            'user_id':1,
            'pickup': 'mulago',
            'destination': 'bukoto',
            'description': 'This a smartTv',
            'weight': 50,
            'product': 'Samsung flat screen Tv',
        })
        CreateOrder().create_order({
            'user_id':2,
            'pickup': 'mulago',
            'destination': 'kamwokya',
            'description': 'This a radio',
            'weight': 10,
            'product': 'Iphone',
        })
        CreateOrder().create_order({
            'user_id':3,
            'pickup': 'mulago',
            'destination': 'ntinda',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'Iphone',
        })

        req = CreateOrder().client().put('/api/v1/parcels/10/cancel/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'order not found')
        self.assertEqual(req.status_code, 404)
