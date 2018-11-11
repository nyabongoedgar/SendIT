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
        "receiver_name":"Kenneth"
        }
        self.parcel_order2 = {
        "parcel_name":"phone",
        "parcel_source":"Bukoto",
        "parcel_destination":"KaMakindyemwokya",
        "parcel_weight":20,
        "receiver_name":"Kenneth"
        }
        self.status = {"status":"cancelled"}
        self.client = app.test_client()
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order), content_type="application/json")

    @classmethod
    def tearDownClass(self):
        print('TearDown')                  

    def test_init_page(self):
        rv = self.client.get('/api/v1/')
        self.assertEqual(rv.status_code, 200)

    ### tests for products first
    def test_get_all_orders(self):
        rv = self.client.get('/api/v1/parcels')
        self.assertEqual(rv.status_code, 200)
        # resp_data = json.loads(rv.data.decode())
        # for i in resp_data:
        #     self.assertIn('productId',i)
        #     self.assertNotIn('saleId',i)  
       
    def test_create_parcel_delivery_order(self):
        rv = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_order2), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        # resp_data = json.loads(rv.data.decode())
        # self.assertEqual(resp_data['message'],'product created')
        # self.assertEqual(resp_data['status'],'success') 

    def test_get_one_order(self):
        rv = self.client.get('/api/v1/parcels/2')
        # self.assertEqual(rv.status_code, 200)
        # resp_data = json.loads(rv.data.decode())
        # self.assertEqual(len(resp_data),4)
        # self.assertEqual(resp_data['productId'],1)   
    # def test_cancel_order(self):
    #     rv = self.client.put('api/v1/1/cancel',data= json.dumps(self.status), content_type="application/json" )
    #     resp_data = json.loads(rv.data.decode())
    #     self.assertEqual(resp_data['status'],'cancelled')
         

if __name__ == "__main__":
    unittest.main()

# python -m unittest discover -v tests
