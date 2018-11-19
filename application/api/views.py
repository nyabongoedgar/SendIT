from flask import Blueprint, jsonify, request 
import jwt, psycopg2, datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
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
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = conn.get_user_id(data['user_id'])
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
    conn_object.register_user(data['username'],data['email'],data['password'],False)
    return jsonify({'message':'User registered successfully'}),201
    
    

@mod.route("/auth/login", methods=['POST'])
def login(current_user): 
    data = request.get_json() 
    if not data or not data['username'] or not data['password']:
        return jsonify({'message':'Verification of credentials failed !'}),401{'WWW-Authentication':'Basic realm = "Login required !"'})
    user = conn.user(username)
    if not user:
        return jsonify({'message':'Verification of credentials failed !'}),401
    if check_password_hash(user['password'],auth.password):
        token = jwt.encode({'user_id':user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('UTF-8')}),200

@mod.route('/parcels', methods=['POST'])
@token_required
def make_order(current_user):
    pass


@mod.route('/parcels', methods=['GET'])
@token_required
def get_all_orders():
    pass


@mod.route('/parcels/<int:parcelId>/destination', methods=['PUT '])
def change_destination(current_user,parcelId):
    pass
@mod.route('/parcels/<int:parcelId>/status', methods=['PUT '])
@token_required
def status(current_user,parcelId):
    pass

@mod.route('/parcels/<int:parcelId>/presentLocation',methods=['PUT'])
@token_required
def change_present_location(current_user,parcelId):
    pass