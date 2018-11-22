""" This module defines methods that interact with the parcel_orders table """
from db import DatabaseConnection
from application.api.utils import Helpers 
import datetime
class Parcel:
    def __init__(self):
        self.db_object = DatabaseConnection()

    def create_parcel_order(self,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,current_location,status, user_id):
        """ This method creates a parcel delivery order """

        date_created = datetime.datetime.utcnow()
        price_quote = Helpers.gen_price(parcel_weight)
        sql = "INSERT INTO parcel_orders(parcel_description,parcel_weight,price_quote,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status,user_id) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(parcel_description,parcel_weight,price_quote,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status,user_id)
        self.db_object.cursor.execute(sql)

    def change_parcel_destination(self, new_destination, parcel_id):
        """ This method changes the destination of the parcel to be delivered """

        sql = "UPDATE parcel_orders SET parcel_destination = '{}' WHERE parcel_id = '{}'".format(new_destination,parcel_id)
        self.db_object.cursor.execute(sql)
        rowcount = self.db_object.cursor.rowcount
        return rowcount


    def get_one_user_orders(self,user_id):
        """ This method returns the parcels created by a specific user the parcel to be delivered """

        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.db_object.cursor.execute(sql)
        placed_orders = self.db_object.cursor.fetchall()
        return placed_orders


    

    def get_all_orders(self):
        sql = "SELECT * FROM parcel_orders"
        self.db_object.cursor.execute(sql)
        all_orders = self.db_object.cursor.fetchall()
        return all_orders

   
    def change_parcel_status(self, new_status, parcel_id):
        sql = "UPDATE parcel_orders SET status = '{}' WHERE parcel_id = '{}' ".format(new_status,parcel_id)
        self.db_object.cursor.execute(sql)
        rowcount = self.db_object.cursor.rowcount
        return rowcount

    def change_parcel_current_location(self, new_location, parcel_id):
        sql = "UPDATE parcel_orders SET current_location ='{}' WHERE parcel_id = '{}'".format(new_location,parcel_id) 
        self.db_object.cursor.execute(sql)    
        rowcount = self.db_object.cursor.rowcount
        return rowcount
    