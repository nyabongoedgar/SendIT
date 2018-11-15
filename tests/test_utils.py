import unittest
from application.api.utils import Helpers

class Test_data_mod(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('SetUp')
        self.search_list =[{"CountryId":"1","Country":"Uganda","President":"Yoweri Kaguta"}]
        self.right_key = "CountryId"
        self.wrong_key = "state" 
        self.keyValue = 1
      
    
    @classmethod
    def tearDownClass(self):
        print('TearDown')
    
    
     

    def test_gen_id(self):
        y = Helpers.gen_id(self.search_list,self.right_key)
        self.assertEqual(y,2)
        self.assertNotEqual(y,3)
    
    def test_gen_price(self):
        r = Helpers.gen_price(0)
        s = Helpers.gen_price(50)
        t = Helpers.gen_price(100)
        u = Helpers.gen_price(200)
        v = Helpers.gen_price(20)
        w = Helpers.gen_price(1000)
        x = Helpers.gen_price(1100)        
        self.assertEqual(r,'weight should not be zero')
        self.assertEqual(s, 10000)
        self.assertEqual(t, 15000)
        self.assertEqual(u, 20000)
        self.assertEqual(v,5000)
        self.assertEqual(w,20000)
        self.assertEqual(x,'Weight exceeded')
    
    def test_validate_strings(self):
        y = Helpers.validate_strings(['Edison','Kenga',5])
        self.assertEqual(y,'Data provided should be a string and should not be a space')

    def test_validate_integers(self):
        x = Helpers.validate_integer([4,5,6,7,-1])
        z = Helpers.validate_integer([4,5,6,7,8])
        y = Helpers.validate_integer([4,5,6,7,8,'Edgar'])
        self.assertEqual(x,'Data provided should be an integer and should not be a positive number')
        self.assertEqual(z,None) 
        self.assertEqual(y,'Data provided should be an integer and should not be a positive number')
    
    def test_check_if_exist(self):
        listx = [{
        "parcel_name":"phone",
        "parcel_source":"Bukoto",
        "parcel_destination":"Makindye",
        "parcel_weight":0,
        "receiver_name":"Kenneth",
        "receiver_telephone":"0779865557",
        "parcel_description":"This parcel contains a blue blackberry c23 smartphone"}]
        args = {"parcel_description":"This parcel contains a blue blackberry c23 smartphone","parcel_destination":"Makindye","parcel_weight":0,"parcel_name":"phone"}
        self.assertEqual(Helpers.check_if_exists(args,listx),'Parcel order delivery already placed, please make a unique order')   
