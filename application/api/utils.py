class Helpers:          


    @staticmethod
    def gen_price(weight):
        price = ""
        if weight <= 0 :
            price = 'weight should not be zero'
        if (weight > 0 and weight <= 20):
            price = 5000
        if (weight > 20 and weight <= 50):
            price = 10000
        if (weight > 50 and weight <= 100):
            price = 15000
        if (weight > 100 and weight <= 1000):
            price = 20000
        if weight > 1000:
            price = 'Weight exceeded'
        return price


    @staticmethod
    def validate_strings(args):
        for i in args:
            if not isinstance(i,str) or i.isspace():
                return 'Data provided should be a string and should not be a space'

    @staticmethod
    def validate_integer(args):
        for i in args:
            if not isinstance(i,int) or i < 0:
                return 'Data provided should be an integer and should not be a positive number'
  
    
