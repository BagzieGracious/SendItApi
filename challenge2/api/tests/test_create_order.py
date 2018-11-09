"""
Module for testing create order
"""
from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestCreateProduct(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_create_order(self):
        """
        Method returns create order results
        """
        order = {
            'user_id':1,
            'pickup': 'mulago',
            'destination': 'bukoto',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'Iphone',
        }
        post = CreateOrder().create_order(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['product'], 'Iphone')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)
