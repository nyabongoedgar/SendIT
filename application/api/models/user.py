from application.api.models.db import DatabaseConnection
class User:
    def __init__(self):
        self.db_object = DatabaseConnection()

    

    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username='{}' and password = '{}'".format(username,password)
        self.db_object.cursor.execute(sql)
        user = self.db_object.cursor.fetchone()
        return user

    def register_user(self,username, email, password):
        admin = False
        create_user = "INSERT INTO users(username, email, password, admin) VALUES('{}', '{}', '{}', '{}')".format(username, email, password,admin)
        self.db_object.cursor.execute(create_user)

    def get_user_by_id(self, user_id):
        sql = "SELECT * FROM users WHERE user_id='{}' ".format(user_id)
        self.db_object.cursor.execute(sql)
        user_result = self.db_object.cursor.fetchone()
        return user_result

    def user(self, username):
        sql = "SELECT * FROM users WHERE username='{}'".format(username)
        self.db_object.cursor.execute(sql)
        user = self.db_object.cursor.fetchone()
        return user