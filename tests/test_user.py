import unittest, json
from application import app
from db import DatabaseConnection


class TestViews(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = app.test_client() 
        self.conn_object = DatabaseConnection()
        self.present_location = {'present_location':'Bukumiro'}

        self.admin_user = {'username':'timo','password':'123','email':'admin@gmail.com'}

        self.user ={"username":"Micky","password":"123","email":"micky@gmail.com"}

        self.user2 ={"username":"Gafabusa2","password":"123","email":"gafabusa@gmail.com"}
        self.client.post('/api/v2/signup',data=json.dumps(self.user2), content_type="application/json")
        
        
        
        
        
    @classmethod
    def tearDownClass(self):
        self.conn_object.drop_tables('users')   

    def test_initial_page(self):
        response = self.client.get('/api/v2/')
        self.assertEqual(response.status_code,200)
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'),'Welcome to the SendIT application')
        
    def test_user_registration_user(self):
        
        user_one = self.client.post('/api/v2/auth/signup',data=json.dumps({'username':'jinkens','password':'123','email':'j@gmail.com'}),content_type='application/json')
        response = json.loads(user_one.data.decode()) 
        self.assertEqual(response['message'],'User registered successfully')
        self.assertEqual(user_one.status_code,201)

    def test_user_registration_already_existing(self):
        user_one = self.client.post('/api/v2/auth/signup',data=json.dumps({"username":"Gafabusa2","password":"123","email":"gafabusa@gmail.com"}),content_type='application/json')
        response = json.loads(user_one.data.decode()) 
        self.assertEqual(response['message'],'Username already exists')
        self.assertEqual(user_one.status_code,400)
              


    def test_login(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        #test for right details
        response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Micky",password='123')),content_type='application/json')
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(response_data.get('token'))
           
        #test for wrong password
        response_2 = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Dickson",password='j4g874t2')),content_type='application/json')
        
        response_2_data = json.loads(response_2.data.decode('utf-8'))
        self.assertEqual(response_2_data['message'],'Verification of credentials failed !')
        # wrong details
        wrong_data = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Micky",password="j4g874t2")),content_type='application/json')
        response3 = json.loads(wrong_data.data.decode())
        self.assertEqual(response3['message'],'password does not match !')
        self.assertEqual(wrong_data.status_code,401)

    def test_login_without_data(self):
        response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="",password='')),content_type='application/json')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'No data has been sent')
        self.assertEqual(response.status_code,400)

    

    def test_promote_user(self):
        response = self.client.put('/api/v2/promote/Gafabusa2')
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'Gafabusa2 promoted to admin')

    def test_promote_wrong_user(self):
        response = self.client.put('/api/v2/promote/78')
        self.assertEqual(response.status_code,400)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'user promotion failed')

    



        

            

if __name__ == '__main__':
    unittest.main()
    