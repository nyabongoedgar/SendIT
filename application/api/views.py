from flask import Blueprint, jsonify, request 
import psycopg2
import datetime
from application import app
from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnection
from application.api.models.user import User
from application.api.models.parcels import Parcel
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = '\x01\n=:\x87\xe1\x02\xca\x81\x8b\x0c\xe4Y=\x87\xb7\xa8\x89.<\x95\x90\xbb\x06'
 
mod = Blueprint('Parcel',__name__, url_prefix='/api/v2/')

user_object = User()
parcel_object = Parcel()
conn_object = DatabaseConnection()
 
@mod.route('/')
def index():
    return jsonify({'message':'SendIT application'}),200
 
@mod.route('/auth/signup', methods = ['POST']) 
def register_user():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password') 
    user = user_object.user(username)  
    if user is not None:
        return jsonify({'message':'Username already exists'}),400 
    hashed_password = generate_password_hash(password, method='sha256')
    user_object.register_user(username,email,hashed_password)
    return jsonify({'message':'User registered successfully'}),201
    
   

@mod.route("/auth/login", methods=['POST'])
def login(): 
    data = request.get_json() 
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message':'No data has been sent'}),401
    user = user_object.user(data.get('username'))
    if not user:
        return jsonify({'message':'Verification of credentials failed !'}),401
    if check_password_hash(user['password'],data['password']):
        token = create_access_token(identity=user['user_id'])
        return jsonify({'token':token}), 200        
    return jsonify({'message':'password does not match !'})

@mod.route('/parcels', methods=['POST'])
@jwt_required
def make_order():
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    parcel_object.create_parcel_order(data['parcel_description'],data['parcel_weight'],data['parcel_source'],data['parcel_destination'],data['receiver_name'],data['receiver_telephone'],data['current_location'],data['status'], current_user)
    return jsonify({'message':'order placed successfully'}),201


@mod.route('/parcels', methods=['GET'])
@jwt_required
def get_user_specific_orders():
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    output = []
    placed_orders  = parcel_object.get_user_specific_parcel_orders(user['user_id'])
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200


@mod.route('/parcels/<int:parcelId>/destination', methods=['PUT'])
@jwt_required
def change_destination(parcelId):
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    new_destination = data['destination']
    result_set = parcel_object.change_parcel_destination(new_destination,parcelId)
    if result_set == -1:
        return jsonify({'message':'Failed to update parcel delivery order destination'}),400
    return jsonify({'message':'destination of parcel delivery order changed'}),200

@mod.route('/parcels/<int:parcelId>/status', methods=['PUT'])
@jwt_required
def status(parcelId):
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    new_status = data['status']
    result_set = parcel_object.change_parcel_status(new_status,parcelId)
    if result_set == -1:
        return jsonify({'message':'Failed to update status of delivery order'}),400

    return jsonify({'message':'status of parcel delivery order changed'}),200
    
@mod.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
@jwt_required
def change_present_location(parcelId):
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    present_location = data['present_location']
    result_set = parcel_object.change_parcel_current_location(present_location,parcelId)
    if result_set == -1:
        return jsonify({'message':'Failed to update present location of delivery order'}),400

    return jsonify({'message':'present location of parcel delivery order changed'}),200


@mod.route('/admin/parcels', methods=['GET'])
@jwt_required
def get_all_user_orders():
    current_user = get_jwt_identity()
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    user  = user_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is a normal user route'}),401
    output = []
    placed_orders  = parcel_object.get_user_parcel_orders(user['user_id'])
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200

@mod.route('/promote/<username>',methods=['PUT'])
def promote_user(username):
    result_set =user_object.promoter(username)
    if result_set:
        return jsonify({'message':username + ' promoted to admin'}),200
    return jsonify({'message':'user promotion failed'})
    