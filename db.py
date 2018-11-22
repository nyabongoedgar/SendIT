import psycopg2
import psycopg2.extras
import os,uuid


class DatabaseConnection:

    def __init__(self):
        db_name = os.getenv('DB_NAME')

        try:
            self.connection = psycopg2.connect(db=db_name,user='postgres', host='localhost',password='',port='5432')

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
        for table in tables:
            sql = 'DROP TABLE IF EXISTS {} CASCADE'.format(table)
            self.cursor.execute(sql)
            

   


if __name__ == '__main__':
    conn = DatabaseConnection()
    conn.cursor.execute()
     
    
