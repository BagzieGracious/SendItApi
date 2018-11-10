"""
Module for testing string errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestStringErrors(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_string_errors(self):
        """
        Method for testing string errors
        """
        order = {
            'user_id':1,
            'pickup': 256,
            'destination': 'bukoto',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'Iphone',
        }
        post = CreateOrder().create_order(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'pickup, destination, description and product should be string values')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
