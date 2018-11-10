"""
Module for testing empty errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestEmptyErrors(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_empty_errors(self):
        """
        Method for testing empty errors
        """
        order = {
            'user_id':1,
            'pickup': '',
            'destination': 'bukoto',
            'description': 'This a smartphone',
            'weight': 1,
            'product': 'Iphone',
        }
        post = CreateOrder().create_order(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'no empty values are allowed')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
