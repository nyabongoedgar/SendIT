import psycopg2
import os


class DatabaseConnection:

    def __init__(self):
       

        try:
            self.connection = psycopg2.connect(
                dbname='d62ol3dfvvnubk', user='rkgsgupxsprnfx', host='ec2-174-129-236-147.compute-1.amazonaws.com', password='77c80267f50cfc06bf5f8d89b27bf08df304c9c11c6c70c6337193fa77605a12', port='5432'
            )

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print ('Database connected.')
            users_table_sql = "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, username VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, password TEXT NOT NULL);"
            parcels_orders_table_sql = "CREATE TABLE IF NOT EXISTS parcel_orders (parcel_id UUID NOT NULL, user_id INTEGER REFERENCES users(user_id), parcel_description TEXT NOT NULL, parcel_weight INTEGER NOT NULL, price_quote NUMBER, parcel_source VARCHAR (255) NOT NULL, parcel_destination VARCHAR (255) NOT NULL, receiver_name VARCHAR (100) NOT NULL, receiver_telephone VARCHAR(10) NOT NULL, date_created TIMESTAMP NOT NULL,current_location VARCHAR(200),status VARCHAR(30), PRIMARY_KEY(parcel_id,user_id));"

            # self.cursor.execute(SET timezone = 'Nairobi')
            self.cursor.execute(users_table_sql)
            self.cursor.execute(parcels_orders_table_sql)


        except:
            print('Cannot connect to the database.')

    def check_user(self, user_id):
        sql = " ' SELECT * FROM users WHERE user_id=%s',(user_id,)"
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        return user

    def create_users(self,username, email, password):
        create_user = " ' INSERT INTO users(username, email, password) VALUES(%s, %s, %s) ', (username, email, password) "
        self.cursor.execute(create_user)
    
    def login(self, username, password):
        sql = " 'SELECT * FROM users WHERE username=%s and password = %s',(username,password)"
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        return user

    def create_parcel_order(self,parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status):
        sql = " ' INSERT INTO parcel_orders(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) ',(parcel_id,parcel_description,parcel_weight,parcel_source,parcel_destination,receiver_name,receiver_telephone,date_created,current_location,status) "
        self.cursor.execute(sql)

    def change_parcel_destination(self, new_destination, parcel_id):
        sql = " 'UPDATE table parcel_orders SET parcel_destination = %s WHERE parcel_id = %s',(new_destination,parcel_id) "
        self.cursor.execute(sql) 


    def get_user_parcel_orders(self, user_id):
        sql = " ' SELECT * FROM parcel_orders WHERE user_id=%s',(user_id,) "
        self.cursor.execute(sql)
        return answers
    
    #admin methods

    def get_all_parcel_orders(self):
        sql = "SELECT * FROM parcel_orders"
        self.cursor.execute(sql)
        question = self.cursor.fetchall()
        return question

    def change_parcel_status(self, new_status, parcel_id):
        sql = " ' UPDATE table parcel_orders SET status = %s WHERE parcel_id = %s ',(new_status,parcel_id) "
        self.cursor.execute(sql)

    def change_parcel_current_location(self, new_location, parcel_id):
        sql = " ' UPDATE table parcel_orders SET current_location =%s WHERE parcel_id = %s',(new_location,parcel_id) "
        self.cursor.execute(sql)    
    

    def drop_tables(self):
        sql = "DROP TABLE users, parcel_orders"
        self.cursor.execute(sql)

   


if __name__ == '__main__':
    conn = DatabaseConnection()
