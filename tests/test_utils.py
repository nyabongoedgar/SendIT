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
        x = Helpers.gen_price(20)
        self.assertEqual(x,5000)
        self.assertNotEqual(x,8000)
    
    def test_validate_strings(self):
        y = Helpers.validate_strings(['Edison','Kenga',5])
        self.assertEqual(y,'Data provided not a string and should not be a space')

    def test_validate_integers(self):
        x = Helpers.validate_integer([4,5,6,7,-1])
        z = Helpers.validate_integer([4,5,6,7,8])
        y = Helpers.validate_integer([4,5,6,7,8,'Edgar'])
        self.assertEqual(x,'Data provided not an integer and should not be a positive number')
        self.assertEqual(z,None) 
        self.assertEqual(y,'Data provided not an integer and should not be a positive number')