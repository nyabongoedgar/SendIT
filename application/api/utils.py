class Helpers:

    @staticmethod
    def search(items_list,item_id,item_key): 
        for item in items_list:
            if item[item_key] == int(item_id):
                return item
          

    @staticmethod
    def gen_id(items_list,item_key):
        if len(items_list) == 0:
            item_id  = 1
            return item_id
        else:
            ##setting id if list is not empty
            last_dict = items_list[len(items_list)-1]
            id = int(last_dict[item_key])
            item_id = int(id + 1)
            return item_id

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


    staticmethod
    def validate_strings(args):
        for i in args:
            if not isinstance(i,str) or i.isspace():
                return 'Data provided should be a string and should not be a space'

    staticmethod
    def validate_integer(args):
        for i in args:
            if not isinstance(i,int) or i < 0:
                return 'Data provided should be an integer and should not be a positive number'
    @staticmethod    
    def modify_status(mylist,key,new_entry,parcelId):
	    for i in mylist:
		    if i[key] == parcelId:
			    i['status'] = new_entry
	    return i
