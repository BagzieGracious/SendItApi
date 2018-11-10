"""
Module for testing users order
"""
from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.create_order import CreateOrder

class TestUserOrder(TestCase):
    """
    Class that return the test results for users orders
    """
    def test_user_order(self):
        """
        Method for testing endpoint of users orders
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
            'user_id':1,
            'pickup': 'mulago',
            'destination': 'kamwokya',
            'description': 'This a radio',
            'weight': 10,
            'product': 'Iphone',
        })
        CreateOrder().create_order({
            'user_id':2,
            'pickup': 'mulago',
            'destination': 'ntinda',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'HTC',
        })

        req = CreateOrder().client().get('/api/v1/users/2/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data'][0]['product'], 'HTC')
        self.assertEqual(req.status_code, 200)
