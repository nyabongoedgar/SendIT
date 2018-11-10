from flask import Blueprint,request,jsonify 
import json , datetime
from application.api.models import Parcel
from application.api.utils import Helpers

mod = Blueprint('parcels',__name__,url_prefix='/api/v1')
parcelObject = Parcel()

''' index route '''
@mod.route('/')
def index():
    return 'Welcome to the SendIT App'

''' Create a parcel delivery order '''
@mod.route("/parcels", methods=['POST'])
def create_parcel_delivery_order():
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
        return jsonify({'message':x}) 
       
    validate_int = Helpers.validate_integer([weight,price])
    if validate_int is not None:
        return jsonify({'message':validate_int}),400

    validate_string = Helpers.validate_strings([name,source,destination,date_created])
    if validate_string is not None:
        return jsonify({'message':validate_string}),400
    
    return parcelObject.create_parcel_order_delivery(pid,name,source,destination,weight, receiver_name,price,date_created,status,delivered)

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
    return parcelObject.cancel_specific_parcel(parcelId)


           
