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

    def get_order(self):
        """
        method for get data from data structures
        """
        return jsonify({"status": "success", "data":Model.lsts}), 200

    def get_single_order(self, order_id, user_id):
        for order in Model.lsts:
            if str(order['order_id']) == order_id and order['user_id'] == user_id:
                return jsonify({"status": "success", "data": order}), 200
        return jsonify({"status": "failure", "error": {"message": "order not found"}}), 404

    def get_order_user(self, usr, user_id):
        """
        Methods for get data posted by a specific user
        """
        if str(usr) == user_id:
            for order in Model.lsts:
                if str(order['user_id']) == user_id:
                    Model.userLst.append(order)
                else:
                    Model.userLst.clear()

            if len(Model.userLst) > 0:
                return jsonify({"status": "success", "data":Model.userLst}), 200
        return jsonify({"status": "failure", "error":{"message": "order not found"}}), 404


    def cancel_order(self, order_id, user_id):
        """
        Method for cancelling parcel delivery order
        """
        for order in Model.lsts:
            if order['user_id'] == user_id:
                if str(order['order_id']) == order_id:
                    order['status'] = 'cancelled'
                    return jsonify({"status": "success", "data":order}), 200
        return jsonify({"status": "failure", "error": {"message": "order not found"}}), 404

    def create_order(self, order):
        """
        method for add an order in the data structure
        """
        Model.lsts.append(order)
        return jsonify({"status": "success", "data":order}), 201

    def check_for_exist(self, user_id, product, destination ):
        for order in Model.lsts:
            if order['user_id'] == user_id and order['product'] == product and order['destination'] == destination:
                return jsonify({"status": "failure", "error": {"message": "you have created that order previously"}}), 400
        return False
