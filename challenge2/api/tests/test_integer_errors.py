"""
Module for testing create order
"""
from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestIntegerErrors(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_integer_errors(self):
        """
        Method returns create order results
        """
        order = {
            'user_id':'1',
            'pickup': 'mulago',
            'destination': 'bukoto',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'Iphone',
        }
        post = CreateOrder().create_order(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'user_id and weight should be integers')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
