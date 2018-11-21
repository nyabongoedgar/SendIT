from application.api.models.db import DatabaseConnection
class Parcel:
    def __init__(self):
        self.db_object = DatabaseConnection()

    def create_parcel_order(self,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,current_location,status):
        data_created = datetime.datetime.utcnow()
        sql = "INSERT INTO parcel_orders(parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status)

        sql = "INSERT INTO parcel_orders(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status)
        self.db_object.cursor.execute(sql)

    def change_parcel_destination(self, new_destination, parcel_id):
        sql = "UPDATE table parcel_orders SET parcel_destination = '{}' WHERE parcel_id = '{}'".format(new_destination,parcel_id)
        self.db_object.cursor.execute(sql)
        rowcount = self.db_object.cursor.rowcount
        return rowcount


    def get_user_specific_parcel_orders(self,user_id):
        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.db_object.cursor.execute(sql)
        placed_orders = self.db_object.cursor.fetchall()
        return placed_orders

    def get_user_parcel_orders(self, user_id):
        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.db_object.cursor.execute(sql)
        placed_orders = self.db_object.cursor.fetchall()
        return placed_orders
    
    #admin methods

    def get_all_parcel_orders(self):
        sql = "SELECT * FROM parcel_orders"
        self.db_object.cursor.execute(sql)
        all_orders = self.db_object.cursor.fetchall()
        return all_orders

   
    def change_parcel_status(self, new_status, parcel_id):
        sql = "UPDATE table parcel_orders SET status = '{}' WHERE parcel_id = '{}' ".format(new_status,parcel_id)
        self.db_object.cursor.execute(sql)
        rowcount = self.db_object.cursor.rowcount
        return rowcount

    def change_parcel_current_location(self, new_location, parcel_id):
        sql = "UPDATE table parcel_orders SET current_location ='{}' WHERE parcel_id = '{}'".format(new_location,parcel_id) 
        self.db_object.cursor.execute(sql)    
        rowcount = self.db_object.cursor.rowcount
        return rowcount
    