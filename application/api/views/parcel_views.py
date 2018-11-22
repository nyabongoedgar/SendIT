""" This module defines uthe parcel routes """

from flask import Blueprint, jsonify, request 
import re
from application import app
from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnection
from application.api.models.user import User
from application.api.models.parcels import Parcel
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

 
 
parcel = Blueprint('Parcel',__name__, url_prefix='/api/v2/')

user_object = User()
parcel_object = Parcel()
conn_object = DatabaseConnection()
 
@parcel.route('/')
def index():
    """ This is the index route, returns jsonified welcome message """
    return jsonify({'message':'Welcome to the SendIT application'}),200   

@parcel.route('/parcels', methods=['POST'])
@jwt_required
def make_order():
    """ This function enables a user to make a parcel delivery order """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    parcel_object.create_parcel_order(data['parcel_description'],data['parcel_weight'],data['parcel_source'],data['parcel_destination'],data['receiver_name'],data['receiver_telephone'],data['current_location'],data['status'], current_user)
    return jsonify({'message':'order placed successfully'}),201


@parcel.route('/parcels', methods=['GET'])
@jwt_required
def get_user_orders():
    """ This function enables a user to fetch his parcel delivery orders """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    output = []
    placed_orders  = parcel_object.get_one_user_orders(user['user_id'])
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200


@parcel.route('/parcels/<int:parcelId>/destination', methods=['PUT'])
@jwt_required
def change_destination(parcelId):
    """ This function enables a user to change the destination of a parcel delivery order """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    new_destination = data['destination']
    result_set = parcel_object.change_parcel_destination(new_destination,parcelId)
    if result_set == None:
        return jsonify({'message':'Failed to update parcel delivery order destination'}),400
    return jsonify({'message':'destination of parcel delivery order changed'}),200

@parcel.route('/parcels/<int:parcelId>/status', methods=['PUT'])
@jwt_required
def status(parcelId):
    """ This function enables an admin user to change the status a parcel delivery order """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    new_status = data['status']
    result_set = parcel_object.change_parcel_status(new_status,parcelId)
    if result_set == None:
        return jsonify({'message':'Failed to update status of delivery order'}),400

    return jsonify({'message':'status of parcel delivery order changed'}),200
    
@parcel.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
@jwt_required
def change_present_location(parcelId):
    """ This function enables a user to change the present location of a parcel delivery order """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    present_location = data['present_location']
    result_set = parcel_object.change_parcel_current_location(present_location,parcelId)
    if result_set == None:
        return jsonify({'message':'Failed to update present location of delivery order'}),400

    return jsonify({'message':'present location of parcel delivery order changed'}),200


@parcel.route('/admin/parcels', methods=['GET'])
@jwt_required
def get_all_user_orders():
    """ This function enables an admin user to get all parcel delivery orders in the system """
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    user  = user_object.get_user_by_id(current_user)
    output = []
    placed_orders  = parcel_object.get_all_orders()
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200
    
    