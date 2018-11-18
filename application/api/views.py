from flask import Blueprint, jsonify, request 
import jwt, psycopg2, datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnection 
mod = Blueprint('Parcel',__name__, url_prefix='/api/v1/')

conn = DatabaseConnection ()

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
    pass

 
@mod.route('/auth/signup', methods = ['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    conn.create_users(data['username'],data['email'],data['password'],False)
    return jsonify({'message':'new user created'}),201 

@mod.route("/auth/login", methods=['POST'])
def login():
    auth = request.headers
    if not auth or not auth.username or not auth.password:
        return make_response('coul not verify',401,{'WWW-Authentication':'Basic realm = "Login required !"'})
    user = conn.user(auth.username)
    if not user:
        return make_response('coul not verify',401,{'WWW-Authentication':'Basic realm = "Login required !"'})
    if check_password_hash(user['password'],auth.password):
        token = jwt.encode({'user_id':user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('UTF-8')}),200

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