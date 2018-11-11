from flask import Blueprint,request,jsonify 
import json , datetime
from application.api.models import Parcel
from application.api.models import User
from application.api.utils import Helpers

mod = Blueprint('parcels',__name__,url_prefix='/api/v1')
parcelObject = Parcel()
userObject = User()

''' index route '''
@mod.route('/')
def index():
    return 'Welcome to the SendIT App'

''' Account creation route '''
@mod.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    a = Helpers.validate_strings([username,password,email])
    if a is not None:
        return jsonify({'message':a}),400
    b = Helpers.gen_id(userObject.users,"user_id")
    return userObject.signup(b,username,password,email)

''' Sign in route '''
@mod.route('/login',methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    b = Helpers.validate_strings([username,password])
    if b is not None:
        return jsonify({'message':b}),400
    return userObject.login(username,password)

''' Create a parcel delivery order '''
@mod.route("/parcels", methods=['POST'])
def create_parcel_delivery_order():
    if len(userObject.users) is 0:
        return jsonify({'message':'Login is required !'}),401

    for i in userObject.users:
        user_id = i["user_id"]

    data = request.get_json()
    pid = Helpers.gen_id(parcelObject.parcels,'parcel_id')
    name = data.get('parcel_name')
    source = data.get('parcel_source')
    destination = data.get('parcel_destination')
    date_created = str(datetime.datetime.utcnow())
    weight = int(data.get('parcel_weight'))
    receiver_name =data.get('receiver_name')
    delivered = False
    status = 'pending'
    

    x = Helpers.gen_price(weight)
    if isinstance(x,int):
        price = x
    else:
        return jsonify({'message':x}),400 
       
    validate_int = Helpers.validate_integer([weight,price])
    if validate_int is not None:
        return jsonify({'message':validate_int}),400

    validate_string = Helpers.validate_strings([name,source,destination,date_created])
    if validate_string is not None:
        return jsonify({'message':validate_string}),400
    
    return parcelObject.create_parcel_order_delivery(pid,name,source,destination,weight, receiver_name,price,date_created,status,delivered,user_id)

''' Fetch all parcels records '''
@mod.route('/parcels', methods= ['GET'])
def get_all_parcels():
    return parcelObject.get_all_parcels()
           

''' Fetch a single parcel record '''
@mod.route("/parcels/<int:parcelId>", methods= ['GET'])
def get_one_sale(parcelId):
    return parcelObject.get_one_parcel(parcelId)

@mod.route("/parcels/<int:parcelId>/cancel", methods=['PUT'])
def cancel_order(parcelId):
    check_order = Helpers.search(parcelObject.parcels,parcelId,'parcel_id')
    if check_order is None:
        return jsonify({'message':'parcel with parcel id of ' + str(parcelId) + ' doesnot exist'}),400
    data = request.get_json()
    status = data.get('status')
    if status != "cancelled":
        return jsonify({'message':'status can only be cancelled'}),400
    a = Helpers.validate_strings([status])
    if a is not None:
        return jsonify({'message':a}),400
            
    cancelled_order = Helpers.modify_status(parcelObject.parcels,'parcel_id',status,parcelId)
    
    return parcelObject.cancel_specific_parcel(cancelled_order)


           
