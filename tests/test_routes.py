import unittest, json, datetime
from application import app 


class Test_mod_products(unittest.TestCase):

    @classmethod
    def setUpClass(self):   
        self.parcel_order = {
        "parcel_name":"bag", 
        "parcel_source":"Ntinda",
        "parcel_destination":"Kamwokya",
        "parcel_weight":20,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557"
        }
        self.parcel_order2 = {
        "parcel_name":"phone",
        "parcel_source":"Bukoto",
        "parcel_destination":"KaMakindyemwokya",
        "parcel_weight":20,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557"
        }
    
        self.client = app.test_client()
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order), content_type="application/json")
        self.client.post('/api/v1/signup', data=json.dumps({'username':'timo','password':'1234','email':'timo@gmail.com'}), content_type="application/json")

    @classmethod
    def tearDownClass(self):
        print('TearDown')                  

    def test_init_page(self):
        rv = self.client.get('/api/v1/')
        self.assertEqual(rv.status_code, 200)
    def test_signup(self):
        rv = self.client.post('api/v1/signup', data=json.dumps({'username':'eddie','password':'1234','email':'eddie@gmail.com'}), content_type="application/json")
        self.assertEqual(rv.status_code,201) 
    def test_login(self):
        rv = self.client.post('api/v1/login',data=json.dumps({'username':'timo','password':'1234'}),content_type="application/json")
        self.assertEqual(rv.status_code,200)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(resp_data['message'],'Logged in')

    ### tests for products first
    def test_get_all_orders(self):
        rv = self.client.get('/api/v1/parcels')
        self.assertEqual(rv.status_code, 200)
        resp_data = json.loads(rv.data.decode())
        for i in resp_data:
             self.assertIn('parcel_id',i)
             self.assertIn('user_id',i)  
       
    def test_create_parcel_delivery_order(self):
        rv = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order2), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(resp_data['message'],'parcel order delivery placed')
        self.assertEqual(resp_data['status'],'success') 

    def test_get_one_order(self):
        rv = self.client.get('/api/v1/parcels/1')
        self.assertEqual(rv.status_code, 200)
        resp_data = json.loads(rv.data.decode())
        self.assertEqual(len(resp_data),12)
        self.assertEqual(resp_data['parcel_id'],1)
        self.assertEqual(resp_data['user_id'],1)    

    def test_cancel_order(self):
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order), content_type="application/json")
        rv = self.client.put('/api/v1/parcels/1/cancel', data = json.dumps({'status':'cancelled'}), content_type="application/json" )
        self.assertEqual(rv.status_code,201)
       
         

if __name__ == "__main__":
    unittest.main()

# python -m unittest discover -v tests
