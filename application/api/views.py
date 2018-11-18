from flask import Blueprint, jsonify, request 
import jwt, psycopg2
from functools import wraps
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
            current_user = conn.check_user(data)
        except:
            return jsonify({'message':'Token is required'}),401
           
    return f(current_user, *args, **kwargs)
 
@mod.route('/')
def index():
    pass

 
@mod.route('/auth/signup', methods = ['POST'])
def sigup():
    pass

@mod.route("/auth/login", methods=['POST'])
def login():
    pass

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