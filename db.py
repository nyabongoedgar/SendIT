""" This module contains the database connection and some database utility functions  """

import psycopg2
import psycopg2.extras
import os,uuid


class DatabaseConnection:
    """ This class defines the database connection """

    def __init__(self):
        """ This method initializes the database connection """
        # db_name = os.getenv('DATABASE_NAME')

        try:
            self.connection = psycopg2.connect(dbname='defb17uf0pchi7',user='fvheujobpptfos', host='ec2-23-21-201-12.compute-1.amazonaws.com',password='5b404bb6671defebfed8c63f4df98f14594660f26675b1c225ddc97b51c5cee3',port='5432')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print ('Database connected.')
            users_table_sql = "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, username VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, password TEXT NOT NULL, admin Boolean NOT NULL);"

            parcels_orders_table_sql = "CREATE TABLE IF NOT EXISTS parcel_orders (parcel_id SERIAL NOT NULL, user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE, parcel_description TEXT NOT NULL, parcel_weight INTEGER NOT NULL, price_quote INTEGER, parcel_source VARCHAR (255) NOT NULL, parcel_destination VARCHAR (255) NOT NULL, receiver_name VARCHAR (100) NOT NULL, receiver_telephone VARCHAR(10) NOT NULL, date_created TIMESTAMP NOT NULL,current_location VARCHAR(200),status VARCHAR(30), PRIMARY KEY(parcel_id,user_id));"

            
            self.cursor.execute(users_table_sql)
            self.cursor.execute(parcels_orders_table_sql)


        except:
            print('Cannot connect to the database.')

  
    def drop_tables(self, *tables):
        """ This method drops tables that are passed as a list """
        for table in tables:
            sql = 'DROP TABLE IF EXISTS {} CASCADE'.format(table)
            self.cursor.execute(sql)
            

   


if __name__ == '__main__':
    conn = DatabaseConnection()
    
     
    
