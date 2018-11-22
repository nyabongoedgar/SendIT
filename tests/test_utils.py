import unittest
from application.api.utils import Helpers

class Test_data_mod(unittest.TestCase):

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