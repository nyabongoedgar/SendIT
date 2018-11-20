from flask import Blueprint, jsonify, request 
import psycopg2
import datetime
import jwt
from functools import wraps
from application import app
# from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnection
 
 
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
    # hashed_pasword = generate_password_hash(password, method='sha256')
    conn_object.register_user(username,email,password)
    return jsonify({'message':'User registered successfully'}),201
    
    

@mod.route("/auth/login", methods=['POST'])
def login(): 
    data = request.get_json() 
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message':'Verification of credentials failed !'}),401
    user = conn_object.user(data.get('username'))
    if not user:
        return jsonify({'message':'Verification of credentials failed !'}),401
    # if check_password_hash(user['password'],data['password']):
    if user['password'] == data['password']:
        token = jwt.encode({'user_id':user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token':token.decode('UTF-8')}),200
    return jsonify({'message':'password does not match !'})

@mod.route('/parcels', methods=['POST'])
@token_required
def make_order(current_user):
    data = request.get_json()
    return conn_object.create_parcel_order(data['parcel_description'],data['parcel_weight'],data['parcel_source'],data,data['receiver_name'],data['receiver_telephone'],data['current_location'],data['status'])


@mod.route('/parcels', methods=['GET'])
@token_required
def get_all_orders():
    return conn_object.get_all_parcel_orders()


@mod.route('/parcels/<int:parcelId>/destination', methods=['PUT '])
def change_destination(current_user,parcelId):
    data = request.get_json()
    new_destination = data['destination']
    return conn.object.change_parcel_destination(new_destination,parcelId)

@mod.route('/parcels/<int:parcelId>/status', methods=['PUT '])
@token_required
def status(current_user,parcelId):
    data = request.get_json()
    new_status = data['status']
    return conn_object.change_parcel_status(new_status,parcelId)

@mod.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
@token_required
def change_present_location(current_user,parcelId):
    data = request.get_json()
    present_location = data['present_location']
    return change_parcel_current_location(present_location,parcelId)