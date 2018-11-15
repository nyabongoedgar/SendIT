import unittest, json, datetime
from application import app 


class Test_routes(unittest.TestCase):

    @classmethod
    def setUpClass(self):   
        self.parcel_order = {
        "parcel_name":"bag", 
        "parcel_source":"Ntinda",
        "parcel_destination":"Kamwokya",
        "parcel_weight":20,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557",
        "description":"This parcel contains a black bag with 50 pieces of soap "
        }
        self.parcel_order2 = {
        "parcel_name":"phone",
        "parcel_source":"Bukoto",
        "parcel_destination":"KaMakindyemwokya",
        "parcel_weight":20,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557",
        "description":"This parcel contains an Iphone X with a 7 inch screen"
        }
        self.parcel_order3 = {
        "parcel_name":"phone",
        "parcel_source":"Bukoto",
        "parcel_destination":"Makindye",
        "parcel_weight":0,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557",
        "parcel_description":"This parcel contains a blue blackberry c23 smartphone"
        }
        self.parcel_order4 = {
        "parcel_name":658,
        "parcel_source":"Bukoto",
        "parcel_destination":"KaMakindyemwokya",
        "parcel_weight":30,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557",
        "parcel_description":"This parcel contains a number"
        }
    
        self.client = app.test_client()
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order), content_type="application/json")
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order2), content_type="application/json")
        self.client.post('/api/v1/signup', data=json.dumps({'username':'timo','password':'1234','email':'timo@gmail.com'}), content_type="application/json")
        

    @classmethod
    def tearDownClass(self):
        print('TearDown')                  

    def test_init_page(self):
        rv = self.client.get('/api/v1/')
        self.assertEqual(rv.status_code, 200)
    def test_signup(self):
        rv = self.client.post('/api/v1/signup', data=json.dumps({'username':'eddie','password':'1234','email':'eddie@gmail.com'}), content_type="application/json")
        self.assertEqual(rv.status_code,201)
        resp_right = json.loads(rv.data.decode())
        self.assertEqual(resp_right['message'],'Your user account has been created') 
        wrong_data = self.client.post('api/v1/signup', data=json.dumps({'username':678,'password':8492,'email':470}), content_type="application/json")
        response = json.loads(wrong_data.data.decode())
        self.assertEqual(wrong_data.status_code,400)
        self.assertEqual(response['message'],'username,email and password required. Data provided should be a string and should not be a space')
        self.assertEqual(rv.status_code,201) 

    def test_login(self):
        rv = self.client.post('/api/v1/login',data=json.dumps({'username':'timo','password':'1234'}),content_type="application/json")
        wrong_data = self.client.post('api/v1/login',data = json.dumps({'username':123,'password':'pass'}),content_type="application/json")
        response = json.loads(wrong_data.data.decode())
        self.assertEqual(wrong_data.status_code,400)
        self.assertEqual(response['message'],'Data provided should be a string and should not be a space')
        self.assertEqual(rv.status_code,200)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(resp_data['message'],'Logged in')

    def test_logout(self):
        self.client.post('/api/v1/login', data=json.dumps({'username':'timo','password':'1234'}), content_type="application/json")
        rv =self.client.get('api/v1/logout')
        self.assertEqual(rv.status_code,200)
        resp = json.loads(rv.data.decode())
        self.assertEqual(resp['message'],'You have logged out successfully!')
    ### tests for products first
    def test_get_all_orders(self):
        self.client.get('api/v1/logout')
        without_login = self.client.get('/api/v1/parcels')
        self.assertEqual(without_login.status_code,401)
        self.client.post('/api/v1/login', data=json.dumps({'username':'timo','password':'1234'}), content_type="application/json")
        rv = self.client.get('/api/v1/parcels')
        self.assertEqual(rv.status_code, 200)
        resp_data = json.loads(rv.data.decode())
        for i in resp_data:
             self.assertIn('parcel_id',i)
             self.assertIn('user_id',i)  
       
    def test_create_parcel_delivery_order(self):
        self.client.get('api/v1/logout')
        without_login = self.client.get('/api/v1/parcels')
        self.assertEqual(without_login.status_code,401)
        self.client.post('/api/v1/login', data=json.dumps({'username':'timo','password':'1234'}), content_type="application/json")
        rv = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order2), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(resp_data['message'],'parcel order delivery placed')
        self.assertEqual(resp_data['status'],'success')
        #invalid data type
        wrong_data = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order3), content_type="application/json")
        self.assertEqual(wrong_data.status_code,400)
        response = json.loads(wrong_data.data.decode())
        self.assertEqual(response['message'],'Data provided should be an integer and should not be a positive number')
        #invalid string
        wrong_data2 = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order4), content_type="application/json")
        response2 = json.loads(wrong_data2.data.decode())
        self.assertEqual(response2['message'],'Data provided should be a string and should not be a space')  

    def test_get_one_order(self):
        self.client.get('api/v1/logout')
        without_login = self.client.get('/api/v1/parcels')
        self.assertEqual(without_login.status_code,401)
        self.client.post('/api/v1/login', data=json.dumps({'username':'timo','password':'1234'}), content_type="application/json")
        rv = self.client.get('/api/v1/parcels/1')
        self.assertEqual(rv.status_code, 200)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(len(resp_data),13)
        self.assertEqual(resp_data['parcel_id'],1)
        self.assertEqual(resp_data['user_id'],1)    

    def test_cancel_order(self):
        self.client.get('api/v1/logout')
        without_login = self.client.get('/api/v1/parcels')
        self.assertEqual(without_login.status_code,401)
        self.client.post('/api/v1/login', data=json.dumps({'username':'timo','password':'1234'}), content_type="application/json")
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order), content_type="application/json")
        rv = self.client.put('/api/v1/parcels/1/cancel', data = json.dumps({'status':'cancelled'}), content_type="application/json" )
        self.assertEqual(rv.status_code,201)
        wrong_data1 = self.client.put('/api/v1/parcels/300/cancel', data = json.dumps({'status':'cancelled'}), content_type="application/json" )
        self.assertEqual(wrong_data1.status_code,400)
        response1 = json.loads(wrong_data1.data.decode())
        self.assertEqual(response1['message'],'parcel with parcel id of 300 doesnot exist')     

        wrong_data2 = self.client.put('/api/v1/parcels/1/cancel', data = json.dumps({'status':'something'}), content_type="application/json" ) 
        response2 = json.loads(wrong_data2.data.decode())
        self.assertEqual(wrong_data2.status_code,400) 
        self.assertEqual(response2['message'],'status can only be cancelled')
        

    def test_get_orders_by_userId(self):
        rv = self.client.get('/api/v1/users/1/parcels?key=mysimpleapikey')
        self.assertEqual(rv.status_code,200)
        response = json.loads(rv.data.decode())
        for i in response:
            self.assertIn('Orders',i)  
        self.assertNotEqual(len(response),0)
        wrong_data = self.client.get('/api/v1/users/30/parcels?key=mysimpleapikey')
        response2 = json.loads(wrong_data.data.decode())
        self.assertEqual(response2['message'],'No orders for this user') 
        self.assertEqual(wrong_data.status_code,200)
        wrong_api_key = self.client.get('api/v1/users/1/parcels?key=peoplepower')
        self.assertEqual(wrong_api_key.status_code,401)

if __name__ == "__main__":
    unittest.main()

# python -m unittest discover -v tests
