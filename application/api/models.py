from flask import jsonify, request, abort
import datetime
from application.api.utils import Helpers 

class User:

    def __init__(self):
        self.users = []
        self.logged_in = []
    
    def signup(self,user_id,username,password,email):
        for i in self.users:
            if i['username'] == username:
                return jsonify({'message':'Username already exists'}),400
        new_user  = {"user_id":user_id,"username":username, "password":password,'email':email,"admin":False}

        self.users.append(new_user)
        return jsonify({'message':'Your user account has been created'}),201

    def login(self,username,password):
        for i in self.users:
            if (i['username'] == username and i['password'] == password):
                user_id = i['user_id']
                self.logged_in.append(user_id)
                return jsonify({'message':'Logged in'}),200            
        return jsonify({'message':'Invalid credentials'}),400
    
    

    def logout(self):
        if len(self.logged_in) is not None:
            self.logged_in.remove(self.logged_in[0])
            return jsonify({'message':'You have logged out successfully!'}),200


class Parcel:
    def __init__(self):
        self.parcels =[]

    # creates prcel with data sent from route
    def create_parcel_order_delivery(self,order):
        self.parcels.append(order)
        return jsonify({'message':'parcel order delivery placed','status':'success'}),201

    #checks if there are orders in self.parcels and returns all of them
    def get_all_parcels(self):
        if len(self.parcels) is 0:
            responseObject={"message":"There are no items to display at the moment"}
            return jsonify(responseObject),200
        else:
            return jsonify(self.parcels),200
    
    #model method for picking one specific parcel
    def get_one_parcel(self,parcelId):
        item = Helpers.search(self.parcels,parcelId,'parcel_id')
        if item is None:
            return jsonify({"messagae":"Pacel ID not valid and cannot be a negative"}),400
        else:
            return jsonify(item),200 

    #model method for cancelling a parcel delivery order.
    def cancel_specific_parcel(self,parcelId):  
        return jsonify({'message':'Parcel delivery order with id '+str(parcelId)+' has been cancelled'}),201

    #Admin method for picking user specific orders
    def get_user_orders(self,user_orders):
        return jsonify({'Orders':user_orders}),200