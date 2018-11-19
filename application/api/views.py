from flask import Blueprint, jsonify, request 
import jwt, psycopg2, datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnection
from db import conn 
mod = Blueprint('Parcel',__name__, url_prefix='/api/v1/')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'] 
        if not token:
            return jsonify({'message':'Token is missing !'}),401
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = conn.get_user_id(data)
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
    try:
        hashed_password = generate_password_hash(data['password'])
        conn.create_users(data['username'],data['email'],hashed_password,False)
        responseObject = {'message': 'Successfully registered.' } 
        return make_response(jsonify(responseObject)), 201

    except Exception as e:
        responseObject = {
                        'status': 'fail',
                        'message': 'User already exists.',
                        'Exception': e.decode()
                                }
        return make_response(jsonify(responseObject)), 401

@mod.route("/auth/login", methods=['POST'])
def login(): 
        data = request.get_json() 
        if not data or not data['username'] or not data['password']:
            return jsonify({'message':'password and username required'}),404

        if conn.login(data['username'],data['password']):
            token = jwt.encode({'user_id':user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8')}),200
        else:
            return jsonify({'message':'Could not verify, Login required !'}),401

@mod.route('/parcels', methods=['POST'])
def make_order():
    pass

@mod.route('/parcels', methods=['GET'])
def get_orders():
    pass

@mod.route('/parcels/<int:parcelId>', methods=['GET'])
def get_specific_order(parcelId):
    pass

@mod.route('/parcels/<int:parcelId>/destination', methods=['PUT '])
def change_destination(parcelId):
    pass
@mod.route('/parcels/<int:parcelId>/status', methods=['PUT '])
def status(parcelId):
    pass
@mod.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
def change_present_location(parcelId):
    pass