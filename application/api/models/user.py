""" This module defines user methods for registration login and user queries """
from db import DatabaseConnection

class User:
    """ Users contains methods that operate on the user object """

    def __init__(self):
        self.db_object = DatabaseConnection()

    

    def login(self, username, password):
        """ The login method signs in a registered user """

        sql = "SELECT * FROM users WHERE username='{}' and password = '{}'".format(username,password)
        self.db_object.cursor.execute(sql)
        user = self.db_object.cursor.fetchone()
        return user

    def register_user(self,username, email, password):
        """ The register_user method creates a user an account for a user """

        admin = False
        create_user = "INSERT INTO users(username, email, password, admin) VALUES('{}', '{}', '{}', '{}')".format(username, email, password,admin)
        self.db_object.cursor.execute(create_user)

    def get_user_by_id(self, user_id):
        """ This method returns a user with the provided userId """

        sql = "SELECT * FROM users WHERE user_id='{}' ".format(user_id)
        self.db_object.cursor.execute(sql)
        user_result = self.db_object.cursor.fetchone()
        return user_result

    def user(self, username):
        """ This method returns a user with the provided user_name """

        sql = "SELECT * FROM users WHERE username='{}'".format(username)
        self.db_object.cursor.execute(sql)
        user = self.db_object.cursor.fetchone()
        return user

    def promoter(self,username):
        """ This method promotes a user to admin """
        
        sql = "UPDATE users SET admin='{}' WHERE username = '{}'".format(True,username)
        self.db_object.cursor.execute(sql)
        rowcount = self.db_object.cursor.rowcount
        return rowcount