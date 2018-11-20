import unittest, json
from application import app
from db import DatabaseConnection


class TestViews(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('SetUp')
        self.client = app.test_client()
        self.conn_object = DatabaseConnection()
        self.user ={"username":"Gafabusa","password":"123","email":"gafabusa@gmail.com"}
        
        
    @classmethod
    def tearDownClass(self):
        print('TearDown')
        self.conn_object.drop_tables()   


    def test_user_registration_user(self):
       
        user_one = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        response = json.loads(user_one.data.decode()) 
        self.assertEqual(response['message'],'User registered successfully')
        self.assertEqual(user_one.status_code,201)
        same_user = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        response2 = json.loads(same_user.data.decode())
        self.assertEqual(response2['message'],'Username already exists')

      
          
            


    # def test_login(self):
    #     TestViews.register_user()
    #     #test for right details
    #     response = self.client.post('/auth/login',data=json.dumps(dict( username="testername",password='testerpassword')),content_type='application/json')
    #     self.assertEqual(response.status_code,200)
    #     response_data = json.loads(response.data.decode('utf-8'))
    #     self.assertEqual(response_data.get('message'),'Successfully logged in.')
    #     self.assertTrue(response_data.get('auth_token'))
           
    #     #test for wrong login details
    #     response_2 = self.client.post('/auth/login',data=json.dumps(dict( username="sbdbk03982y2",password='j4g874t2')),content_type='application/json')
        
    #     response_2_data = json.loads(response_2.data.decode('utf-8'))
    #     self.assertEqual(response_2_data.get('message'),'Wrong login credentials')

if __name__ == '__main__':
    unittest.main()
    