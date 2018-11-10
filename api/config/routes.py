"""
Module for rendering routes
"""

from api.controllers.controller import Controller

class Routes:
    """
    Create a Routes class
    """

    @staticmethod
    def fetch_routes(app):
        """
        static method for fetching all routes
        """

        #default route
        @app.route('/')
        def index():
            return "<h1>Welcome to Send-It</h1> <p>The easy way to track your delivery.</p>"

        #parcels endpoints
        app.add_url_rule(
            '/api/v1/parcels/',
            view_func=Controller.as_view('createParcel'),
            methods=['POST'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/parcels/',
            view_func=Controller.as_view('getParcels'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/parcels/<int:parcel_id>',
            view_func=Controller.as_view('getSingleParcel'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/users/<int:user_id>/parcels',
            view_func=Controller.as_view('getParcelByUser'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/parcels/<int:parcel_id>/cancel',
            view_func=Controller.as_view('cancelParcel'),
            methods=['PUT'],
            strict_slashes=False
        )
