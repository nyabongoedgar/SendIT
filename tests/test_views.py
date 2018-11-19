import unittest, json
from application import app


class TestViews(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('SetUp')
        self.client = app.test_client()
        
        
    @classmethod
    def tearDownClass(self):
        print('TearDown')
        # self.models_object.test_delete('testername')   
        
    @staticmethod 
    def register_user():
        client = app.test_client()
        resp_register = client.post('/auth/signup',data=json.dumps({'username':'testname','password':'password','admin':False}),content_type='application/json')
        return True
          
            


    def test_login(self):
        TestViews.register_user()
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
    