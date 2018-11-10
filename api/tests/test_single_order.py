"""
Module returns getting single orders results
"""
from unittest import TestCase
from api.tests.create_order import CreateOrder
from flask import json
from api.models.model import Model

class TestSingleOrder(TestCase):
    """
    Class that return the test results for getting all orders
    """
    def test_single_order(self):
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

        req = CreateOrder().client().get('/api/v1/parcels/1')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['destination'], 'bukoto')
        self.assertEqual(req.status_code, 200)
