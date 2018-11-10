from flask import jsonify, request, abort
import datetime
from application.api.utils import Helpers 

class Users:
    def __init__(self,name,password):
        self.users = []
        self.name = name
        self.password = password
        admin=False
    
    def create_account(self):
        x = Helpers.validate_strings([self.name,self.password])
        if x is not None:
            return jsonify({'message':x}),400
        new_user  = {"username":self.name, "password":self.password,"admin":admin}
        self.users.append(new_user)

    def login(self):
        pass



class Parcel:
    def __init__(self):
        self.parcels =[]


    def create_parcel_order_delivery(self,pid,name,source,destination,weight, receiver_name,price,date_created,status,delivered):
        
        order = {'parcel_id':pid, 'parcel_name':name, 'source':source,'destination':destination,'weight':weight, 'receiver_name':receiver_name, 'price':price,'date_created':date_created,'status':status, 'delivered':delivered}

        self.parcels.append(order)

        return jsonify(self.parcels),201

         
    def get_all_parcels(self):
        if len(self.parcels) is 0:
            responseObject={"message":"There are no items to display at the moment"}
            return jsonify(responseObject),204
        else:
            return jsonify(self.parcels),200

    def get_one_parcel(self,parcelId):
        item = Helpers.search(self.parcels,parcelId,'parcel_id')
        if item is None:
            return jsonify({"messagae":"Pacel ID not valid and cannot be a negative"})
        else:
            return jsonify(item),200 

    def cancel_specific_parcel(self,parcelId):
        data = request.get_json()
        status = data.get('status')
        x = Helpers.modify_status(self.parcels,'parcel_id',status,parcelId)
        return jsonify(x),201