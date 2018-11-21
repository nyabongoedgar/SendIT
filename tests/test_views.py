import unittest, json
from application import app
from db import DatabaseConnection


class TestViews(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # print('SetUp')
        self.client = app.test_client()
        
        self.conn_object = DatabaseConnection()
        # parcel order
        # self.another_parcel_order = {'parcel_description':'this parcel contains a phone','parcel_weight':50,'parcel_source':'Ntinda','parcel_destination':'Mbarara','receiver_name':'Ritah','receiver_telephone':'077890340','current_location':'Ntinda','status':'pending'}
        #posting order to database
        self.present_location = {'present_location':'Bukumiro'}
        self.client.post('/api/v2/parcels',data=json.dumps({'parcel_description':'this parcel contains a phone','parcel_weight':50,'parcel_source':'Ntinda','parcel_destination':'Mbarara','receiver_name':'Ritah','receiver_telephone':'077890340','current_location':'Ntinda','status':'pending'}), content_type="application/json")
        self.admin_user = {'username':'timo','password':'123','email':'admin@gmail.com'}
        self.user ={"username":"Gafabusa","password":"123","email":"gafabusa@gmail.com"}
        self.user2 ={"username":"Gafabusa2","password":"123","email":"gafabusa@gmail.com"}
        
        self.new_destination = {'destination':'Kamwokya'}
        self.new_status = {'status':'delivered'}
        # testing with user below
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.user2),content_type='application/json')
        login_response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gafabusa2",password='123')),content_type='application/json')
        login_data = json.loads(login_response.data.decode('utf-8'))
        self.token = login_data.get('token')
        
        
    @classmethod
    def tearDownClass(self):
        self.conn_object.drop_tables('parcel_orders', 'users')   

    def test_user_registration_user(self):
       
        user_one = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        response = json.loads(user_one.data.decode()) 
        self.assertEqual(response['message'],'Username already exists')
        self.assertEqual(user_one.status_code,400)      


    def test_login(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.user),content_type='application/json')
        #test for right details
        response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gafabusa2",password='123')),content_type='application/json')
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(response_data.get('token'))
           
        #test for wrong password
        response_2 = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gafabusa",password='j4g874t2')),content_type='application/json')
        
        response_2_data = json.loads(response_2.data.decode('utf-8'))
        self.assertEqual(response_2_data['message'],'password does not match !')
        # wrong details
        wrong_data = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="Gshbdj",password="j4g874t2")),content_type='application/json')
        response3 = json.loads(wrong_data.data.decode())
        self.assertEqual(response3['message'],'Verification of credentials failed !')
        self.assertEqual(wrong_data.status_code,401)

    def test_create_parcel_delivery_order(self):
            
            #test for right details
            response = self.client.post('/api/v2/parcels',data=json.dumps({'parcel_description':'this parcel contains a bag','parcel_weight':30,'parcel_source':'Ntinda','parcel_destination':'Lubaga','receiver_name':'Godfrey','receiver_telephone':'077890340','current_location':'Ntinda','status':'pending'}), content_type="application/json", headers={'Authorization': 'Bearer ' + self.token})
            self.assertEqual(response.status_code,201)
            response_data = json.loads(response.data.decode())
            self.assertEqual(response_data['message'], 'order placed successfully')
        
    def test_user_getting_orders(self):
        response = self.client.get('/api/v2/parcels',headers={'Authorization': 'Bearer ' + self.token})
        self.assertEqual(response.status_code,200)

    def test_get_all_user_orders(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.admin_user),content_type='application/json')
        self.client.put('/api/v2/promote/timo')
        admin_login_response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="timo",password='123')),content_type='application/json')
        admin_login_data = json.loads(admin_login_response.data.decode('utf-8')) 
        token = admin_login_data.get('token')
        #test for right details        
        response = self.client.get('/api/v2/admin/parcels',headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response.status_code,200)
    #this is a user function
    def test_change_destination(self):
        #test for right details
        response = self.client.put('/api/v2/parcels/1/destination', data=json.dumps(self.new_destination), content_type="application/json", headers={'Authorization': 'Bearer ' + self.token})
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'destination of parcel delivery order changed')

    #admin
    def test_change_status(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.admin_user),content_type='application/json')
        self.client.put('/api/v2/promote/timo')
        admin_login_response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="timo",password='123')),content_type='application/json')
        admin_login_data = json.loads(admin_login_response.data.decode('utf-8')) 
        token = admin_login_data.get('token')

        response = self.client.put('/api/v2/parcels/1/status', data=json.dumps(self.new_status), content_type="application/json",headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'status of parcel delivery order changed')    

    def test_change_present_location(self):
        self.client.post('/api/v2/auth/signup',data=json.dumps(self.admin_user),content_type='application/json')
        self.client.put('/api/v2/promote/timo')
        admin_login_response = self.client.post('/api/v2/auth/login',data=json.dumps(dict( username="timo",password='123')),content_type='application/json')
        admin_login_data = json.loads(admin_login_response.data.decode('utf-8')) 
        token = admin_login_data.get('token')

        response = self.client.put('/api/v2/parcels/1/presentLocation', data=json.dumps(self.present_location), content_type="application/json",headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response.status_code,200)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'],'present location of parcel delivery order changed')

    

        

            

if __name__ == '__main__':
    unittest.main()
    