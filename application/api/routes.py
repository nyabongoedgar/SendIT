from flask import Blueprint,request,jsonify 
import json , datetime
from application.api.models import Parcel
from application.api.models import User
from application.api.utils import Helpers

mod = Blueprint('parcels',__name__,url_prefix='/api/v1')
parcel_object = Parcel()
user_object = User()

#index route 
@mod.route('/')
def index():
    return 'Welcome to the SendIT App'

#Account creation route
@mod.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    validate_data = Helpers.validate_strings([username,password,email])
    if validate_data is not None:
        return jsonify({'message':'username,email and password required. '+ validate_data}),400
    generated_id = Helpers.gen_id(user_object.users,"user_id")
    return user_object.signup(generated_id,username,password,email)

#Sign in route
@mod.route('/login',methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    validate_data = Helpers.validate_strings([username,password])
    if validate_data is not None:
        return jsonify({'message':validate_data}),400
    return user_object.login(username,password)

@mod.route('/logout')
def logout():
    return user_object.logout()

#Create a parcel delivery order
@mod.route("/parcels", methods=['POST'])
def create_parcel_delivery_order():
   
    if len(user_object.logged_in) is 0:
        return jsonify({'message':'Login is required !'}),401

    user_id = user_object.logged_in[0]

    data = request.get_json()
    pid = Helpers.gen_id(parcel_object.parcels,'parcel_id')
    name = data.get('parcel_name')
    source = data.get('parcel_source')
    destination = data.get('parcel_destination')
    date_created = str(datetime.datetime.utcnow())
    weight = int(data.get('parcel_weight'))
    receiver_name =data.get('receiver_name')
    receiver_telephone =data.get('receiver_telephone')
    delivered = False
    status = 'pending'
    price = Helpers.gen_price(weight)
    validate_int = Helpers.validate_integer([weight,price])
    if validate_int is not None:
        return jsonify({'message':validate_int}),400
    validate_string = Helpers.validate_strings([name,source,destination,date_created])
    if validate_string is not None:
        return jsonify({'message':validate_string}),400   
    order = {'parcel_id':pid, 'parcel_name':name, 'source':source,'destination':destination,'weight':weight, 'receiver_name':receiver_name, 'receiver_telephone':receiver_telephone,'price':price,'date_created':date_created,'status':status, 'delivered':delivered,'user_id':user_id}  
    return parcel_object.create_parcel_order_delivery(order)

#Fetch all parcels records '''
@mod.route('/parcels', methods= ['GET'])
def get_all_parcels():
    return parcel_object.get_all_parcels()
           

#Fetch a single parcel record
@mod.route("/parcels/<int:parcelId>", methods= ['GET'])
def get_one_sale(parcelId):
    return parcel_object.get_one_parcel(parcelId)

#route for cancelling a parcel order
@mod.route("/parcels/<int:parcelId>/cancel", methods=['PUT'])
def cancel_order(parcelId):
    check_order = Helpers.search(parcel_object.parcels,parcelId,'parcel_id')
    if check_order is None:
        return jsonify({'message':'parcel with parcel id of ' + str(parcelId) + ' doesnot exist'}),400
    data = request.get_json()
    status = data.get('status')
   
    if (status != "cancelled"):
        return jsonify({'message':'status can only be cancelled'}),400
            
    cancelled_order = Helpers.modify_status(parcel_object.parcels,'parcel_id',status,parcelId)
    if cancelled_order is not None:
        return parcel_object.cancel_specific_parcel(parcelId)

#route for getting all orders made by a specific user
@mod.route("/users/<int:userId>/parcels", methods=['GET'])
def get_user_orders(userId):
    all_orders = []
    for b in parcel_object.parcels:
        if b['user_id'] == int(userId):
            all_orders.append(b)
    if len(all_orders) is 0:
        return jsonify({'message':'No orders for this user'}),400

    return parcel_object.get_user_orders(all_orders)

           
