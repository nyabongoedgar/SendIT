import psycopg2
import psycopg2.extras
import os, datetime, uuid


class DatabaseConnection:

    def __init__(self):
        db = os.getenv('DATABASE_NAME')
        

        try:
            self.connection = psycopg2.connect(dbname=db, user='postgres', host='localhost', password='password', port='5432')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print ('Database connected.')
            users_table_sql = "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, username VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, password TEXT NOT NULL, admin Boolean NOT NULL);"
            parcels_orders_table_sql = "CREATE TABLE IF NOT EXISTS parcel_orders (parcel_id SERIAL, user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE, parcel_description TEXT NOT NULL, parcel_weight INTEGER NOT NULL, price_quote INTEGER, parcel_source VARCHAR (255) NOT NULL, parcel_destination VARCHAR (255) NOT NULL, receiver_name VARCHAR (100) NOT NULL, receiver_telephone VARCHAR(10) NOT NULL, date_created TIMESTAMP NOT NULL,current_location VARCHAR(200),status VARCHAR(30), PRIMARY KEY(parcel_id,user_id));"

           
            self.cursor.execute(users_table_sql)
            self.cursor.execute(parcels_orders_table_sql)


        except:
            print('Cannot connect to the database.')

    def get_user_by_id(self, user_id):
        sql = "SELECT * FROM users WHERE user_id='{}' ".format(user_id)
        self.cursor.execute(sql)
        user_result = self.cursor.fetchone()
        return user_result

    def user(self, username):
        sql = "SELECT * FROM users WHERE username='{}'".format(username)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        return user

    def register_user(self,username, email, password):
        admin = False
        create_user = "INSERT INTO users(username, email, password, admin) VALUES('{}', '{}', '{}', '{}')".format(username, email, password,admin)
        self.cursor.execute(create_user)
    
    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username='{}' and password = '{}'".format(username,password)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        return user


    def create_parcel_order(self,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,current_location,status):
        data_created = datetime.datetime.utcnow()
        sql = "INSERT INTO parcel_orders(parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status)

        sql = "INSERT INTO parcel_orders(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status)
        self.cursor.execute(sql)

    def change_parcel_destination(self, new_destination, parcel_id):
        sql = "UPDATE table parcel_orders SET parcel_destination = '{}' WHERE parcel_id = '{}'".format(new_destination,parcel_id)
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        return rowcount


    def get_user_specific_parcel_orders(self,user_id):
        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.cursor.execute(sql)
        placed_orders = self.cursor.fetchall()
        return placed_orders

    def get_user_parcel_orders(self, user_id):
        sql = "SELECT * FROM parcel_orders WHERE user_id='{}'".format(user_id)
        self.cursor.execute(sql)
        placed_orders = self.cursor.fetchall()
        return placed_orders
    
    #admin methods

    def get_all_parcel_orders(self):
        sql = "SELECT * FROM parcel_orders"
        self.cursor.execute(sql)
        all_orders = self.cursor.fetchall()
        return all_orders

   
    def change_parcel_status(self, new_status, parcel_id):
        sql = "UPDATE table parcel_orders SET status = '{}' WHERE parcel_id = '{}' ".format(new_status,parcel_id)
        self.cursor.execute(sql)
        rowcount = self.cursor.rowcount
        return rowcount

    def change_parcel_current_location(self, new_location, parcel_id):
        sql = "UPDATE table parcel_orders SET current_location ='{}' WHERE parcel_id = '{}'".format(new_location,parcel_id) 
        self.cursor.execute(sql)    
        rowcount = self.cursor.rowcount
        return rowcount
    
  
    def drop_tables(self, *tables):
        for table in tables:
            sql = 'DROP TABLE IF EXISTS {}'.format(table)
            self.cursor.execute(sql)
            

   


if __name__ == '__main__':
    conn = DatabaseConnection()
     
    
