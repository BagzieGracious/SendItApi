# SendItApi
[![Build Status](https://travis-ci.com/BagzieGracious/SendItApi.svg?branch=develop)](https://travis-ci.com/BagzieGracious/SendItApi)    [![Coverage Status](https://coveralls.io/repos/github/BagzieGracious/SendItApi/badge.svg?branch=develop)](https://coveralls.io/github/BagzieGracious/SendItApi?branch=develop)    [![Maintainability](https://api.codeclimate.com/v1/badges/8013b3d2fbcb647d9ca9/maintainability)](https://codeclimate.com/github/BagzieGracious/SendItApi/maintainability)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/e80558299d754090a8619621cfec8035)](https://www.codacy.com/app/BagzieGracious/SendItApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BagzieGracious/SendItApi&amp;utm_campaign=Badge_Grade)


# SendItApi
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

**Application Features**
* Users can create an account and log in.
* Users can create a parcel delivery order.
* Users can change the destination of a parcel delivery order.
* Users can cancel a parcel delivery order.
* Users can see the details of a delivery order.
* Admin can change the status and present location of a parcel delivery order


# A user can perform the following :
 Use the following endpoints to perform the specified tasks 
    
    EndPoint                                     | Functionality
    ------------------------                     | ----------------------
    Get /parcels/                                | Fetch all parcel delivery orders
    Get /parcels/<int:parcel_id>                 | Fetch a specific parcel delivery order
    POST /users/<int:user_id>/parcels            | Fetch all parcel delivery orders by a specific user
    PUT /parcels/<int:parcel_id>/cancel/         | Cancel the specific parcel delivery order
    POST /parcels/                               | Cancel the specific parcel delivery order
    
**Getting started with the app**

**Technologies used to build the application**

* [Python 3.6.5](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)

# Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone https://github.com/BagzieGracious/SendItApi.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```
Test your setup using a client app like postman
