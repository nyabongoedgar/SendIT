from flask import Blueprint, jsonify, request 
import psycopg2
import datetime
import jwt
from functools import wraps
from application import app
from werkzeug.security import generate_password_hash, check_password_hash
from application.api.db import DatabaseConnection
 
 
mod = Blueprint('Parcel',__name__, url_prefix='/api/v2/')

conn_object = DatabaseConnection()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'] 
        if not token:
            return jsonify({'message':'Token is missing !'}),401
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']

        except:
            return jsonify({'message':'Token is required'}),401
           
        return f(current_user, *args, **kwargs)
    return decorated
 
@mod.route('/')
def index():
    return jsonify({'message':'SendIT application'}),200
 
@mod.route('/auth/signup', methods = ['POST']) 
def register_user():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password') 
    user = conn_object.user(username)  
    if user is not None:
        return jsonify({'message':'Username already exists'}),401 
    hashed_pasword = generate_password_hash(password, method='sha256')
    conn_object.register_user(username,email,hashed_password)
    return jsonify({'message':'User registered successfully'}),201
    
    

@mod.route("/auth/login", methods=['POST'])
def login(): 
    data = request.get_json() 
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message':'Verification of credentials failed !'}),401
    user = conn_object.user(data.get('username'))
    if not user:
        return jsonify({'message':'Verification of credentials failed !'}),401
    if check_password_hash(user['password'],data['password']):
    # if user['password'] == data['password']:
        token = jwt.encode({'user_id':user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token':token.decode('UTF-8')}),200
    return jsonify({'message':'password does not match !'})

@mod.route('/parcels', methods=['POST'])
@token_required
def make_order(current_user):
    user  = conn_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    conn_object.create_parcel_order(data['parcel_description'],data['parcel_weight'],data['parcel_source'],data['parcel_destination'],data['receiver_name'],data['receiver_telephone'],data['current_location'],data['status'])
    return jsonify({'message':'order placed successfully'}),201


@mod.route('/parcels', methods=['GET'])
'''This function returns a users order '''
@token_required
def get_user_specific_orders(current_user):
    user  = conn_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    output = []
    placed_orders  = conn_object.get_user_specific_parcel_orders(user['user_id'])
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200


@mod.route('/parcels/<int:parcelId>/destination', methods=['PUT'])
def change_destination(current_user,parcelId):
    user  = conn_object.get_user_by_id(current_user)
    if user['admin'] ==  True:
        return  jsonify({'message':'This is a normal user route'}),401
    data = request.get_json()
    new_destination = data['destination']
    result_set = conn.object.change_parcel_destination(new_destination,parcelId)
    if result_set is not 1:
        return jsonify({'message':'Failed to update parcel delivery order destination'}),400
    return jsonify({'message':'destination of parcel delivery order changed'}),200

@mod.route('/parcels/<int:parcelId>/status', methods=['PUT'])
@token_required
def status(current_user,parcelId):
    user  = conn_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    new_status = data['status']
    result_set = conn_object.change_parcel_status(new_status,parcelId)
    if result_set is not 1:
        return jsonify({'message':'Failed to update status of delivery order'}),400

    return jsonify({'message':'status of parcel delivery order changed'}),200

@mod.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
@token_required
def change_present_location(current_user,parcelId):
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    data = request.get_json()
    present_location = data['present_location']
    result_set = conn_object.change_parcel_current_location(present_location,parcelId)
    if result_set is not 1:
        return jsonify({'message':'Failed to update present location of delivery order'}),400

    return jsonify({'message':'present location of parcel delivery order changed'}),200


@mod.route('/parcels/admin', methods=['GET'])
def get_all_user_orders(current_user):
    if user['admin'] ==  False:
        return  jsonify({'message':'This is an admin route, you are not authorized to access it'}),401
    user  = conn_object.get_user_by_id(current_user)
    if user['admin'] ==  False:
        return  jsonify({'message':'This is a normal user route'}),401
    output = []
    placed_orders  = conn_object.get_user_parcel_orders(user['user_id'])
    if placed_orders is None:
        return jsonify({'message':'No orders placed for this user'})
    for order in placed_orders:
        output.append(order)
    return jsonify({'placed orders':output}),200