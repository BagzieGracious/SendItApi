"""
Module that acts a model, for handling data manipulation
"""
from flask import jsonify

class Model:
    """
    model class that add data to data structures
    """
    lsts = []
    userLst = []

    def get_order(self, order_id=None):
        """
        method for get data from data structures
        """
        if order_id is None:
            return jsonify({"success":True, "data":Model.lsts}), 200
        for order in Model.lsts:
            if order.get('order_id') == order_id:
                return jsonify({"success":True, "data":order}), 200
        return jsonify({"success":False, "error":{"message": "order not found"}}), 404

    def get_order_user(self, user_id):
        """
        Methods for get data posted by a specific user
        """
        for order in Model.lsts:
            if order.get('user_id') == user_id:
                Model.userLst.append(order)
            else:
                Model.userLst.clear()

        if len(Model.userLst) > 0:
            return jsonify({"success":True, "data":Model.userLst}), 200
        return jsonify({"success":False, "error":{"message": "order not found"}}), 404


    def cancel_order(self, order_id):
        """
        Method for cancelling parcel delivery order
        """
        for order in Model.lsts:
            if order.get('order_id') == order_id:
                order['status'] = 'cancelled'
                return jsonify({"success":True, "data":order}), 200
        return jsonify({"success":False, "error":{"message": "order not found"}}), 404

    def create_order(self, order):
        """
        method for add an order in the data structure
        """
        Model.lsts.append(order)
        return jsonify({"success":True, "data":order}), 201
