import unittest, json
from flask import request
import requests
from application import app 
from application import Blueprint 
from application.users.routes import db
import flask
from application.users import models
import chardet

class Test_auth(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('SetUp')
        self.client = app.test_client()
        app.testing = True
        test = flask.Blueprint('application.users.routes.db',__name__) 
        self.models_object = models.models.DatabaseConnection()
        
    @classmethod
    def tearDownClass(self):
        print('TearDown')
        self.models_object.test_delete('testername')   
        
    @staticmethod
    def register_user():
        client = app.test_client()
        resp_register = client.post(
                '/auth/signup',
                data=json.dumps(dict(
                    user_id="2",
                    email_address='testername@gmail.com',
                    password='testerpassword',
                    username="testername",
                )),
                content_type='application/json'
            )
        return True
          
            


    def test_login(self):
        Test_auth.register_user()
        #test for right details
        response = self.client.post('/auth/login',data=json.dumps(dict( username="testername",password='testerpassword')),content_type='application/json')
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data.get('message'),'Successfully logged in.')
        self.assertTrue(response_data.get('auth_token'))
           
        #test for wrong login details
        response_2 = self.client.post('/auth/login',data=json.dumps(dict( username="sbdbk03982y2",password='j4g874t2')),content_type='application/json')
        
        response_2_data = json.loads(response_2.data.decode('utf-8'))
        self.assertEqual(response_2_data.get('message'),'Wrong login credentials')

if __name__ == '__main__':
    unittest.main()
    