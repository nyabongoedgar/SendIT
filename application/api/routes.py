from flask import Blueprint,request,jsonify, abort 
import json , datetime
from application.api.models import Parcel
from application.api.models import User
from application.api.utils import Helpers
from functools import wraps

mod = Blueprint('parcels',__name__,url_prefix='/api/v1')

#the actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    #the new, post-decoration function
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == 'mysimpleapikey':
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


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
    parcel_weight = int(data.get('parcel_weight'))
    receiver_name =data.get('receiver_name')
    receiver_telephone =data.get('receiver_telephone')
    description = data.get('parcel_description')
    delivered = False
    status = 'pending'
    price = Helpers.gen_price(parcel_weight)
    validate_int = Helpers.validate_integer([parcel_weight,price])
    if validate_int is not None:
        return jsonify({'message':validate_int}),400
    validate_string = Helpers.validate_strings([name,source,destination,date_created])
    if validate_string is not None:
        return jsonify({'message':validate_string}),400   
    order = {'parcel_id':pid, 'parcel_name':name,'parcel_description':description, 'parcel_source':source,'parcel_destination':destination,'parcel_weight':parcel_weight, 'receiver_name':receiver_name, 'receiver_telephone':receiver_telephone,'price_quote':price,'date_created':date_created,'status':status, 'delivered':delivered,'user_id':user_id}
    check_for_similar_order = Helpers.check_if_exists(args=order,myList=parcel_object.parcels)
    if check_for_similar_order is not None:
        return jsonify({'message':check_for_similar_order}),400
      
    return parcel_object.create_parcel_order_delivery(order)

#Fetch all parcels records '''
@mod.route('/parcels', methods= ['GET'])
def get_all_parcels():
    if len(user_object.logged_in) is 0:
        return jsonify({'message':'Login is required !'}),401
    return parcel_object.get_all_parcels()
           

#Fetch a single parcel record
@mod.route("/parcels/<int:parcelId>", methods= ['GET'])
def get_one_sale(parcelId):
    if len(user_object.logged_in) is 0:
        return jsonify({'message':'Login is required !'}),401
    return parcel_object.get_one_parcel(parcelId)

#route for cancelling a parcel order
@mod.route("/parcels/<int:parcelId>/cancel", methods=['PUT'])
def cancel_order(parcelId):
    if len(user_object.logged_in) is 0:
        return jsonify({'message':'Login is required !'}),401
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
@require_appkey
def get_user_orders(userId):
    all_orders = []
    for b in parcel_object.parcels:
        if b['user_id'] == int(userId):
            all_orders.append(b)
    if len(all_orders) is 0:
        return jsonify({'message':'No orders for this user'}),200

    return parcel_object.get_user_orders(all_orders)

           
