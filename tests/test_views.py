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
        # self.conn_object.drop_tables([parcel_orders, users])   


    def test_user_registration_user(self):
       
        user_one = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        response = json.loads(user_one.data.decode()) 
        self.assertEqual(response['message'],'User registered successfully')
        self.assertEqual(user_one.status_code,201)      


    def test_login(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        #test for right details
        response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gafabusa",password='123')),content_type='application/json')
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data.get('message'),'Successfully logged in.')
        self.assertTrue(response_data.get('token'))
           
        #test for wrong password
        response_2 = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gafabusa",password='j4g874t2')),content_type='application/json')
        
        response_2_data = json.loads(response_2.data.decode('utf-8'))
        self.assertEqual(response_2_data['message'],'password does not match !')
        #wrong details
        # wrong_data = self.client('/api/v1/auth/login',data=json.dumps(dict( username="Gshbdj",password="j4g874t2")),content_type='application/json')
        # response3 = json.loads(wrong_data.data.decode())
        # self.assertEqual(response3['message'],'Verification of credentials failed !')
        # self.assertEqual(wrong_data.status_code,401)

if __name__ == '__main__':
    unittest.main()
    