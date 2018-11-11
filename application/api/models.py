from flask import jsonify, request, abort
import datetime
from application.api.utils import Helpers 

class User:

    def __init__(self):
        self.users = []
        
    
    def signup(self,user_id,username,password,email):
        new_user  = {"user_id":user_id,"username":username, "password":password,'email':email,"admin":False}
        self.users.append(new_user)
        return jsonify({'user created':self.users}),201

    def login(self,username,password):
        for i in self.users:
            if (i['username'] == username and i['password'] == password):
                return jsonify({'message':'Logged in'})
        return jsonify({'message':'Invalid credentials'}),400



class Parcel:
    def __init__(self):
        self.parcels =[]


    def create_parcel_order_delivery(self,pid,name,source,destination,weight, receiver_name,price,date_created,status,delivered,user_id):
        
        order = {'parcel_id':pid, 'parcel_name':name, 'source':source,'destination':destination,'weight':weight, 'receiver_name':receiver_name, 'price':price,'date_created':date_created,'status':status, 'delivered':delivered,'user_id':user_id}

        self.parcels.append(order)

        return jsonify(self.parcels),201

    '''' checks if there are orders in self.parcels and returns all of them '''   
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

    def cancel_specific_parcel(self,order):
        
        return jsonify(order),201

    def get_user_orders(self,user_orders):
        return jsonify({'Orders':user_orders}),200